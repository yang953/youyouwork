#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author:袁麻麻
Data： 2019/06/03
Describe:selenium 环境安装和初步使用
'''


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

    print("出现次数最多的数字是：" + str(max_str),"\n按从小到大排序结果：" + str(min_str),"\n排序去从结果：" + str(num_list))


if __name__ == "__main__":
    list_num = [1, 6, 8, 11, 9, 1, 8, 6, 8, 7, 8]
    work_01(list_num)

