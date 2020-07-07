#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 15:57
# @Author  : wenlei

'''
并查集结构
'''

# 并查集结构的节点，随便什么类型（int, string, float, list...）
class UnionFind():
    def __init__(self, nodes):
        self.fatherMap = [] # key: node value: node
        self.sizeMap = [] # key:node value: size 表示节点所在集合有多少元素
        self.__makeSets(nodes) # 输入数据集合

    def __makeSets(self, nodes):
        self.fatherMap.clear()
        self.sizeMap.clear()
        # 每个节点各自成为一个集合
        for node in nodes:
            self.fatherMap[node] = node
            self.sizeMap[node] = 1

    def __findHead(self, node):
        father = self.fatherMap.get(node)
        if father != node:
            father = self.__findHead(father)
        self.fatherMap[node] = father
        return father

    def isSameSet(self, a, b):
        return self.__findHead(a) == self.__findHead(b)

    def union(self, a, b):
        if not a or not b:
            return None
        aHead = self.__findHead(a)
        bHead = self.__findHead(b)
        if aHead != bHead:
            sizeOfa = self.sizeMap.get(a)
            sizeOfb = self.sizeMap.get(b)
            if sizeOfa > sizeOfb:
                self.fatherMap[b] = a
                self.sizeMap[b] = self.sizeMap[b] + self.sizeMap[a]
            else:
                self.fatherMap[a] = b
                self.sizeMap[a] = self.sizeMap[a] + self.sizeMap[b]

if __name__ == '__main__':
    set = UnionFind([1, 2, 3, 4, 5])
    print(set.isSameSet(1, 5))
    set.union(1, 3)
    print(set.isSameSet(1, 3))
    set.union(3, 2)
    print(set.isSameSet(1, 2))
    print(set.isSameSet(1, 5))
