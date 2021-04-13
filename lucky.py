#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/18 11:23
# @Author  : wenlei

# 队列和栈（collections包中的deque双向队列，性能最好）
import collections

deque = collections.deque() # 创建双向队列/栈

deque.append(x) # 插入元素到队尾（队列）

deque.appendleft(x) # 插入元素到队头（栈）

# deque.pop() # 弹出队尾元素

deque.popleft() # 从队头弹出元素（√）

deque[0] # 队头/栈顶元素

len(deque) # 队列/栈大小

# 栈
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

# 队列
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

# 队列（queue包中的Queue）
import queue

q = queue.Queue() # 创建队列

q.put(1) # 插入元素

q.get() # 弹出元素

q.qsize() # 队列大小

q.empty() # 判断队列是否为空

# 判断队列是否为空

# 小根堆（python默认为小根堆）
import heapq

heap = [] # 初始化一个空堆

heapq.heapify(heap) # 将某个数组初始化为小根堆

heapq.heappush(heap, x) # 插入元素

heapq.heappop(heap) # 弹出堆顶元素（最小值）

heap[0] # 获得堆顶元素

len(heap) # 堆的大小

not heap # 堆为空

# 大根堆（需要取反放入小根堆）
import heapq

heap = [] # 初始化一个空堆

heapq.heapify(heap) # 将某个数组初始化为小根堆，此时heap中的元素应该取反

heapq.heappush(heap, - x) # 插入元素

- heapq.heappop(heap) # 弹出堆顶元素（最大值）

- heap[0] # 获得堆顶元素

len(heap) # 堆的大小

not heap # 堆为空

# 比较器1
import functools

def myComparator(s1, s2):
    if (s1 + s2) < (s2 + s1):
        return -1 # s1比较小
    elif (s1 + s2) > (s2 + s1):
        return 1 # s1比较大
    else:
        return 0

def lowestString(strs):
    sort_strs = sorted(strs, key = functools.cmp_to_key(myComparator))

# 比较器2
students_tuples = [('join', 'a', 15), ('kane', 'b', 20), ('pole', 'c', 30)]
sorted(students_tuples, key = lambda student: student[2])
print(students_tuples)


# 交换
def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def swap(arr, i, j):
    arr[i] = arr[i] ^ arr[j]
    arr[j] = arr[i] ^ arr[j]
    arr[i] = arr[i] ^ arr[j]

a, b = b, a

# 读文件操作
f = open('./practice/article.txt')

data1 = f.read() # 一次性读出整个文件

while True:
    data2 = f.read(10) # 每次读长度为10的字符串
    if not data2: break

# 每次读一行
for line in f.readlines():
    print(line)

# 将文件作为一个迭代器读取
with open('./practice/article.txt') as f:
    for line in f:
        print(line)

# 遍历dict
dic = {'a': 1, 'b': 2, 'c': 3}

dic.keys()
dic.values()
dic.pop('b')

for k, v in dic.items():
    print(k, v)
