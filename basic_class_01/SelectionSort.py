#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 19:00
# @Author  : wenlei

'''
选择排序
'''

import random

def selectionSort(arr):
    if not arr or len(arr) < 2:
        return
    for i in range(len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            minIndex = j if arr[j] < arr[minIndex] else minIndex
        swap(arr, i, minIndex) # 不管怎样都会交换，这时候用异或抖机灵就可能出问题

def swap(arr,i,j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp
    #这里不能用异或！

#for test
def comparator(arr):
    arr.sort()

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize + 1) * random.random())
    for i in range(len(arr)):
        arr[i] = int((maxValue + 1)*random.random()) - int((maxValue)*random.random())
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
    if len(arr1) == 0 and len(arr2) == 0:
        return True
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
        selectionSort(arr1)
        comparator(arr2)

        if not isEqual(arr1,arr2):
            success = False
            print(arr1)
            print(arr2)
            break

    print('Nice!') if success else print('Fuck!')