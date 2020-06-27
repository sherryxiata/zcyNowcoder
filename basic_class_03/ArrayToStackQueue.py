#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 20:26
# @Author  : wenlei

'''
用一个数组实现固定大小的队列和栈
'''

class ArrayStack():
    def __init__(self, init_size):
        if init_size < 0:
            raise Exception('stack size less than 0')
        self.arr = [None] * init_size
        self.index = 0 # 新数应存放的位置

    def push(self, num):
        if self.index == len(self.arr):
            raise Exception('stack full')
        self.arr[self.index] = num
        self.index += 1

    def pop(self):
        if self.index == 0:
            raise Exception('stack empty')
        self.index -= 1
        return self.arr[self.index]

    # 获取栈顶元素
    def peak(self):
        if self.index == 0:
            return None
        return self.arr[self.index - 1]

class ArrayQueue():
    def __init__(self, init_size):
        if init_size < 0:
            raise Exception('queue size less than 0')
        self.arr = [None] * init_size
        self.end = 0
        self.start = 0
        self.size = 0

    def push(self, num):
        self.size += 1
        if self.size > len(self.arr):
            raise Exception('stack full')
        self.arr[self.end] = num
        self.end = 0 if self.end == len(self.arr) - 1 else self.end + 1

    def pop(self):
        if self.size == 0:
            raise Exception('stack empty')
        self.size -= 1
        tmp = self.start
        self.start = 0 if self.start == len(self.arr) - 1 else self.start + 1
        return self.arr[tmp]

    def peak(self):
        if self.size == 0:
            return None
        return self.arr[self.start]


if __name__ == '__main__':
    stack = ArrayQueue(3)
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    stack.push(3)
    print(stack.pop())
    stack.push(4)
    stack.push(5)
    print(stack.peak())



