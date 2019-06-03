#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author:袁麻麻
Data：2019/06/03
Describe: 课后练习题1和2
'''

def multiplication_table():
    '''求99乘法表'''
    for i  in range(1,10):
        for j in range(1,i + 1):
            print("%d * %d = %2d" % (i,j,i*j),end=" ")
        print("")


def daffodil_num():
    '''求水仙花数'''
    list_num = []
    for i in range(100,1000):
        a = i % 10 # %除法求余数
        b = (i//10) % 10 # // 除法向下取整，然再求余数
        c = i // 100
        if a**3 + b**3 + c**3 == i:
            list_num.append(i)
    print(list_num)

if __name__ == "__main__":
    multiplication_table()
    daffodil_num()