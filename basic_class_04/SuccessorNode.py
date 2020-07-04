#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 16:46
# @Author  : wenlei

'''
找二叉树节点的后续节点
'''


class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        self.parent = None

def getSuccessorNode(node):
    if not node:
        return node
    if node.right:
        return getMostLeft(node.right) # 找到右子树的最左节点
    else:
        parent = node.parent
        while parent and parent.left != node:
            node = parent
            parent = node.parent
    return parent

def getMostLeft(node):
    while node.left:
        node = node.left
    return node

def getProceedNode(node):
    if not node:
        return node
    if node.left:
        return getMostRight(node.left)
    else:
        parent = node.parent
        while parent and parent.right != node:
            node = parent
            parent = node.parent
        return parent

def getMostRight(node):
    while node.right:
        node = node.right
    return node

if __name__ == '__main__':
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 后续节点
    test = head.left.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left.left.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.left.right.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right.left.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right.left
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right
    print(test.value, " next: ", getSuccessorNode(test).value)
    test = head.right.right #  10's next is None
    print(test.value, " next: ", getSuccessorNode(test))

    # 前驱节点
    test = head.left.left  #  1's last is None
    print(test.value, " last: ", getProceedNode(test))
    test = head.left.left.right
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.left
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.left.right
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.left.right.right
    print(test.value, " last: ", getProceedNode(test).value)
    test = head
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.right.left.left
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.right.left
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.right
    print(test.value, " last: ", getProceedNode(test).value)
    test = head.right.right
    print(test.value, " last: ", getProceedNode(test).value)