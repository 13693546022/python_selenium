# -- coding: utf-8 --
# 读用例
import pandas
from common.log import log
def read_case(xlsfile,columns=None):
    try:
        xlsfile='../excelcase/'+xlsfile
        data=pandas.read_excel(xlsfile,usecols=columns,keep_default_na=False)
        # print(data)
        case_info=data['用例编号']+':'+data['用例名称']
        data.insert(0,'用例信息',case_info)
        data.drop(['用例编号','用例名称'],axis=1,inplace=True)
        case=data.values.tolist()
        log().info(f'读用例文件{xlsfile}成功')
        return case
    except BaseException as e:
        log().error(f'错误类型：{type(e).__name__}==错误内容：{e}')
        exit()

if __name__ == '__main__':
    read_case('login.xlsx', ['用例编号','用例名称','用户名','密码','登录前页面预期','登录后弹窗预期','登录后页面预期'])