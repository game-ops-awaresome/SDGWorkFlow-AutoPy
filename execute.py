#coding=utf-8
import time as T
from selenium import webdriver
from selenium.webdriver.common.by import By

class WorkFlowOperate():
    def Log_newuser(self, driver, baseURL, loginuser):
        driver.implicitly_wait(30) # 隐性等待，最长等30秒
        driver.get(baseURL)
        username = driver.find_element(By.ID, "UserName")
        username.clear()
        print ('~$LoginID : '+loginuser)
        username.send_keys(loginuser)
        password = driver.find_element(By.ID, "password1").send_keys("c")
        login = driver.find_element_by_xpath("//html//body//div[2]//div[2]//table//tbody//tr[6]//td[1]//input")
        login.click()
        
    def Log_out(self,driver):
        driver.close()
        
    def Into_FlowSheet(self, driver, FlowID):
        driver.find_element_by_link_text(FlowID).click()
        driver.switch_to_window(driver.window_handles[1])

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
    user = "zhaoruntong.falcon"
    flow = "GMSWBRWD18000098"
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSystemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'
    driver = webdriver.Ie()


    mission = WorkFlowOperate()
    mission.Log_newuser(driver, url, user)
    mission.Into_FlowSheet(driver, flow)
    mission.Sheet_Operate(driver, "Pass")
    mission.Log_out(driver)

