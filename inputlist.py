#coding=utf-8
import re
import execute as ex
import readsql as sq
from selenium import webdriver

class ChainOperate():
    
    def Get_Chain(self, driver):
        name = []
        ChainID = []
        record = False
        getway = sq.SQLOperate()#实例化数据库操作
        titleelems = driver.find_elements_by_class_name('name')#name class元素全抓取
        character = driver.find_elements_by_class_name('mouse')#mouse class元素全抓取
        print('一共找到 '+str(len(titleelems))+' 个审批人！:')
        for i in range(len(titleelems)):
            print(titleelems[i].text+'\t----', end=' ')
            print(character[i].text)
            if '[当前审批]' in titleelems[i].text:
                record = True
            if record == True:
                name.append(re.sub(u"\\（.*?\\）|\\(.*?\\)|\\{.*?}|\\[.*?]|\\ ", "", titleelems[i].text))
        for j in range(len(name)):
            ChainID.append(getway.GetLoginname(name[j]))                   
        return ChainID
    
    def Get_FlowID(self, driver):
        titleelems = driver.find_element_by_id('ctl00_Folio').get_attribute("value")        
        return titleelems


if __name__ == "__main__":
    user = "zhaoruntong.falcon"
    flow = "GMSWBRWD18000104"
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSy\
stemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192\
.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'
    
    driver = webdriver.Ie()
    c = ex.WorkFlowOperate()
    Mission = ChainOperate()
    c.Log_newuser(driver, url, user)
    c.Into_FlowSheet(driver, flow)
    print(Mission.Get_FlowID(driver))
    print(Mission.Get_Chain(driver))
    c.Log_out(driver)
