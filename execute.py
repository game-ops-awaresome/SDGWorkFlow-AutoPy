#coding=utf-8
import time as T
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class WorkFlowOperate():
    def Log_newuser(self, driver, baseURL, loginuser):
        driver.implicitly_wait(30) # 隐性等待，最长等30秒
        driver.get(baseURL)#get请求页面
        username = driver.find_element(By.ID, "UserName")#登录用户名栏抓取
        username.clear()#清空栏内缓存信息
        print ('~$LoginID : '+loginuser)#监视当前需要登入的账户
        username.send_keys(loginuser)#输入用户名
        password = driver.find_element(By.ID, "password1").send_keys("c")#测试环境下随意密码
        login = driver.find_element_by_xpath("//html//body//div[2]//div[2]//table//tbody//tr[6]//td[1]//input")#抓取“登录”
        login.click()#点击
        print ('~$login success')
        
    def Log_out(self,driver):
        driver.close()
        
    def Into_FlowSheet(self, driver, FlowID):
        driver.find_element_by_link_text(FlowID).click()
        driver.switch_to_window(driver.window_handles[1])
        print ('Into flowsheet :'+FlowID)

    def Start_FlowSheet(self, driver, FlowType):
        driver.find_element_by_link_text('发起流程').click()
        self.Into_FlowSheet(driver, FlowType)

    def Sheet_Operate(self, driver, Operate):
        words = driver.find_element(By.ID, "ctl00_conApproveSave_k2tbComment")
        if (Operate == "Pass"):
            Message = "~Script#$ -Pass"
            Button = "action0"
        elif (Operate == "Continue"):
            Message = "~Script#$ -Continue"
            Button = "action1"
        elif (Operate == "Repulse"):
            Message = "~Script#$ -Repulse"
            Button = "action2"
        else :
            print ("Command error in Sheet_Operate(). Please use Pass or Continue or Repulse to finish action")
            return False
        print (Message)
        words.send_keys(Message)
        approve = driver.find_element(By.ID, Button).click()
        driver.switch_to_window(driver.window_handles[0])
        
if __name__ == "__main__":
    user = "赵润彤.Falcon"
    flow = "GMSWBRWD18000102"
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSystemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'
    driver = webdriver.Ie()


    mission = WorkFlowOperate()
    mission.Log_newuser(driver, url, user)
    mission.Into_FlowSheet(driver, flow)
    mission.Sheet_Operate(driver, 'Pass')
    mission.Log_out(driver)


