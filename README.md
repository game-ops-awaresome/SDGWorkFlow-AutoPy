# WorkFlow-AutoPy
**SDGWorkFlow-AutoPy** 是盛大游戏工作流系统自动化测试及过流脚本的python支持包
## 基础支持说明 <br> 
编译环境及工具包:

- **Python** (`3.5.4`及以上) 
- **Selenium** (`3.14.1`) and *webdriver* (`Ie`for Selenium`3.14.0`)
- **pymysql** (`0.9.2`及以上)
- **xlwt** (`1.3.0`)


支持包使用前，务必实例化浏览器驱动<br>
`from selenium import webdriver `<br>
`driver = webdriver.Ie()`


## execute.py  <br>

**execute.py**为脚本的浏览器操作包<br>
### 导入支持包：<br>
`import execute as ex `<br>
<br>
### *exevute.py*基础环境包函:<br>
`import time as T`<br>
`from selenium import webdriver`<br>
`from selenium.webdriver.common.by import By`<br>
`from selenium.webdriver.support.select import Select`<br>
<br>
### 网页及工作流操作脚本类：`WorkFlowOperate()`
**实例化：**`exmple = ex.WorkFlowOperate()`<br>

- **登入新账户：**` Log_newuser(self, driver, baseURL, loginuser)`<br>
- **登出：**` Log_out(self,driver)`<br>
- **进入流程单：**` Into_FlowSheet(self, driver, FlowID)`<br>
- **进入最近一次发起流程：**` Into_lastFlow(self, driver)`<br>
- **发起流程：**` Start_FlowSheet(self, driver, FlowType)`<br>
- **流程单操作：**` Sheet_Operate(self, driver, Operate)`<br>




## inputlist.py <br>

**inputlist.py**为脚本的审批信息拉取及表单信息拉取操作包<br>
### 导入支持包：<br>
`import inputlist as ls `
<br>
### *inputlist.py*基础环境包函:<br>
`import re`<br>
`import execute as ex`<br>
`import readsql as sq`<br>
`from selenium import webdriver`<br>
<br>
### 信息抓取操作脚本类：`ChainOperate()`
**实例化：**`example = ls.ChainOperate()`<br>

- **拉取审批链：**` Get_Chain(self, driver)`<br>
- **拉取单号：**` Get_FlowID(self, driver)`<br>




## readsql.py <br>
**readsql.py**为脚本的数据库操作包<br>
### 导入支持包：<br>
`import readsql as sq`
<br>
### *readsql.py*基础环境包函:<br>
`import pymysql`<br>
<br>
### SQL数据库操作脚本类：`SQLOperate()`
**实例化：**`example = sq.SQLOperate()`<br>

- **从数据库读取账号：**` GetLoginname(self, name)`<br>


## passroll.py <br>
**passroll.py**为脚本的通过流程操作包<br>
### 导入支持包：<br>
`from passroll import *`
<br>
### *passroll.py*基础环境包函:<br>
`import time as T`<br>
`import execute as ex`<br>
`import inputlist as ls`<br>
`from selenium import webdriver`<br>
<br>
### SQL数据库操作脚本类：`SQLOperate()`
**实例化：**`example = Passroll()`<br>

- **通过流程：**` passoperate(self, driver, url, user, flow)`<br>