# -- coding: utf-8 --
import unittest
from locate.page_login import login_page
from operate.operate_element import Operate_page
from common.conf import Conf
from common.db import DB
from common.case import read_case
from parameterized import parameterized
import warnings
from time import sleep
import time
from HTMLTestRunner import HTMLTestRunner
from common.log import log
case = read_case('web_login.xlsx', ['用例编号', '用例名称', '用户名', '密码', '登录前页面预期', '登录后弹窗预期', '登录后页面预期'])

class Login(unittest.TestCase, Operate_page):
    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning) # 忽略资源警告
        DB().init_db('login.sql')
        Login.open_browser() # 打开浏览器
    def setUp(self) -> None:
        self.open_page(Conf().url) # 打开被测页面
    @classmethod
    def tearDownClass(cls) -> None:
        cls.quit_browser()
    @parameterized.expand(case)
    def test_login(self, case_info, username, password, pre_login_expect, alert_expect, after_login_expect):
        sleep(3)
        self.input_text(login_page['用户名'], username)
        self.input_text(login_page['密码'],password)
        unmsg_expect, pwmsg_expect=pre_login_expect.replace('空字符串','').split(';')
        # print(unmsg_expect, pwmsg_expect)
        unmsg_actual, pwmsg_actual=self.get_text(login_page['用户名错误信息']), self.get_text(login_page['密码错误信息'])
        self.assertEqual(unmsg_expect, unmsg_actual)
        self.assertEqual(pwmsg_expect, pwmsg_actual)
        if 'login_01' not in case_info:
            self.click(login_page['登录按钮'])
        if alert_expect: # 有弹窗
            sleep(3)
            alert_actual=self.get_alert_text()
            self.assertEqual(alert_expect, alert_actual)
        if after_login_expect:
            sleep(3)
            if '*' in after_login_expect:
                unmsg_expect, pwmsg_expect=after_login_expect.replace('空字符串','').split(';')
                # print(unmsg_expect,pwmsg_expect)
                unmsg_actual, pwmsg_actual=self.get_text(login_page['用户名错误信息']), self.get_text(login_page['密码错误信息'])
                # print(unmsg_actual,pwmsg_actual)
                try:
                    self.assertEqual(unmsg_expect,unmsg_actual)
                    log().info(f'{case_info}==测试成功')
                except AssertionError:
                    msg=f'{case_info}==测试失败==预期：{unmsg_expect}==实际：{unmsg_actual}'
                    log().warning(msg)
                    raise AssertionError(msg)
                except BaseException as e:
                    log().error(f'错误类型：{type(e).__name__}==错误内容：{e}')
                    exit()
                try:
                    self.assertEqual(pwmsg_expect,pwmsg_actual)
                    log().info(f'{case_info}==测试成功')
                except AssertionError:
                    msg=f'{case_info}==测试失败==预期：{pwmsg_expect}==实际：{pwmsg_actual}'
                    log().warning(msg)
                    raise AssertionError(msg)
                except BaseException as e:
                    log().error(f'错误类型：{type(e).__name__}==错误内容：{e}')
            else:
                actual=self.get_text(login_page['成功页面'])
                try:
                    self.assertEqual(actual, after_login_expect)
                    log().info(f'{case_info}==测试成功')
                except AssertionError:
                    msg = f'{case_info}==测试失败==预期：{after_login_expect}==实际：{actual}'
                    log().warning(msg)
                except BaseException as e:
                    log().error(f'错误类型：{type(e).__name__}==错误内容：{e}')
        sleep(3)

if __name__ == '__main__':
    # unittest.main()
    loader=unittest.defaultTestLoader
    suite=loader.discover('../testcase', '*.py')
    now=time.strftime('%Y%m%d_%H%M%S')
    report_file=open(f'../report/{now}.html', 'wb')
    runner=HTMLTestRunner(report_file, title='webtest测试报告', description='测试环境描述', verbosity=2)
    runner.run(suite)