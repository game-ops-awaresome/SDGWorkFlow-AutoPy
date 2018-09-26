#coding=utf-8
import time as T
import execute as ex
import inputlist as ls
from selenium import webdriver


if __name__ == "__main__":
    user = "zhaoruntong.falcon"
    flow = "GMSWBZXD18000015"
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSy\
stemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192\
.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'
    
    driver = webdriver.Ie()
    action = ex.WorkFlowOperate()
    ID = ls.ChainOperate()
    action.Log_newuser(driver, url, user)
    action.Into_FlowSheet(driver, flow)
    flowList = ID.Get_Chain(driver)
    action.Log_out(driver)
    T.sleep(10)

    for i in range(len(flowList)):
        driver = webdriver.Ie()
        action.Log_newuser(driver, url, flowList[i])
        action.Into_FlowSheet(driver, flow)
        action.Sheet_Operate(driver, "Pass")
        action.Log_out(driver)
        T.sleep(10)
