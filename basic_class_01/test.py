#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 17:21
# @Author  : wenlei

def str_sort(s):
    if not s or len(s) < 2:
        return s
    arr = list(s)
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j + 1 ]:
            swap(arr, j, j + 1)
            j -= 1
    return str(arr)

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

if __name__ == '__main__':
    s = 'dbAa'
    print(str_sort(s))


