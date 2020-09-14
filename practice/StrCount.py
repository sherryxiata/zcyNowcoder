#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 15:31
# @Author  : wenlei

'''
统计字符串2在字符串1中出现的次数
'''

def count(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i:len(s2)] == s2:
            cnt += 1
    return cnt

if __name__ == '__main__':
    s1 = '1111223'
    s2 = '11'
    print(count(s1, s2))