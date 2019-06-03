#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
Author:袁麻麻
Data：
Describe:
'''
list_num = [i for i in range(100,1000) if((i%10)**3 + ((i//10)%10)**3 + (i//10)**3) == i]
print(list_num)