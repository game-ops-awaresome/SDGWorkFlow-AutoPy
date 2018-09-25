# WorkFlow-AutoPy
**SDGWorkFlow-AutoPy** 是盛大游戏工作流系统自动化测试及过流脚本的python支持包
## 基础支持说明 <br> 
编译环境及工具包:

- **Python** (`3.5.4`及以上) 
- **Selenium** (`3.14.1`) and *webdriver* (`Ie`for Selenium`3.14.0`)
- **pymysql** (`0.9.2`及以上)
- **xlwt** (`1.3.0`)




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