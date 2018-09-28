#coding=utf-8
from tkinter import *
from tkinter import ttk
from passroll import *
from selenium import webdriver
import execute as ex

url = 'http://10.246.190.50:9554/Sso.do/?GSubSystemCode=&SubSy\
stemCode=1134&EntranceCode=16&RType=1&ReturnUrl=http%3a%2f%2f192\
.168.100.150%2fSDG.Workflow.Platform%2fLogin.aspx'

def PressButton():
    driver = webdriver.Ie()
    user = LoginID.get()
    flow = flowID.get()
    action = Passroll()
    action.passoperate(driver, url, user, flow)

root = Tk()
root.title("SDGWorkFlowScript")
root.geometry('1100x650')
root.resizable(width=False, height=False)

photo = PhotoImage(file='logo.png')
img_label = Label(root, imag=photo)
img_label.place(x=20,y=5,anchor='nw')

wordF = Label(root, text="LogingID\t: \n\nFlowID\t: ", fg = "blue", justify=LEFT)
wordF.place(x=10,y=90,anchor='nw')

e = StringVar()
e.set("zhaoruntong.falcon")
LoginID = Entry(root, fg = 'green', textvariable=e, width = 25)
LoginID.place(x=90,y=90,anchor='nw')

f = StringVar()
f.set('GMSWBRWD18000108')
flowID = Entry(root, fg = 'green', textvariable=f, width = 25)
flowID.place(x=90,y=135,anchor='nw')


Button(root,text = 'PassFlow',width = 10,height =1, command = PressButton).place(x=100,y=175,anchor='nw')


root.mainloop()


 
