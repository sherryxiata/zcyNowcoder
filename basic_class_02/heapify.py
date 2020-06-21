#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 18:19
# @Author  : wenlei

def heapify(arr):
    # 生成大根堆
    for i in range(len(arr)):
        heapInsert(arr, i)

def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

if __name__ == '__main__':
    arr = [2,1,3,6,0,4]
    heapify(arr)
    print(arr)