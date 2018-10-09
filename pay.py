#!/usr/bin/env python3
#coding=utf-8
import execute as ex
from optional import OptionSet
from selenium import webdriver




if __name__ == "__main__":
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSystemCode=1134&EntranceCode=17&RType=1&ReturnUrl=http%3a%2f%2f192.168.104.117%2fSDG.Workflow.Platform%2fLogin.aspx'

    
    user = 'zhangshuping'
    flow = "盛大游戏付款申请流程"
    
    #OptionSet = OptionSet()
    #chrome_opt = OptionSet.Broser_Images()
    #driver = webdriver.Chrome(chrome_options = chrome_opt)
    driver = webdriver.Ie()
    mission = ex.WorkFlowOperate()
    mission.Log_newuser(driver, url, user)
    mission.Start_FlowSheet(driver, flow)

    
    driver.switch_to_window(driver.window_handles[1])

    #一次性付款清单
    driver.find_element_by_xpath('//*[@id="Form1"]/table/tbody/tr[1]/td/table[2]/tbody/tr[1]/td[3]/font/a/font').click()

    driver.find_element_by_id('ctl00_ContentHolder_ProTitle').send_keys('script~# 一次性付款清单')
    #driver.switch_to_window(driver.window_handles[1])
    #driver.find_element_by_xpath('//*[@id="VendorName"]').send_keys('上海')
    
    #非一次性付款清单
    #driver.find_element_by_xpath('//*[@id="Form1"]/table/tbody/tr[1]/td/table[2]/tbody/tr[2]/td[3]/font/a/font').click()


#//*[@id="Form1"]/table/tbody/tr[1]/td/table[2]/tbody/tr[2]/td[3]/font/a/font
