#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 22:54
# @Author  : wenlei

'''
判断链表是否为回文结构
'''

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

class Node():
    def __init__(self, x):
        self.val = x
        self.next = None

# 空间复杂度O(N)
def isPalindrome1(head):
    stack = Stack()
    cur = head
    while cur:
        stack.push(cur.val)
        cur = cur.next
    while head:
        if head.val != stack.pop():
            return False
        head = head.next
    return True

# 空间复杂度O(N/2)
def isPalindrome2(head):
    if not head or not head.next:
         return True
    cur = head # 快指针
    right = head.next # 慢指针
    while cur.next and cur.next.next:
        right = right.next
        cur = cur.next.next
    stack = Stack()
    while right:
        stack.push(right.val)
        right = right.next
    while not stack.isEmpty():
        if head.val != stack.pop():
            return False
        head = head.next
    return True

# 空间复杂度O(1)
def isPalindrome3(head):
    if not head or not head.next:
        return True
    # 找到中间位置，并且如果N为偶数，取靠左的中间位置
    n1 = head # 慢指针
    n2 = head # 快指针
    while n2.next and n2.next.next:
        n1 = n1.next
        n2 = n2.next.next
    # 逆序右半部分
    n2 = n1.next # 右半部分的开始
    n1.next = None
    while n2:
        n3 = n2.next
        n2.next = n1
        # 向右移动
        n1 = n2
        n2 = n3
    # 首尾分别设置指针，进行比较
    n2 = head
    n3 = n1
    flag = True
    while n1 and n2:
        if n1.val != n2.val:
            flag = False
            break
        n1 = n1.next
        n2 = n2.next
    # 还原链表
    n1 = n3.next
    n3.next = None
    while n1:
        n2 = n1.next
        n1.next = n3
        n1 = n3
        n1 = n2
    return flag


if __name__ == '__main__':
    head = None # T
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) # T
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) # F
    head.next = Node(2)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) # T
    head.next = Node(1)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) # F
    head.next = Node(2)
    head.next.next = Node(3)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) # T
    head.next = Node(2)
    head.next.next = Node(1)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) #F
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(1)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) #T
    head.next = Node(2)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

    head = Node(1) #T
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    print(isPalindrome1(head))
    print(isPalindrome2(head))
    print(isPalindrome3(head))
    print('=========================')

