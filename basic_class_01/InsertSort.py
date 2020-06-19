#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 17:23
# @Author  : wenlei

'''插入排序
'''

import random

def insertSort(arr):
    if len(arr) < 2:
        return
    for i in range(1, len(arr)):
        j = i - 1
        while j >= 0 and arr[j] > arr[j+1]:
            swap(arr, j, j+1)
            j = j - 1

def swap(arr,a,b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

#for test
def comparator(arr):
    arr.sort() #直接修改原列表

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize + 1) * random.random())
    for i in range(len(arr)):
        arr[i] = int((maxValue + 1) * random.random()) - int((maxValue) * random.random()) #有正有负
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
        insertSort(arr1)
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



