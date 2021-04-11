#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 13:46
# @Author  : wenlei

'''
逆序对问题
在一个数组中，如果左边的数大于右边的数，则这两个数构成一个逆序对；打印出所有逆序对
'''

import random

def inversionPair(arr):
    if not arr or len(arr) < 2:
        return []
    return mergeSort(arr, 0, len(arr) - 1)

def mergeSort(arr, l, r):
    if l == r:
        return []
    mid = l + (r - l) # 2
    return mergeSort(arr, l, mid) + mergeSort(arr, mid + 1, r) + merge(arr, l, mid, r)

def merge(arr, l, m, r):
    help = [None] * (r - l + 1)
    i = 0
    p1 = l
    p2 = m + 1
    res = []
    while p1 <= m and p2 <= r:
        if arr[p1] > arr[p2]:
            help[i] = arr[p2]
            for j in range(p1, m + 1):
                res.append([arr[j], arr[p2]])
            p2 += 1
        else:
            help[i] = arr[p1]
            p1 += 1
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
        return []
    res = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                res.append([arr[i],arr[j]])
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

def isEqual(arr1,arr2):
    if len(arr1) != len(arr2):
        return False
    arr1.sort()
    arr2.sort() #方便比较
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True

if __name__ == '__main__':
    testTime = 50000
    maxSize = 100
    maxValue = 100
    success = True

    for i in range(testTime):
        arr1 = generateRandomArray(maxSize,maxValue)
        arr2 = copyArray(arr1)
        res1 = inversionPair(arr1)
        res2 = comparator(arr2)
        if not isEqual(res1,res2):
            success = False
            print('result:',res1,'arr:',arr1)
            print('result:',res2,'arr:',arr2)
            break

    if success:
        print('Nice!')
    else:
        print('Fuck!')