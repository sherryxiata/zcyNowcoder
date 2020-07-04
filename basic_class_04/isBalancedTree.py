#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 14:11
# @Author  : wenlei

'''
判断一棵二叉树是否是平衡二叉树
'''

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

# 解法1
class ReturnData():
    def __init__(self, isB, h):
        self.isB = isB
        self.h = h

def isBalance(head):
    return process(head).isB

def process(head):
    if not head:
        return ReturnData(True, 0)
    left = process(head.left)
    if not left.isB:
        return ReturnData(False, 0)
    right = process(head.right)
    if not right.isB:
        return ReturnData(False, 0)
    if abs(left.h - right.h) > 1:
        return ReturnData(False, 0)
    return ReturnData(True, max(left.h, right.h) + 1)

# 解法2
def isBalance(head):
    res = [None]
    res[0] = True
    getHeight(head, 1, res)
    return res[0]

def getHeight(head, level, res):
    if not head:
        return level
    lH = getHeight(head.left, level + 1, res)
    if not res[0]:
        return level
    rH = getHeight(head.right, level + 1, res)
    if not res[0]:
        return level
    if abs(lH - rH) > 1:
        res[0] = False
    return max(lH, rH)


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.right.left.left = Node(8)

    print(isBalance(head))
