#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 14:56
# @Author  : wenlei

'''
递归逆序栈
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

def reverseStack(stack):
    if stack.isEmpty():
        return None
    i = getBottomElem(stack) # 取出栈底元素
    reverseStack(stack) # 递归取出栈底元素，最后缓存在i中的最上面的元素就是栈顶
    stack.push(i) # 将i中的缓存逐个放入stack

def getBottomElem(stack):
    res = stack.pop()
    if stack.isEmpty():
        return res # 弹出的就是栈底元素
    else:
        last = getBottomElem(stack)
        stack.push(res) # 将除栈底以外的元素重新放回栈
        return last

if __name__ == '__main__':
    test = Stack()
    test.push(1)
    test.push(2)
    test.push(3)
    test.push(4)
    test.push(5)
    reverseStack(test)
    while not test.isEmpty():
        print(test.pop())
