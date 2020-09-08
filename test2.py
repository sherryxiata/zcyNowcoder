#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def findMin(arr):
    mi, mi2 = arr[0], arr[0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            mi = min(mi, arr[j])
            mi2 = max(mi2, mi)
    for num in range(mi2, mi):
        if num != mi:
            return num

# ******************************结束写代码******************************


_arr_rows = 0
_arr_cols = 0
_arr_rows = int(input())
_arr_cols = int(input())

_arr = []
for _arr_i in range(_arr_rows):
    _arr_temp = map(int, re.split(r'\s+', input().strip()))
    _arr.append(_arr_temp)

res = findMin(_arr)

print(str(res) + "\n")