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
#  中序序列化和反序列化：不能实现，因为根据中序反序列化二叉树的结果不唯一
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
    head = Node(int(value))
    head.left = reconByPreOrder(queue)
    head.right = reconByPreOrder(queue)
    return head

# 2.层次序列化
def serialByLevel(head):
    if not head:
        return '#_'
    queue = Queue()
    queue.push(head)
    res = str(head.value) + '_'
    while not queue.isEmpty():
        head = queue.pop()
        if head.left:
            queue.push(head.left)
            res += str(head.left.value) + '_'
        else:
            res += '#_'
        if head.right:
            queue.push(head.right)
            res += str(head.right.value) + '_'
        else:
            res += '#_'
    return res

def reconByLevelString(str):
    values = str.split('_')
    index = 0
    head = generateNodeByString(values[index])
    index += 1

    queue = Queue()

    if head:
        queue.push(head)

    while not queue.isEmpty():
        node = queue.pop()
        node.left = generateNodeByString(values[index])
        index += 1
        node.right = generateNodeByString(values[index])
        index += 1
        if node.left:
            queue.push(node.left)
        if node.right:
            queue.push(node.right)
    return head

def generateNodeByString(str):
    if str == '#':
        return None
    return Node(int(str))

# 直观打印二叉树
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
    head = None
    printTree(head)

    pre = serialByPre(head)
    print("serialize tree by pre-order: " + pre)
    head = reconByPreString(pre)
    print("reconstruct tree by pre-order, ")
    printTree(head)

    level = serialByLevel(head)
    print("serialize tree by level: " + level)
    head = reconByLevelString(level)
    print("reconstruct tree by level, ")
    printTree(head)

    print("====================================")

    head = Node(1)
    printTree(head)

    pre = serialByPre(head)
    print("serialize tree by pre-order: " + pre)
    head = reconByPreString(pre)
    print("reconstruct tree by pre-order, ")
    printTree(head)

    level = serialByLevel(head)
    print("serialize tree by level: " + level)
    head = reconByLevelString(level)
    print("reconstruct tree by level, ")
    printTree(head)

    print("====================================")

    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)
    printTree(head)

    pre = serialByPre(head)
    print("serialize tree by pre-order: " + pre)
    head = reconByPreString(pre)
    print("reconstruct tree by pre-order, ")
    printTree(head)

    level = serialByLevel(head)
    print("serialize tree by level: " + level)
    head = reconByLevelString(level)
    print("reconstruct tree by level, ")
    printTree(head)

    print("====================================")

    head = Node(100)
    head.left = Node(21)
    head.left.left = Node(37)
    head.right = Node(-42)
    head.right.left = Node(0)
    head.right.right = Node(666)
    printTree(head)

    pre = serialByPre(head)
    print("serialize tree by pre-order: " + pre)
    head = reconByPreString(pre)
    print("reconstruct tree by pre-order, ")
    printTree(head)

    level = serialByLevel(head)
    print("serialize tree by level: " + level)
    head = reconByLevelString(level)
    print("reconstruct tree by level, ")
    printTree(head)

    print("====================================")