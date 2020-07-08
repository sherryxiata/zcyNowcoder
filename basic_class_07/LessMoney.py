#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 19:51
# @Author  : wenlei

'''
金条分割
'''

from heapq import *

# 大根堆
class MaxHeap():
    def __init__(self):
        self.heap = []

    def heapInsert(self, node):
        heappush(self.heap, - node)

    def heapify(self):
        heapify(self.heap)

    def heapPop(self):
        return - heappop(self.heap)

    def heapPeek(self):
        if not self.heap:
            return None
        return - self.heap[0]

    def size(self):
        return len(self.heap)

def lessMoney(arr):
    heapify(arr)
    res = 0
    while len(arr) > 1:
        cur = heappop(arr) + heappop(arr)
        res += cur
        heappush(arr, cur)
    return res

if __name__ == '__main__':
    arr = [1, 2, 6, 4, 3, 7, 1, 8]
    # arr = [10, 20, 30]
    print(lessMoney(arr))

    print('===================================')

    arrForHeap = [3, 5, 2, 7, 0, 1, 6, 4]

    # heapq给定的小根堆
    minHeap = []
    for i in arrForHeap:
        heappush(minHeap, i)
    for i in range(len(minHeap)):
        print(heappop(minHeap))

    print('===================================')

    # 实现大根堆
    maxHeap = MaxHeap()
    for i in arrForHeap:
        maxHeap.heapInsert(i)
    while maxHeap.size() > 0:
        print(maxHeap.heapPop())

