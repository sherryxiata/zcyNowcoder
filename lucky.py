#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 11:23
# @Author  : wenlei

# 栈
class Stack():
    def __init__(self):
        self.arr = []

    def push(self, num):
       self.arr.append(num)

    def pop(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return (self.arr.pop())

    def peek(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return (self.arr[-1])

    def isEmpty(self):
        if not self.arr or len(self.arr) < 1:
            return True

# 队列
class Queue():
    def __init__(self):
        self.arr = []

    def push(self, num):
        self.arr.append(num)

    def pop(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return (self.arr.pop(0))

    def peek(self):
        if self.isEmpty():
            raise Exception('The stack is empty')
        return (self.arr[0])

    def isEmpty(self):
        if not self.arr or len(self.arr) < 1:
            return True

    def size(self):
        return len(self.arr)

# 小根堆（python默认为小根堆）
import heapq

heap = [] # 初始化一个空堆

heapq.heapify(heap) # 将某个数组初始化为小根堆

heapq.heappush(heap, x) # 插入元素

heapq.heappop(heap) # 弹出堆顶元素（最小值）

heap[0] # 获得堆顶元素

len(heap) # 堆的大小

not heap # 堆为空

# 大根堆（需要取反放入小根堆）
import heapq

heap = [] # 初始化一个空堆

heapq.heapify(heap) # 将某个数组初始化为小根堆，此时heap中的元素应该取反

heapq.heappush(heap, - x) # 插入元素

- heapq.heappop(heap) # 弹出堆顶元素（最大值）

- heap[0] # 获得堆顶元素

len(heap) # 堆的大小

not heap # 堆为空
