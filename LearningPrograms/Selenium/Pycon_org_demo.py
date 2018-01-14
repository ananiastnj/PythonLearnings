from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("C:\\JUnit\\chromedriver.exe")
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("arun")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
print("Success")
time.sleep(5)
driver.close()