#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 12:42
# @Author  : wenlei

'''
小和问题
对数组中的每一个数，将左边比其小的数累加。
'''

import random

def smallSum(arr):
    if not arr or len(arr) < 2:
        return 0
    return mergeSort(arr, 0, len(arr)-1)

def mergeSort(arr,l,r):
    if l == r:
        return 0
    mid = l + ((r-l) >> 1)
    return mergeSort(arr, l, mid) + mergeSort(arr, mid+1, r) + merge(arr, l, mid, r)

def merge(arr, l, m, r):
    i = 0
    p1 = l
    p2 = m + 1
    res = 0
    help = [None] * (r - l + 1)

    while p1 <= m and p2 <= r:
        if arr[p1] < arr[p2]:
            help[i] = arr[p1]
            res += arr[p1] * (r - p2 + 1)
            p1 += 1
        else:
            help[i] = arr[p2]
            p2 += 1
        i += 1
    while p1 <= m:
        help[i] = arr[p1]
        p1 += 1
        i += 1

    while p2 <= r:
        help[i] = arr[p2]
        p2 += 1
        i += 1

    for k in range(len(help)):
        arr[l + k] = help[k]

    return res

#for test
def comparator(arr):
    if len(arr) < 2:
        return 0
    res = 0
    for i in range(1,len(arr)):
        for j in range(0,i):
            if arr[j] < arr[i]:
                res += arr[j]
    return res

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize+1) * random.random())
    for i in range(len(arr)):
        arr[i] = int((maxValue+1) * random.random()) - int((maxValue) * random.random()) #有正有负
    return arr

def copyArray(arr):
    if len(arr) == 0:
        return []
    arr1 = [None] * len(arr) #必须要事先声明一个空数组，不然会始终和arr一模一样！！！
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
        res1 = smallSum(arr1)
        res2 = comparator(arr2)
        if res1 != res2:
            success = False
            print('result:',res1,'arr:',arr1)
            print('result:',res2,'arr:',arr2)
            break

    if success:
        print('Nice!')
    else:
        print('Fuck!')