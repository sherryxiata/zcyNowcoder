#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/26 20:46
# @Author  : wenlei

'''
经典随机快排
'''

import random

def quickSort(arr):
    if not arr or len(arr) < 2:
        return arr
    sortProcess(arr, 0, len(arr) - 1)

def sortProcess(arr, L, R):
    # 返回的等于部分下标必须是有效值
    if L < R:
        # 随机生成一个[l, R]之间的位置
        i = random.randint(L, R)
        arr[i], arr[R] = arr[R], arr[i]
        # 返回等于部分下标
        p = partition(arr, L, R)
        # 左边继续划分
        sortProcess(arr, L, p - 1)
        # 右边继续划分
        sortProcess(arr, p + 1, R)

def partition(arr, L, R):
    i = L - 1
    while L < R:
        if arr[L] <= arr[R]:
            i += 1
            arr[L], arr[i] = arr[i], arr[L]
        L += 1
    arr[i + 1], arr[R] = arr[R], arr[i + 1]
    return i + 1

# for test
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
        quickSort(arr1)
        comparator(arr2)

        if not isEqual(arr1,arr2):
            success = False
            print(arr1)
            print(arr2)
            break

    print('Nice!') if success else print('Fuck!')