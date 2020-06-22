#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/21 18:19
# @Author  : wenlei

'''堆排序
'''

import  random

def heapSort(arr):
    if not arr or len(arr) < 2:
        return arr
    # 将数组调整为大根堆
    for i in range(len(arr)):
        heapInsert(arr, i)
    heapSize = len(arr)
    # 交换堆顶和最后一个元素
    heapSize -= 1
    swap(arr, 0, heapSize)
    while heapSize > 0:
        #调整大根堆
        heapify(arr, 0, heapSize)
        heapSize -= 1
        swap(arr, 0, heapSize)

def heapInsert(arr, index):
    while arr[index] > arr[int((index - 1) / 2)]:
        swap(arr, index, int((index - 1) / 2))
        index = int((index - 1) / 2)

def heapify(arr, index, heapSize):
    # index位置的元素变小
    left = 2 * index + 1
    while left < heapSize:
        # 两个子孩子中的最大值
        largest = left + 1 if (left + 1) < heapSize and arr[left + 1] > arr[left] else left
        # 子孩子中的最大值和index中的最大值
        largest = largest if arr[largest] > arr[index] else index
        # index就是三者中的最大值
        if largest == index:
            break
        swap(arr, largest, index)
        index = largest
        left = index * 2 + 1

def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


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
        heapSort(arr1)
        comparator(arr2)

        if not isEqual(arr1,arr2):
            success = False
            print(arr1)
            print(arr2)
            break

    print('Nice!') if success else print('Fuck!')
