# -*- coding:utf-8 -*-
# !/usr/bin/env
'''
Author:袁麻麻
Data：2019/05/31
Describe: 鼠标和键盘事件
'''
from selenium import webdriver
import time
# 导入鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
# 导入键盘事件
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
url = r'http://www.baidu.com'
driver = webdriver.Firefox()
driver.get(url)

'''
鼠标一般事件
context_click() 右击
double_click() 双击
drag_and_drop(source, target)拖动
move_to_element() 鼠标悬停

'''
# 创建鼠标事件地点
mouse = driver.find_element_by_link_text('设置')
# 选择鼠标动作
ActionChains(driver).move_to_element(mouse).perform()
time.sleep(1)
driver.find_element_by_link_text('搜索设置').click()

'''
键盘一般事件
send_keys(Keys.BACK_SPACE) 删除键（BackSpace）
send_keys(Keys.SPACE) 空格键(Space)
send_keys(Keys.TAB) 制表键(Tab)
send_keys(Keys.ESCAPE) 回退键（Esc）
send_keys(Keys.ENTER) 回车键（Enter）
send_keys(Keys.CONTROL,'a') 全选（Ctrl+A）
send_keys(Keys.CONTROL,'c') 复制（Ctrl+C）
send_keys(Keys.CONTROL,'x') 剪切（Ctrl+X）
send_keys(Keys.CONTROL,'v') 粘贴（Ctrl+V）
send_keys(Keys.F1) 键盘F1
……
Send_keys(Keys.F5)键盘F5
…
send_keys(Keys.F12) 键盘F12

'''
time.sleep(3)
driver.quit()