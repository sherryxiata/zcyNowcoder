#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 16:24
# @Author  : wenlei

'''
假设你有一个用1001个整数组成的数组，这些整数是任意排列的，但是你知道所有的整数都在1到1000(包括1000)之间。
此外，除一个数字出现两次外，其他所有数字只出现一次。
假设你只能对这个数组做一次处理，用一种算法找出重复的那个数字。
如果你在运算中使用了辅助的存储方式，那么你能找到不用这种方式的算法吗?
'''

import random
from collections import Counter

def findTwice(arr):
    # 解法1
    # return sum(arr) - (1 + 1000) * 1000 // 2
    # 解法2
    hashmap = Counter(arr)
    for k in hashmap.keys():
        if hashmap[k] == 2:
            return k

if __name__ == '__main__':
    arr = [x for x in range(1, 1002)]
    # print(arr)
    arr[1000] = 11
    random.shuffle(arr)
    print(findTwice(arr))