#!/usr/bin/env python3
#coding=utf-8
from selenium import webdriver  
import os

class OptionSet():
    def Broser_Images(self):
        opt = webdriver.ChromeOptions()
        opt.add_argument("--start-maximized")
        return opt
    
    def Broser_NoImages(self):
        opt = webdriver.ChromeOptions()
        prefs = {'profile.managed_default_content_settings.images':2}
        opt.add_experimental_option('prefs', prefs)
        opt.add_argument("--start-maximized")
        return opt
    
    def NoBroser_NoImages(self):
        opt = self.Broser_NoImages()
        opt.set_headless()
        opt.add_argument('--disable-gpu')
        return opt

#op
if __name__ == "__main__":
    url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSy\
stemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192\
.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'
    user = 'zhaoruntong.falcon'
  
    OptionSet = OptionSet()
    chrome_opt = OptionSet.Broser_NoImages()

    #实例化
    driver = webdriver.Chrome(chrome_options = chrome_opt)
