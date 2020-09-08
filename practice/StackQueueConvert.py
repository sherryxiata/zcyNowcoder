#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 15:52
# @Author  : wenlei

# 用两个栈实现队列(list)
class QueueWith2Stack():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def top(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

# 用两个队列实现栈(list)
class StackWith2Queue():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        res = self.queue1.pop()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def top(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        res = self.queue1[0]
        self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def empty(self):
        return not self.queue1 and not self.queue2

import collections

# 用两个栈实现队列(deque)
class QueueWith2Stack1():
    def __init__(self):
        self.stack1 = collections.deque()
        self.stack2 = collections.deque()

    def push(self, x):
        self.stack1.appendleft(x)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.appendleft(self.stack1.popleft())
        return self.stack2.popleft()

    def top(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.appendleft(self.stack1.popleft())
        return self.stack2[0]

    def empty(self):
        return not self.stack1 and not self.stack2

# 用两个队列实现栈(deque)
class StackWith2Queue1():
    def __init__(self):
        self.queue1 = collections.deque()
        self.queue2 = collections.deque()

    def push(self, x):
        self.queue1.append(x)

    def pop(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        res = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def top(self):
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        res = self.queue1[0]
        self.queue2.append(self.queue1.popleft())
        self.queue1, self.queue2 = self.queue2, self.queue1
        return res

    def empty(self):
        return not self.queue1 and not self.queue2

