from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def get_attendance():
    driver = webdriver.Chrome()
    driver.get("https://vishnu.ac.in/")  # Replace with your college site

    time.sleep(2)

    # Login
    driver.find_element(By.XPATH, "//*[@id='txtId2']").send_keys("22pa1a4254", Keys.ENTER)
    driver.find_element(By.XPATH, "//*[@id='txtPwd2']").send_keys("webcap", Keys.ENTER)

    time.sleep(5)

    # Navigate to Attendance
    driver.find_element(By.XPATH, "//*[@id='tblscreens']/tbody/tr[3]/td[2]/div").click()
    time.sleep(3)

    # Select "Till Now" and Show
    driver.find_element(By.XPATH, "//*[@id='radTillNow']").click()
    driver.find_element(By.XPATH, "//*[@id='btnShow']").click()
    time.sleep(3)

    # Get last row's attendance
    attendance = driver.find_element(By.XPATH, "//*[@id='tblReport']/table/tbody/tr[3]/td/table/tbody/tr[last()]/td[4]").text

    driver.quit()
    return attendance

if __name__ == "__main__":
    print(get_attendance())
