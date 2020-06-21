#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:54
# @Author  : wenlei

'''荷兰国旗问题
小于的放在左边，等于的放在中间，大于的放在右边
'''

import random

def partition(arr, L, R, num):
    less = L - 1
    more = R + 1
    while L < more:
        if arr[L] < num:
            less += 1
            swap(arr, L, less)
            L += 1
        elif arr[L] == num:
            L += 1
        else:
            more -= 1
            swap(arr, L, more)
    return [less + 1, more - 1] # 等于部分的起止下标

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
    res = partition(test, 0, len(test) - 1, 4)
    print(test)
    print(res)