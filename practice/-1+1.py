#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 10:26
# @Author  : wenlei

'''
给[-1,1，.......,-1,1]，将-1放在左边，1放在右边
'''

def sort(arr):
    l, i = -1, 0
    while i < len(arr):
        if arr[i] == -1:
            l += 1
            arr[i], arr[l] = arr[l], arr[i]
        i += 1

if __name__ == '__main__':
    arr = [-1, 1, 1, 1, -1, 1, -1, -1, 1]
    print(sorted(arr))