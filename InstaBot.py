from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome('./chromedriver.exe')
browser.maximize_window()
browser.get("https://www.instagram.com")

browser.find_element_by_name('username').send_keys('username')
sleep(5)
browser.find_element_by_name('password').send_keys('password')
sleep(5)

user_button = browser.find_element_by_class_name('sqdOP.L3NKy.y3zKF')
sleep(5)
user_button.click()



