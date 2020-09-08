#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def subSort(arr):
    start, end = 0, 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            start = i
            break
    ma = arr[start + 1]
    for j in range(start + 1, len(arr)):
        ma = max(ma, arr[j])

    for i in range(len(arr) - 1, start, -1):
        if arr[i] < arr[i - 1]:
            end = i + 1
            break
    if start == end: return [-1, -1]
    return [start, end]


# ******************************结束写代码******************************


_arr_cnt = 0
_arr_cnt = int(input())
_arr_i = 0
_arr = []
while _arr_i < _arr_cnt:
    _arr_item = int(input())
    _arr.append(_arr_item)
    _arr_i += 1

res = subSort(_arr)

for res_cur in res:
    print(str(res_cur) + "\n")