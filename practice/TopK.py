#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 11:22
# @Author  : wenlei

'''
用小根堆维护前k大的元素
'''

import heapq

def topk(arr, k):
    minHeap =  arr[0:k]
    heapq.heapify(minHeap)
    for num in arr[k::]:
        if num > minHeap[0]:
            minHeap[0] = num
            heapq.heapify(minHeap)
    return minHeap

arr = [1,5,4,6,2,4]
print(topk(arr, 3))
