# -*- coding:utf-8 -*-
# !/usr/bin/env
'''
Author:袁麻麻
Data：2019/05/31
Describe: 各种元素定位
'''
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("http://www.baidu.com")

# element 和 elements 单数和复数的区别
# 一条普通的元素属性<input id="kw" class="s_ipt" autocomplete="off" maxlength="255" value="" name="wd">

# 1.通过定位元素ID
# element = driver.find_element_by_id('kw').send_keys('袁麻麻博客园')

# 2.通过定位元素名称name
# element = driver.find_element_by_name('wd').send_keys('袁麻麻博客园')

# 3.通过定位元素class
# element = driver.find_element_by_class_name('s_ipt').send_keys('袁麻麻博客园')

# 4.通过定位元素标签tag, 标签是指元素属性开头标记
# 元素标签存在多个时会报错Traceback (most recent call last):元素标签不唯一，这时需要使用其他方法
# element = driver.find_element_by_tag_name('input').send_keys('袁麻麻博客园')

# 5.通过定位元素超链接link
# element = driver.find_element_by_link_text('新闻').click()

# 6.通过定位元素超长连接partial link 该方法是link的强化版，可以只匹配其中一部分
# element = driver.find_element_by_partial_link_text('hao1').click()

# 7.通过定位元素xpath
# element = driver.find_element_by_xpath(".//*[@id='kw']").send_keys('袁麻麻博客园')

# 8.通过定位元素的css
element = driver.find_element_by_css_selector('#kw').send_keys('袁麻麻博客园')

time.sleep(3)
driver.quit()