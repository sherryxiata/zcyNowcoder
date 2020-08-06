#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 14:55
# @Author  : wenlei

'''冒泡排序
'''

import random

def bubbleSort(arr):
    if not arr or len(arr) < 2:
        return
    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1) #交换数组中的两个数

def swap(arr,a,b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

    #另一种写法
    # arr[a] = arr[a] ^ arr[b]
    # arr[b] = arr[a] ^ arr[b]
    # arr[a] = arr[a] ^ arr[b]

# for test
def comparator(arr):
    arr.sort() # sort()直接修改原列表 sorted(a) 不会修改原列表

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize + 1) * random.random()) # random.random()生成0-1范围的数
    for i in range(len(arr)):
        arr[i] = int((maxValue + 1) * random.random()) - int((maxValue) * random.random()) # 有正有负
    return arr

def isEqual(arr1,arr2):
    # 长度一样 + 每个位置上的数一样
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def copyArray(arr):
    if len(arr) == 0:
        return []
    arr1 = [None] * len(arr)
    for i in range(len(arr)):
        arr1[i] = arr[i]
    return arr1

if __name__ == '__main__':
    testTime = 50000
    maxSize = 100
    maxValue = 100
    success = True

    for i in range(testTime):
        arr1 = generateRandomArray(maxSize, maxValue)
        arr2 = copyArray(arr1)
        bubbleSort(arr1)
        comparator(arr2)
        if not isEqual(arr1,arr2):
            success = False
            print(arr1)
            print(arr2)
            break

    if success:
        print('Nice!')
    else:
        print('Oh No!')




