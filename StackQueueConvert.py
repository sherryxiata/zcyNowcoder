# -*- coding: utf-8 -*-
# @Time    : 2020/6/25 11:44
# @Author  : wenlei

'''
用两个队列实现栈，用两个栈实现队列
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

class StackWith2Queue():
    def __init__(self):
        self.queue = Queue()
        self.help = Queue()

    def push(self, num):
        self.queue.push(num)

    def pop(self):
        if self.queue.isEmpty():
            raise Exception('The stack is empty')
        while self.queue.size() > 1:
            self.help.push(self.queue.pop())
        res = self.queue.pop()
        self.swap()
        return res

    def peek(self):
        if self.queue.isEmpty():
            raise Exception('The stack is empty')
        while self.queue.size() > 1:
            self.help.push(self.queue.pop())
        res = self.queue.peek()
        self.help.push(self.queue.pop())
        self.swap()
        return res

    def isEmpty(self):
        if not self.arr or len(self.arr) < 1:
            return True

    def swap(self):
        tmp = self.help
        self.help = self.queue
        self.queue = tmp

class QueueWith2Stack():
    def __init__(self):
        self.pushStack = Stack()
        self.popStack = Stack()

    def push(self, num):
        self.pushStack.push(num)

    def pop(self):
        if self.pushStack.isEmpty() and self.popStack.isEmpty():
            raise Exception('The queue is empty')
        if self.popStack.isEmpty():
            while not self.pushStack.isEmpty():
                self.popStack.push(self.pushStack.pop())
        return self.popStack.pop()

    def peek(self):
        if self.pushStack.isEmpty() and self.popStack.isEmpty():
            raise Exception('The queue is empty')
        if self.popStack.isEmpty():
            while not self.pushStack.isEmpty():
                self.popStack.push(self.pushStack.pop())
        return self.popStack.peek()

    def isEmpty(self):
        if not self.arr or len(self.arr) < 1:
            return True

    def swap(self):
        tmp = self.help
        self.help = self.queue
        self.queue = tmp

if __name__ == '__main__':
    # 栈
    # stack1 = StackWith2Queue()
    # stack1.push(1)
    # stack1.push(2)
    # print(stack1.pop())
    # stack1.push(3)
    # print(stack1.pop())
    # print(stack1.peek())
    # print(stack1.pop())
    # 队列
    queue1 = QueueWith2Stack()
    queue1.push(1)
    queue1.push(2)
    print(queue1.pop())
    queue1.push(3)
    print(queue1.pop())
    print(queue1.peek())
    print(queue1.pop())