# -- coding: utf-8 --
# 登录页面元素定位
from selenium.webdriver.common.by import By
login_page={
    '用户名': (By.NAME, 'username'),
    '密码': (By.NAME, 'password'),
    '登录按钮': (By.NAME, 'login'),
    '成功页面': (By.TAG_NAME, 'body'),
    '用户名错误信息': (By.ID, 'unmsg'),
    '密码错误信息': (By.ID, 'pwmsg'),
    '注册链接': (By.LINK_TEXT,'注册'),
}