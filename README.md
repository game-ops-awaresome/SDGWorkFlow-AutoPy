# WorkFlow-AutoPy
**SDGWorkFlow-AutoPy** 是盛大游戏工作流系统自动化测试及过流脚本的python支持包
## 基础支持说明 ##
编译环境及工具包:

- **Python** (`3.5.4`及以上) 
- **Selenium** (`3.14.1`) and *webdriver* (`Ie`for Selenium`3.14.0`)
- **pymysql** (`0.9.2`)




## execute.py  <br>

**execute.py**为脚本的浏览器操作包<br>
导入支持包：<br>
`import execute as ex `<br>
<br>*exevute.py*基础环境包函:<br>
`import time as T`<br>
`from selenium import webdriver`<br>
`from selenium.webdriver.common.by import By`<br>
`from selenium.webdriver.support.select import Select`<br>

## inputlist.py <br>

**inputlist.py**为脚本的审批信息拉取及表单信息拉取操作包<br>
导入支持包：<br>
`import inputlist as ls `
<br>*inputlist.py*基础环境包函:<br>
`import re`<br>
`import execute as ex`<br>
`import readsql as sq`<br>
`from selenium import webdriver`<br>

## readsql.py <br>
**readsql.py**为脚本的数据库操作包<br>
导入支持包：<br>
`import readsql as sq`
<br>*readsql.py*基础环境包函:<br>
`import pymysql`<br>
