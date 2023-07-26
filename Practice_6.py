from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

url = "https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true&state=%2Fwelcome"
service = Service('F:/Python/pythonProject/Selenium _test/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(url=url)
time.sleep(1)
driver.set_window_size(1366, 1330)
driver.find_element(By.NAME, "username").clear()
driver.find_element(By.NAME, "username").send_keys("demo")
driver.find_element(By.NAME, "password").clear()
driver.find_element(By.NAME, "password").send_keys("demo")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "otp-code").clear()
driver.find_element(By.ID, "otp-code").send_keys("0000")
driver.find_element(By.ID, "login-otp-button").click()
driver.find_element(By.XPATH, "//*[@id='cards-overview-index']").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[6]/div[1]/ul[1]/li[1]/ul/li[9]/a").click()
driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/div[6]/div[2]/div[9]/div[1]/div[2]/i").click()
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10104']/div[1]/div[2]/form/input[3]").clear()
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10104']/div[1]/div[2]/form/input[3]").send_keys("ХОКЕЙ")
driver.find_element(By.XPATH, "//*[@id='card-details-ownbank-10104']/div[1]/div[2]/form/button").click()
time.sleep(5)



