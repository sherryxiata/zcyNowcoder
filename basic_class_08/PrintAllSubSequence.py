#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 9:06
# @Author  : wenlei

'''
打印子序列（包括空字符串）
'''

def printAllSubsequence(str):
    arr = list(str)
    res = ''
    process(arr, 0, res)

def process(arr, i, res):
    if i == len(arr):
        print(res)
        return
    process(arr, i + 1, res) # 这一位不用
    process(arr, i + 1, res + arr[i]) # 这一位用

if __name__ == '__main__':
    a = 'abc'
    printAllSubsequence(a)