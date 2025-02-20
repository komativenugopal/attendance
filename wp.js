const { default: makeWASocket, useSingleFileAuthState } = require('@whiskeysockets/baileys');
const { state, saveState } = useSingleFileAuthState('./auth.json');
const { exec } = require('child_process');

const studentData = {}; // Store credentials per user session

async function startBot() {
    const sock = makeWASocket({ auth: state });

    sock.ev.on('creds.update', saveState);

    sock.ev.on('messages.upsert', async (msg) => {
        const message = msg.messages[0];
        if (!message.message) return;

        const sender = message.key.remoteJid;
        const text = message.message.conversation?.trim().toLowerCase() || '';

        console.log(`Received: "${text}" from ${sender}`);

        if (text === 'attendance') {
            sock.sendMessage(sender, { text: "Please send your login ID." });
            studentData[sender] = { step: 'waiting_for_id' };
        } else if (studentData[sender]?.step === 'waiting_for_id') {
            studentData[sender].username = text;
            studentData[sender].step = 'waiting_for_password';
            sock.sendMessage(sender, { text: "Now send your password." });
        } else if (studentData[sender]?.step === 'waiting_for_password') {
            studentData[sender].password = text;
            sock.sendMessage(sender, { text: "Fetching your attendance... Please wait." });

            exec(`python scrape_attendance.py ${studentData[sender].username} ${studentData[sender].password}`, (error, stdout) => {
                if (error) {
                    sock.sendMessage(sender, { text: "Failed to fetch attendance. Please check your credentials." });
                } else {
                    sock.sendMessage(sender, { text: `Your attendance: ${stdout.trim()}` });
                }
                delete studentData[sender]; // Clear session data
            });
        }
    });
}

startBot();
