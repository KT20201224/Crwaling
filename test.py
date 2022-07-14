from selenium import webdriver
import selenium
import time

driver = webdriver.Chrome("/home/kt/kt/chromedriver")

driver.get("https://www.google.com")

driver.execute_script('window.open("about:blank", "_blank");')
driver.execute_script('window.open("about:blank", "_blank");')

driver.widnow_handles[0]

tabs = driver.widnow_handles[0]

driver.switch_to.window(tabs)
driver.get("https://www.naver.com")