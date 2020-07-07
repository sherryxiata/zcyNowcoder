#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 9:56
# @Author  : wenlei

'''
RandomPool结构
'''

import random

class RandomPool():
    def __init__(self):
        self.keyIndexMap = []
        self.indexKeyMap = []
        self.size = 0

    def insert(self, key):
        if not self.keyIndexMap.__contains__(key):
            self.keyIndexMap[key] = self.size
            self.indexKeyMap[self.size] = key
            self.size += 1

    def getRandom(self):
        if self.size == 0:
            return None
        rand = int(random.random() * self.size)
        return self.indexKeyMap.get(rand)

    def delete(self, key):
        if self.keyIndexMap.__contains__(key):
            deleteIndex = self.keyIndexMap.get(key)
            self.size -= 1
            lastIndex = self.size
            lastKey = self.indexKeyMap.get(lastIndex)
            self.keyIndexMap[lastKey] = deleteIndex
            self.indexKeyMap[deleteIndex] = lastKey
            self.keyIndexMap.pop(key)
            self.indexKeyMap.pop(lastIndex)

if __name__ == '__main__':
    pool = RandomPool()
    pool.insert("zuo")
    pool.insert("cheng")
    pool.insert("yun")
    print(pool.getRandom())
    print(pool.getRandom())
    print(pool.getRandom())
    print(pool.getRandom())
    print(pool.getRandom())
    print('--------------------------')
    pool.delete('zuo')
    print(pool.getRandom())
    print(pool.getRandom())
    print(pool.getRandom())
