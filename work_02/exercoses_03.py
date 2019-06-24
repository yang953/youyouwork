# -*- coding:utf-8 -*-
# !/usr/bin/env
'''
Author:袁麻麻
Data：2019/05/31
Describe: 元素定位过程中存在问题
'''
from selenium import webdriver
import time
url = r'http://www.baidu.com'
driver = webdriver.Firefox()
driver.get(url)

# 1.元素中存在多个相同的元素属性
# 当元素中存在多个相同属性时，可以使用xpath语法在浏览器页面中所有的属性，然后根据列表索引选择其中一个元素
# xpath语法使用$x('//input)',xpath搜索使用的是路径搜索
# 多元素使用复数slements定位，结果是一个列表
elements = driver.find_elements_by_tag_name('input')[7].send_keys('袁麻麻')



# 2.当元素中的属性名称中存在空格
# eg：<input id="su" class="bg s_btn btnhover" type="submit" value="百度一下"/>
# 其中class属性就是空格连接，这时只要其中一个就行,要求是元素属性唯一
element = driver.find_element_by_class_name('s_btn').click()

# 3.通过by来操作元素

element= driver.find_element('id','kw').clear()







time.sleep(3)
driver.quit()