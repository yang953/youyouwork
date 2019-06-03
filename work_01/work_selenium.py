#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author:袁麻麻
Data： 2019/06/03
Describe:selenium 环境安装和初步使用
'''
from selenium import webdriver
import time
def firefox(url,url1):
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.get(url) #访问百度
    time.sleep(5)
    browser.find_element_by_xpath("//*[@id='kw']").send_keys("上海-悠悠")
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="su"]').click()
    time.sleep(2)
    browser.get(url1) # 访问博客园
    time.sleep(3)
    browser.back() # 回退上一个页面
    time.sleep(2)
    browser.forward() # 下一个页面
    time.sleep(3)
    browser.refresh() # 刷新页面
    browser.close() # 关闭当前窗口
    browser.quit() # 退出浏览器，清空临时文件

def work_01(list_num):
    temp = 0
    num_list = []
    for i in list_num:
        if list_num.count(i) > temp:
            max_str = i
            temp = list_num.count(i)

    min_str = sorted(list_num)

    for b in min_str:
        if b not in num_list:
            num_list.append(b)

    print("出现次数最多的数字是：" + str(max_str),"\n按从小到大排序结果：" + str(min_str),"\n排序去重结果：" + str(num_list))


if __name__ == "__main__":
    list_num = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
    # work_01(list_num)
    url = "https://www.baidu.com/"
    url1 = "https://www.cnblogs.com/"
    firefox(url,url1)