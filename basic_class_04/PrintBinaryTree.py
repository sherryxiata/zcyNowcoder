#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 15:41
# @Author  : wenlei

'''
直观打印一棵二叉树(福利）
'''

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def printTree(head):
    print('Binary Tree:')
    printInOrder(head, 0, 'H', 17)
    print('\n')

def printInOrder(head, height, to, length):
    if not head:
        return
    printInOrder(head.right, height + 1, 'v', length)
    val = to + str(head.value) + to
    lenM = len(val)
    lenL = (length - lenM) // 2
    lenR = length - lenM - lenL
    val = getSpace(lenL) + val + getSpace(lenR)
    print(getSpace(height * length) + val)
    printInOrder(head.left, height + 1, "^", length)


def getSpace(num):
    space = " "
    tmp = []
    for i in range(num):
        tmp.append(space)
    return ''.join(tmp)

if __name__ == '__main__':
    head = Node(1)
    head.left = Node(-222222222)
    head.right = Node(3)
    head.left.left = Node(-24567894456)
    head.right.left = Node(55555555)
    head.right.right = Node(66)
    head.left.left.right = Node(777)
    printTree(head)

    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.left.left.right = Node(7)
    printTree(head)

    head = Node(1)
    head.left = Node(1)
    head.right = Node(1)
    head.left.left = Node(1)
    head.right.left = Node(1)
    head.right.right = Node(1)
    head.left.left.right = Node(1)
    printTree(head)


