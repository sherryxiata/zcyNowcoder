#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:36
# @Author  : wenlei

'''划分问题
小于等于在左边，大于在右边
'''

import random

def partition(arr, num):
    if not arr or len(arr) < 2:
        return arr
    p = -1
    cur = 0
    while cur < len(arr):
        if arr[cur] <= num:
            p += 1
            swap(arr, cur, p)
        cur += 1
    return p + 1# 大于位置的开始下标

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

# for test
def generateArray():
    arr = [None] * 10
    for i in range(len(arr)):
        arr[i] = int(random.random() * 10)
    return arr

if __name__ == '__main__':
    test = generateArray()
    print(test)
    res = partition(test, 5)
    print(test)
    print(res)