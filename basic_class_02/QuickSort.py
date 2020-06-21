#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 20:29
# @Author  : wenlei

'''利用荷兰国旗改进的快排
'''


import random

def quickSort(arr):
    if not arr or len(arr) < 2:
        return arr
    sortProcess(arr, 0, len(arr) - 1)

def sortProcess(arr, L, R):
    # 返回的等于部分下标必须是有效值
    if L < R:
        # 随机快排
        swap(arr, L + int(random.random() * (R - L + 1)), R)
        # 返回等于部分下标
        p = partition(arr, L, R)
        # 左边继续划分
        sortProcess(arr, L, p[0] - 1)
        # 右边部分继续划分
        sortProcess(arr, p[1] + 1, R)

def partition(arr, L, R):
    # 默认以最后一个数作为Num
    less = L - 1
    more = R
    while L < more:
        if arr[L] < arr[R]:
            less += 1
            swap(arr, L, less)
            L += 1
        elif arr[L] == arr[R]:
            L += 1
        else:
            more -= 1
            swap(arr, L, more)
    # 将最后一位数(num)移到中间来
    swap(arr, more, R)
    return [less + 1, more]

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

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
        quickSort(arr1)
        comparator(arr2)

        if not isEqual(arr1,arr2):
            success = False
            print(arr1)
            print(arr2)
            break

    print('Nice!') if success else print('Fuck!')