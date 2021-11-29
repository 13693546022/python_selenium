# -- coding: utf-8 --
from selenium.webdriver.support.select import Select
from selenium import webdriver
class Operate_page:
    # 打开浏览器
    @classmethod
    def open_browser(cls):
        cls.browser=webdriver.Firefox()
        cls.browser.implicitly_wait(10)
    # 打开网页
    def open_page(self,url):
        self.browser.get(url)
    # 关闭当前网页
    def close_page(self):
        self.browser.close()
    # 退出浏览器
    @classmethod
    def quit_browser(cls):
        cls.browser.quit()
    # 清除文本框、密码框、多行文本框中的文字
    def clear(self,element):
        self.browser.find_element(*element).clear()
    # 在文本框、密码框、多行文本框中输入文字
    def input_text(self,element,text):
        self.browser.find_element(*element).send_keys(text)
    # 单击单选按钮、命令按钮、复选框、链接
    def click(self,element):
        self.browser.find_element(*element).click()
    # 选择下拉列表、列表框中的项
    def select(self,element,index=None,text=None,value=None):
        select_object=Select(self.browser.find_element(*element))
        if index:
            select_object.select_by_index(index)
        elif text:
            select_object.select_by_visible_text(text)
        elif value:
            select_object.select_by_value(value)
        else:print('请使用下标、可视文本、值选择元素')
    # 获得属性
    def get_attribute(self,element,attribute):
        return self.browser.find_element(*element).get_attribute(attribute)
    # 获得文本
    def get_text(self,element):
        return self.browser.find_element(*element).text
    # 获得网页标题
    def get_title(self):
        return self.browser.title
    # 切换弹窗：获得弹窗文字，并点确定
    def get_alert_text(self):
        alert=self.browser.switch_to.alert
        text=alert.text
        alert.accept()
        return text
    # 切换框架
    def switch_frame(self,index_id_name=None,element=None):
        if index_id_name:
            self.browser.switch_to.frame(index_id_name)
        elif element:
            self.browser.switch_to.frame(*element)
        else:print('只能通过框架编号、id、name、或者其他定位方式切换框架')
    # 切换窗口
    def switch_window(self,title=None):
        if title:
            windows=self.browser.window_handles
            for win in windows:
                self.browser.switch_to.window(win)
                page_title=self.browser.title
                if title in page_title:
                    return
        else:print('请自己想办法切换窗口')