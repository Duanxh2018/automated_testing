# -*- coding: utf-8 -*-
import sys
from imp import reload

reload(sys)
sys.setdefaultencoding('utf8')

import xlrd
def getTestData(testDataFile, testScene, host, CaseNo):
    '''
    从excel中获取测试数据
    :param testDataFile: 测试数据文件
    :param testScene: 测试场景
    :param host: 服务器主机
    :param caseNo: 用例No
    :param method: 请求方法
    :return: url，用例No，用例名称，请求参数，预期返回码，预期响应内容
    '''
    CaseNo = int(CaseNo)
    data = xlrd.open_workbook(testDataFile)
    table = data.sheet_by_name(testScene)
    cols = table.ncols

    resource_path = table.cell(1, 1).value  # 文件路径
    url = "http://" + host + resource_path  # 访问的url
    method = table.cell(2, 1).value  # 请求方法

    dict_params ={}
    for i in range(cols):
        dict_params[table.cell(3, i).value] = table.cell(CaseNo+3, i).value

    CaseNo = dict_params.pop("CaseNo")
    CaseDescription = dict_params.pop("Description")
    data = dict_params.pop("body")
    CaseName = dict_params.pop("CaseName")
    expectCode = str(dict_params.pop("expect_code"))
    expectContent = dict_params.pop("expect_content")
    testName = str(CaseName) + "_" + str(CaseDescription) + "_" + str(CaseNo)

    expectContent = expectContent.encode('utf-8')
    data = data.encode('utf-8')

    return method, url, CaseNo, testName, data, expectCode, expectContent

def getTestCaseNum(testDataFile, testScene):
    '''
    获取testScene测试场景中的测试用例数
    :param testDataFile: 测试数据文件
    :param testScene: 测试场景
    :return: 测试用例数
    '''
    data = xlrd.open_workbook(testDataFile)
    table = data.sheet_by_name(testScene)
    rows = table.nrows
    return rows-4

def getTestHttpMethod(testDataFile, testScene):
    '''
    获取testScene测试场景的请求方法
    :param testDataFile: 测试数据文件
    :param testScene: 测试场景
    :return: 请求方法
    '''
    data = xlrd.open_workbook(testDataFile)
    table = data.sheet_by_name(testScene)
    method = table.cell(2, 1).value  # 请求方法
    return method

if __name__ == "__main__":
    testDataFile = "D:\\Officel\\RFprojects\\automated_testing\\testData\\testData.xlsx"
    testScene = "GetAccount"
    host = "192.168.1.13:8093"
    method, url, caseNo, testName, data, expectCode, expectContent = getTestData(testDataFile, testScene, host, 12)
    print(url)
    print expectContent.encode('utf-8')
    print data.encode('utf-8')
    print(testName)
    # print(expectReuslt)