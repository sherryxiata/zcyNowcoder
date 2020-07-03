#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 21:12
# @Author  : wenlei

'''
二叉树的序列化和反序列化
'''

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

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

# 1. 先序序列化
def serialByPre(head):
    if not head:
        return '#_'
    res = str(head.value) + '_'
    res += serialByPre(head.left)
    res += serialByPre(head.right)
    return res

def reconByPreString(str):
    values = str.split('_')
    queue = Queue()
    for i in values:
        queue.push(i)
    return reconByPreOrder(queue)

def reconByPreOrder(queue):
    value = queue.pop()
    if value == '#':
        return None
    head = Node(value)
    head.left = reconByPreOrder()