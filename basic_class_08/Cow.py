#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 10:24
# @Author  : wenlei

'''
母牛问题
'''

def countCow1(n):
    if n < 4:
        return n
    return countCow1(n - 1) + countCow1(n - 3)

def countCow2(n):
    if n < 4:
        return n
    res = 3
    resPre = 2
    resPrePre = 1
    for i in range(4, n + 1):
        tmp = res
        res = res + resPrePre
        resPrePre = resPre
        resPre = tmp
    return res

if __name__ == '__main__':
    n = 7
    print(countCow1(n))
    print(countCow2(n))
