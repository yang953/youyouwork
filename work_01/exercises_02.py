# -*- coding:utf-8 -*-
# !/usr/bin/env
'''
Author:袁麻麻
Data：2019/05/31
Describe: selenium中加载浏览器默认配置
'''
from selenium import webdriver

# 配置文件地址
file_url = r'C:\Users\admin\AppData\Roaming\Mozilla\Firefox\Profiles\t3pc4qkh.default'
# 加载默认参数
profile = webdriver.FirefoxProfile(file_url)

driver = webdriver.Firefox(profile)

driver.get("http://www.baidu.com")

driver.quit()