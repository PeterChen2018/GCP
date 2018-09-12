from selenium import webdriver
from time import sleep

url = 'http://www.google.com'

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

browser.find_element_by_id('gb_70').click()  # 按右上角的 登入 鈕
browser.find_element_by_id('Email').clear()
browser.find_element_by_id('Email').send_keys('您的 Email 帳號')
browser.find_element_by_id('next').click()  # 按 下一步 鈕
sleep(3)  # 必須加入等待，否則會有誤動作
browser.find_element_by_id('Passwd').clear()
browser.find_element_by_id('Passwd').send_keys('您的密碼')
browser.find_element_by_id('signIn').click()  # 按 登入 鈕