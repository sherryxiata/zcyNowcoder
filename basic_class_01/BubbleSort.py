#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 14:55
# @Author  : wenlei

'''
冒泡排序
'''

import random

def bubbleSort(arr):
    if not arr or len(arr) < 2:
        return
    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i] #交换数组中的两个数

# 优化1：对于[5, 1, 2, 3, 4]，第一次排序就可以排好：用一个标志位，如果一次遍历下来没有交换过元素，则表示已经排好序。
def bubbleSort1(arr):
    if not arr or len(arr) < 2:
        return
    for end in range(len(arr) - 1, 0, -1):
        flag = True
        for i in range(end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = False
        if flag: break # 不用再进行下一轮排序了

# 优化2：对于[4,2,1,3,5,6,7]，后半部分已经有序：记录下最后一次交换的位置，下一次比较到这里就可以
def bubbleSort2(arr):
    if not arr or len(arr) < 2:
        return
    k = len(arr) - 1
    pos = 0
    for i in range(len(arr) - 1):
        flag = True
        for j in range(k):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                pos = j + 1
                flag = False
        k = pos
        if flag: break # 不用再进行下一轮排序了

# 优化3：对于[6, 1, 2, 3, 4, 5, 0]，最大值和最小值分别在左右两边的情况：
# 从左到右排完序以后，立即从右到左排序
def bubbleSort3(arr):
    if not arr or len(arr) < 2:
        return
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = False
        if not flag:
            flag = True
            for j in range(len(arr) - 2 - i, 0, -1):
                if arr[j - 1] > arr[j]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    flag = False
        if flag: break

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
        bubbleSort2(arr1)
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




