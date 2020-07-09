#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 9:25
# @Author  : wenlei

'''
最大收益问题
'''

from heapq import *

# 用于小根堆的节点
class minHeapNode():
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit

    def __lt__(self, other):
        return self.cost < other.cost

# 用于大根堆的节点
class maxHeapNode():
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit

    def __lt__(self, other):
        return self.profit > other.profit

def maxMoney(costs, profits, k, w):
    # costs 和 profits是两个数组
    nodes = []
    for i in range(len(profits)):
        nodes.append(minHeapNode(costs[i], profits[i]))
    minHeap = []
    maxHeap = []
    for i in range(len(nodes)):
        heappush(minHeap, nodes[i])
    for i in range(k):
        while minHeap and minHeap[0].cost <= w:
            tmp = heappop(minHeap)
            node = maxHeapNode(tmp.cost, tmp.profit)
            heappush(maxHeap, node)
        if not maxHeap:
            return w
        w += heappop(maxHeap).profit
    return w

if __name__ == '__main__':
    costs = [1, 5, 10, 7, 8]
    profits = [2, 2, 1, 3, 4]
    print(maxMoney(costs, profits, 10, 6))