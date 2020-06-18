#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 19:36
# @Author  : wenlei

#归并排序

import random

def mergeSort(arr,l,r):
    if len(arr)<2:
        return;
    if l==r:
        return;
    mid = l + ((r-l)>>1) #防止溢出；位运算可以提高速度
    mergeSort(arr,l,mid)
    mergeSort(arr,mid+1,r)
    merge(arr,l,mid,r)

def merge(arr,l,m,r):
    help = [None] * (r-l+1) #定义一个辅助数组进行外排
    i = 0
    p1 = l
    p2 = m+1

    while p1<=m and p2<=r:
        if arr[p1] < arr[p2]:
            help[i] = arr[p1]
            p1+=1
        else:
            help[i] = arr[p2]
            p2+=1
        i+=1
    #以下两个while有且只有一个会实现
    while p1<=m:
        help[i] = arr[p1]
        i+=1
        p1+=1
    while p2<=r:
        help[i] = arr[p2]
        i+=1
        p2+=1

    for k in range(len(help)):
        arr[l+k] = help[k]

#for test
def comparator(arr):
    arr.sort() #直接修改原列表

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize+1) * random.random())
    for i in range(len(arr)):
        arr[i] = int((maxValue+1) * random.random()) - int((maxValue) * random.random()) #有正有负
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
        mergeSort(arr1,0,len(arr1)-1)
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

    # arr = generateRandomArray(maxSize,maxValue)
    # print(arr)
    # mergeSort(arr,0,len(arr)-1)
    # print(arr)


