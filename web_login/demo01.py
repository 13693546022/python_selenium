# -- coding: utf-8 --
from selenium import webdriver
from selenium.webdriver.common.by import By
from operate.operate_element import Operate_page
from time import sleep
a_page={
    'b链接': (By.LINK_TEXT, 'B页面'),
    'c链接': (By.LINK_TEXT, 'C页面'),
    'd链接': (By.LINK_TEXT, 'D页面'),
    '页面文本': (By.TAG_NAME, 'body')
} #页面元素定位
page=Operate_page()
page.open_browser()
page.open_page('file:///C:/Users/86136/Documents/Tencent%20Files/895647970/FileRecv/Selenium-Day10/Selenium-Day10/a.html')
page.click(a_page['b链接'])
page.click(a_page['c链接'])
page.click(a_page['d链接'])
page.switch_window('B页面')
print(page.get_text(a_page['页面文本']))
sleep(3)
page.quit_browser()