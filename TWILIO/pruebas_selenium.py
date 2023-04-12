from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(options=options)
browser.implicitly_wait(10)
browser.get('https://github.com')

link = browser.find_element(By.LINK_TEXT, 'Sign in')
link.click()
user_input = browser.find_element(By.ID, 'login_field')
password = browser.find_element(By.ID, 'password')

user_input.send_keys('user')
password.send_keys('password')
pass_input.send_keys(Keys.RETURN)