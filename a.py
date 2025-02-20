from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

# Auto-download and install the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the college website
driver.get("https://vishnu.ac.in/")

# Wait for the page to load
time.sleep(2)

# Enter login credentials (Fixed XPath)
username = driver.find_element(By.XPATH, '//*[@id="txtId2"]')
password = driver.find_element(By.XPATH, '//*[@id="txtPwd2"]')

username.send_keys("22pa1a4254")  # Replace with actual username
password.send_keys("webcap")  # Replace with actual password

# Click login button
login_button = driver.find_element(By.XPATH, '//*[@id="imgBtn2"]')
login_button.click()

# Wait for login to complete
time.sleep(5)

webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
time.sleep(2)


# Click on the "Attendance" button in the menu
attendance_menu_button = driver.find_element(By.XPATH, '//*[@id="tblscreens"]/tbody/tr[3]/td[2]/div')
attendance_menu_button.click()

# Wait for the attendance page to load
time.sleep(3)

# Select "Till Now" radio button
till_now_button = driver.find_element(By.XPATH, '//*[@id="radTillNow"]')
till_now_button.click()

# Click the "Show" button
show_button = driver.find_element(By.XPATH, '//*[@id="btnShow"]')
show_button.click()

# Wait for the table to load
time.sleep(3)

# Find the attendance cell in the last row
attendance_value = driver.find_element(By.XPATH, '//*[@id="tblReport"]/table/tbody/tr[3]/td/table/tbody/tr[14]/td[4]').text

# Print the attendance value
print("Your Attendance:", attendance_value)

# Close the browser
driver.quit()
