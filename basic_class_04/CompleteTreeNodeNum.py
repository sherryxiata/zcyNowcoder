#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 17:10
# @Author  : wenlei

'''
求完全二叉树节点个数
'''

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def countCBTnum(head):
    if not head:
        return 0
    return bs(head, 1, mostLeftLevel(head, 1))

def bs(head, level, h):
    '返回当前节点位置的个数'
    if level == h:
        return 1
    if mostLeftLevel(head.right, level + 1) == h:
        return 2 ** (h - level) + bs(head.right, level + 1, h)
    else:
        return 2 ** (h - level - 1) + bs(head.left, level + 1, h)

def mostLeftLevel(head, level):
    '计算左边界高度'
    while head:
        level += 1
        head = head.left
    return level - 1

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)

    print(countCBTnum(head))