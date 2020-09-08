#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 18:20
# @Author  : wenlei

'''
统计文本中出现次数最多的单词/前三的单词
'''

# 测试用例：单行文件 多行文件 空白文件 标点符号 只有标点符号 只有空格 多空格 出现次数一样 超长本文 其他字符

import sys

dict = {}
try:
    while True:
        line = input()
        if line == '':
            break
        line = line.replace(',', ' ')
        line = line.replace('.', ' ')
        line = line.replace(';', ' ')
        strs = line.split()
        for str in strs:
            if str in dict:
                dict[str] += 1
            else:
                dict[str] = 1
except:
    pass

sort_dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)
print(sort_dict)


# file = open('article.txt','r')
# dict = {}
# for line in file:
#     line = line.replace(',', ' ')
#     line = line.replace('.', ' ')
#     line = line.replace(';', ' ')
#     strs = line.split()
#     for str in strs:
#         if str in dict:
#             dict[str] += 1
#         else:
#             dict[str] = 1
#
# sort_dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)
# print(sort_dict)