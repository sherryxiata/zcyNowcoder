# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 10:27
# @Author  : wenlei

'''
实现一个栈，并且返回栈的最小值
'''

# 定义一个栈
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

class MyStack1():
    def __init__(self):
        self.dataStack = Stack()
        self.minStack = Stack()

    def push(self, num):
        self.dataStack.push(num)
        if self.minStack.isEmpty():
            self.minStack.push(num)
        elif num <= self.getMin():
            self.minStack.push(num)
        else:
            self.minStack.push(self.minStack.peek())

    def pop(self):
        if self.dataStack.isEmpty():
            raise Exception('The stack is empty')
        self.minStack.pop()
        return self.dataStack.pop()

    def getMin(self):
        if self.dataStack.isEmpty():
            raise Exception('The stack is empty')
        return self.minStack.peek()

if __name__ == '__main__':
    stack1 = MyStack1()
    stack1.push(3)
    print(stack1.getMin())
    stack1.push(4)
    print(stack1.getMin())
    stack1.push(1)
    print(stack1.getMin())
    print(stack1.pop())
    print(stack1.getMin())