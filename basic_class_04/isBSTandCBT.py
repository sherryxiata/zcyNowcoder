#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 15:52
# @Author  : wenlei

'''
判断一棵二叉树是否是搜索二叉树
'''

class Node():
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

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

def isBST(head):
    min = -9999999999
    if head:
        stack = Stack()
        while not stack.isEmpty() or head:
            if head:
                stack.push(head)
                head = head.left
            else:
                head = stack.pop()
                if head.value < min:
                    return False
                else:
                    min = head.value
                head = head.right
        return True

# moriis遍历方法（暂时不用懂）
def isBSTMoriis(head):
    pass

def isCBT(head):
    if not head:
        return True
    queue = Queue()
    queue.push(head)
    leaf = False # 情况2是否开启
    while not queue.isEmpty():
        head = queue.pop()
        left = head.left
        right = head .right
        if (not left and right)  or (leaf and (left or right)):
            return False
        if left:
            queue.push(left)
        if right:
            queue.push(right)
        else:
            leaf = True
    return True

# for test
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
    head = Node(4)
    head.left = Node(2)
    head.right = Node(6)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.right.left = Node(5)

    printTree(head)
    print(isBST(head))
    print(isCBT(head))