#coding=utf-8
import re
import execute as ex
import readsql as sq
from selenium import webdriver

class ChainOperate():
    
    def Get_Chain(self,driver):
        name = []
        ChainID = []
        getway = sq.SQLOperate()
        titleelems=driver.find_elements_by_class_name('name')
        character=driver.find_elements_by_class_name('mouse')
        print('一共找到 '+str(len(titleelems))+' 个审批人！:')
        for i in range(len(titleelems)):
            #print('字符长度：'+str(len(titleelems[i].text)))
            print(titleelems[i].text+'\t----', end=' ')
            print(character[i+1].text)
            name.append(re.sub(u"\\（.*?\\）|\\(.*?\\)|\\{.*?}|\\[.*?]|\\ ", "", titleelems[i].text))
        for i in range(len(name)):
            ChainID.append(getway.GetLoginname(name[i]))                   
        return ChainID


if __name__ == "__main__":
    user = "lujinwei.simple"
    flow = "GMSWBRWD18000054"
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSy\
stemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192\
.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'
    
    driver = webdriver.Ie()
    c = ex.WorkFlowOperate()
    Mission = ChainOperate()
    c.Log_newuser(driver, url, user)
    c.Into_FlowSheet(driver, flow)
    flowList = Mission.Get_Chain(driver)
    print(flowList)
    #c.Log_out(driver)
