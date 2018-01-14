from selenium import webdriver
import json
import time

with open('C://Users/ajesuraj/PycharmProjects/FacebookAuto/dataFiles/fb_login_json.json') as login_file:
    login_data = json.load(login_file)

u_name = login_data["username"]
passwd = login_data["password"]
#driver = webdriver.Chrome("C://Users//ajesuraj//PycharmProjects//PrimeInfrastructreMaui//Drivers//chromedriver.exe")
driver = webdriver.Chrome("C://JUnit//chromedriver.exe")
def browser_open():
    driver.get("http://myhcl.com")
    #driver.get("http://facebook.com")
    wait_ten_sec()

def fb_login():
    driver.find_element_by_css_selector("#email").send_keys(u_name)
    wait_one_sec()
    driver.find_element_by_css_selector("#pass").send_keys(passwd)
    wait_one_sec()
    driver.find_element_by_css_selector("#loginbutton").click()
    wait_five_sec()

def wait_one_sec():
    driver.implicitly_wait(1)

def wait_five_sec():
    driver.implicitly_wait(5)

def wait_ten_sec():
    driver.implicitly_wait(10)

def fb_logout():
    driver.find_element_by_css_selector("#userNavigationLabel").click()
    wait_one_sec()
    driver.find_element_by_css_selector("#js_11 > div > div > ul > li:nth-child(13) > a").click()
    wait_one_sec()

browser_open()
fb_login()
fb_logout()
