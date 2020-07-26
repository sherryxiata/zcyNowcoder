#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:54
# @Author  : wenlei

'''
荷兰国旗问题
小于的放在左边，等于的放在中间，大于的放在右边
'''

import random

def partition(arr, L, R, num):
    less = L - 1
    more = R + 1
    while L < more:
        if arr[L] < num:
            less += 1
            arr[L], arr[less] = arr[less], arr[L]
            L += 1
        elif arr[L] > num:
            more -= 1
            arr[L], arr[more] = arr[more], arr[L]
        else:
            L += 1
    return [less + 1, more - 1] # 等于部分的起止下标

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