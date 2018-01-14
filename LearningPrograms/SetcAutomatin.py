from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time

src1 = "Thanjavur"
dest1 = "Chennai"

driver = webdriver.Chrome("C://Users//ajesuraj//PycharmProjects//PrimeMaui-new//Drivers//chromedriver.exe",chrome_options=Options())
time.sleep(3)
#driver.maximize_window()
#print("Maximized window")
print("Web Browser Opened")
driver.get("https://www.redbus.in/")
print("URL Opened")
time.sleep(10)
#driver.switch_to_alert().accept()
#driver.find_element_by_xpath("//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']").click()
#time.sleep(5)
#time.sleep(5)
driver.find_element_by_id("src").send_keys(src1)
print("Src : Thanjavur")
time.sleep(1)
driver.find_element_by_id("dest").send_keys(dest1)
print("Dest : Chennai")
time.sleep(1)
driver.find_element_by_xpath("//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']").click()
driver.find_element_by_xpath("//span[@class='fl icon-calendar_icon-new icon-onward-calendar icon']").click()
#driver.find_element_by_id("onward_cal").click()
#driver.find_element_by_xpath("//input[@id="rb-calendar_onward_cal"]/table/tbody/tr[6]/td[4]",)
print("Calander clicked")
time.sleep(3)
i=6
j=5
driver.find_element_by_xpath("//div[@class='rb-calendar']/table/tbody/tr[{}]/td[{}]".format(i,j)).click()
print("picked a date")
time.sleep(3)
driver.find_element_by_id("search_btn").click()
print("Search bus button clicked")
time.sleep(3)
#driver.quit()
#time.sleep(3)
#print("Web Browser closed")
'''
//*[@id="buses_viewonward"]/div/ul/li[1]
//*[@id="buses_viewonward"]/div/ul/li[3]/div[1]/div/div[1]/div[3]/div[1]
//c = b.find_element_by_xpath(".//div[1]/div/div[1]/div[3]/div[@class='service-name']").text
//*[@id="buses_viewonward"]/div/ul/li[3]/div[1]/div/div[1]/div[7]/div[2]/button

//*[@id="buses_viewonward"]/div/ul/li[3]/div[1]/div/div[1]/div[7]/div[2]/button
//*[@id="buses_viewonward"]/div/ul/li[4]/div[1]/div/div[1]/div[7]/div[2]/button
'''

a = driver.find_elements_by_xpath('//*[@id="buses_viewonward"]/div/ul/li')
for b in a:
    c = b.find_element_by_xpath(".//div[@class='service-name']").text
    if(c=="Rathimeena Travels"):
        print(c)

#//*[@id="buses_viewonward"]/div/ul/li[3]/div[1]/div/div[1]/div[7]/div[2]/button


