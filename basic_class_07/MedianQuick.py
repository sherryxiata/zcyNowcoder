#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 11:05
# @Author  : wenlei

'''
数据流随时取中位数
'''

import heapq
import random

# 小根堆
class MinHeap():
    def __init__(self):
        self.heap = []

    def insert(self, node):
        if not node:
            return
        heapq.heappush(self.heap, node)

    def pop(self):
        return heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return not self.heap

# 大根堆
class MaxHeap():
    def __init__(self):
        self.heap = []

    def insert(self, node):
        heapq.heappush(self.heap, - node)

    def pop(self):
        return - heapq.heappop(self.heap)

    def peek(self):
        if not self.heap:
            return None
        return - self.heap[0]

    def size(self):
        return len(self.heap)

    def isEmpty(self):
        return not self.heap

class MedianHolder():
    def __init__(self):
        self.minHeap = MinHeap()
        self.maxHeap = MaxHeap()

    def __modifyHeapSize(self):
        minSize = self.minHeap.size()
        maxSize = self.maxHeap.size()
        if maxSize == minSize + 2:
            self.minHeap.insert(self.maxHeap.pop())
        if minSize == maxSize + 2:
            self.maxHeap.insert(self.minHeap.pop())

    def addNumber(self, num):
        if self.maxHeap.isEmpty():
            self.maxHeap.insert(num)
            return
        if num <= self.maxHeap.peek():
            self.maxHeap.insert(num)
        else:
            if self.minHeap.isEmpty():
                self.minHeap.insert(num)
                return
            if num < self.minHeap.peek():
                self.maxHeap.insert(num)
            else:
                self.minHeap.insert(num)
        self.__modifyHeapSize()

    def getMedian(self):
        minSize = self.minHeap.size()
        maxSize = self.maxHeap.size()
        if minSize + maxSize == 0:
            return None
        if (minSize + maxSize) % 2 == 0:
            return (self.minHeap.peek() + self.maxHeap.peek()) / 2
        else:
            return self.minHeap.peek() if minSize > maxSize else self.maxHeap.peek()

# for test
def generateRandomArray(maxSize, maxValue):
    arr = [None] * (int(maxSize* random.random()) + 1)
    for i in range(len(arr)):
        arr[i] = int(random.random() * maxValue)
    return arr

def comparator(arr):
    arr1 = [None] * len(arr)
    for i in range(len(arr)):
        arr1[i] = arr[i]
    arr1.sort()
    mid = (len(arr1) - 1) // 2
    if len(arr1) % 2 == 0:
        return (arr1[mid] + arr1[mid + 1]) / 2
    else:
        return arr1[mid]

if __name__ == '__main__':
    # arr = [0, 373, 838]
    # medianhold = MedianHolder()
    # for i in range(len(arr)):
    #     medianhold.addNumber(arr[i])
    # print(medianhold.getMedian())
    # print(comparator(arr))

    testTime = 200000
    maxSize = 5
    maxValue = 1000
    success = True

    for i in range(testTime):
        arr = generateRandomArray(maxSize, maxValue)
        medianHold = MedianHolder()
        for j in range(len(arr)):
            medianHold.addNumber(arr[j])
        if medianHold.getMedian() != comparator(arr):
            success = False
            print(arr)
            print(medianHold.getMedian())
            print(comparator(arr))
            break

    if success:
        print('Nice!')
    else:
        print('Oh No!')



