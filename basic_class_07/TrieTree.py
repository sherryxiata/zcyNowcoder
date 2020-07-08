#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 14:29
# @Author  : wenlei

'''
前缀树结构
'''

class TrieNode():
    def __init__(self):
        self.path = 0 # 经过此节点的次数
        self.end = 0 # 以此节点为结尾的次数
        self.next = [None] * 26 # 到下一节点的路径 为None代表没有到该字符的路径

class TrieTree():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        '插入一个字符串'
        if not word:
            return
        node = self.root
        arr = list(word)
        for str in arr:
            index = ord(str) - ord('a')# 转化为ascii码
            if not node.next[index]:
                node.next[index] = TrieNode()
            node = node.next[index]
            node.path += 1
        node.end += 1

    def search(self, word):
        '返回一个字符串的出现次数'
        if not word:
            return 0
        node = self.root
        arr = list(word)
        for str in arr:
            index = ord(str) - ord('a')  # 转化为ascii码
            if not node.next[index]:
                return 0
            node = node.next[index]
        return node.end

    def delete(self, word):
        '删除一个字符串'
        if self.search(word):
            node = self.root
            arr = list(word)
            for str in arr:
                index = ord(str) - ord('a')  # 转化为ascii码
                node.next[index].path -= 1
                if node.next[index].path < 0:
                    node.next[index] = None
                    return
                node = node.next[index]
            node.end -= 1

    def prefixNumber(self, pre):
        '返回pre作为前缀的次数'
        if not pre:
            return 0
        node = self.root
        arr = list(pre)
        for str in arr:
            index = ord(str) - ord('a')  # 转化为ascii码
            if not node.next[index]:
                return 0
            node = node.next[index]

        return node.path

if __name__ == '__main__':
    trie = TrieTree()
    print(trie.search("zuo"))
    trie.insert("zuo")
    print(trie.search("zuo"))
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.insert("zuo")
    trie.insert("zuo")
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.insert("zuoa")
    trie.insert("zuoac")
    trie.insert("zuoab")
    trie.insert("zuoad")
    trie.delete("zuoa")
    print(trie.search("zuoa"))
    print(trie.prefixNumber("zuo"))