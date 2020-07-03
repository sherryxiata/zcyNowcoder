#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 14:42
# @Author  : wenlei

'''
二叉树的前序、中序、后续遍历（递归/非递归）
'''

class Node():
    def __init__(self, x):
        self.val = x
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


def preOrderRecur(head):
    if not head:
        return []
    return [head.val] + preOrderRecur(head.left) + preOrderRecur(head.right)

def inOrderRecur(head):
    if not head:
        return []
    return inOrderRecur(head.left) + [head.val] + inOrderRecur(head.right)

def posOrderRecur(head):
    if not head:
        return []
    return posOrderRecur(head.left) + posOrderRecur(head.right) + [head.val]

def preOrderNoRecur(head):
    res = []
    if head:
        stack = Stack()
        stack.push(head)
        while not stack.isEmpty():
            head = stack.peek()
            res.append(stack.pop().val)
            if head.right:
                stack.push(head.right)
            if head.left:
                stack.push(head.left)
    return res

def inOrderNoRecur(head):
    res = []
    if head:
        stack = Stack()
        while not stack.isEmpty() or head:
            if head:
                stack.push(head)
                head = head.left
            else:
                head = stack.peek()
                res.append(stack.pop().val)
                head = head.right
    return res

def posOrderNoRecur(head):
    res = []
    if head:
        stack1 = Stack()
        stack2 = Stack()
        stack1.push(head)
        while not stack1.isEmpty():
            head = stack1.peek()
            stack2.push(stack1.pop().val)
            if head.left:
                stack1.push(head.left)
            if head.right:
                stack1.push(head.right)
        while not stack2.isEmpty():
            res.append(stack2.pop())
    return res

def posOrderNoRecur2(head):
    res = []
    if head:
        stack = Stack()
        stack.push(head)
        while not stack.isEmpty():
            c = stack.peek()
            if c.left and head != c.left and head != c.right:
                stack.push(c.left)
            elif c.right and head != c.right:
                stack.push(c.right)
            else:
                res.append(stack.pop().val)
                head = c
    return res

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(3)
    head.right = Node(8)
    head.left.left = Node(2)
    head.left.right = Node(4)
    head.left.left.left = Node(1)
    head.right.left = Node(7)
    head.right.left.left = Node(6)
    head.right.right = Node(10)
    head.right.right.left = Node(9)
    head.right.right.right = Node(11)

    # recursive
    print("==============recursive==============")
    print("pre-order: ", end = '') # [5, 3, 2, 1, 4, 8, 7, 6, 10, 9, 11]
    print(preOrderRecur(head))
    print("in-order: ", end = '') # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print(inOrderRecur(head))
    print("pos-order: ", end = '') # [1, 2, 4, 3, 6, 7, 9, 11, 10, 8, 5]
    print(posOrderRecur(head))

    # unrecursive
    print("============unrecursive=============")
    print(preOrderNoRecur(head))
    print(inOrderNoRecur(head))
    print(posOrderNoRecur(head))
    print(posOrderNoRecur2(head))
