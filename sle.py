from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Auto-download and install the correct ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a website to test
driver.get("https://www.google.com")
print("Browser opened successfully!")

driver.quit()
