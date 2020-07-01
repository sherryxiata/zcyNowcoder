#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 19:36
# @Author  : wenlei

'''归并排序
'''

import random

def mergeSort(arr):
    if not arr or len(arr) < 2:
        return
    sortProcess(arr, 0, len(arr) - 1)

def sortProcess(arr, L, R):
    if L == R:
        return
    mid = L + (R - L) # 2
    sortProcess(arr, L, mid)
    sortProcess(arr, mid + 1, R)
    merge(arr, L, mid, R)

def merge(arr, L, mid, R):
    help = [None] * (R - L + 1)
    i = 0
    p1 = L
    p2 = mid + 1
    while p1 <= mid and p2 <= R:
        if arr[p1] <= arr[p2]:
            help[i] = arr[p1]
            p1 += 1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1
    while p1 <= mid:
        help[i] = arr[p1]
        p1 += 1
        i += 1
    while p2 <= R:
        help[i] = arr[p2]
        p2 += 1
        i += 1
    for i in range(len(help)):
        arr[L + i] = help[i]

#for test
def comparator(arr):
    arr.sort() #直接修改原列表

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize + 1) * random.random())
    for i in range(len(arr)):
        arr[i] = int((maxValue + 1) * random.random()) - int((maxValue) * random.random()) # 有正有负
    return arr

def isEqual(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

def copyArray(arr):
    if len(arr) == 0:
        return []
    arr1 = [None] * len(arr) # 必须要事先声明一个空数组，不然会始终和arr一模一样！！！
    for i in range(len(arr)):
        arr1[i] = arr[i]
    return arr1

if __name__ == '__main__':
    testTime = 50000
    maxSize = 100
    maxValue = 100
    success = True

    for i in range(testTime):
        arr1 = generateRandomArray(maxSize,maxValue)
        arr2 = copyArray(arr1)
        mergeSort(arr1)
        comparator(arr2)
        if not isEqual(arr1,arr2):
            success = False
            print(arr1)
            print(arr2)
            break

    if success:
        print('Nice!')
    else:
        print('Fuck!')

