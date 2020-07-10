#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 9:22
# @Author  : wenlei

'''
打印全排列（重复/不重复）
'''

# 有重复
def printAllPermutations1(str):
    arr = list(str)
    process1(arr, 0)

def process1(arr, i):
    if i == len(arr):
        print(''.join(arr))
        return
    for j in range(i, len(arr)):
        swap(arr, i, j)
        process1(arr, i + 1)

def printAllPermutations2(str):
    arr = list(str)
    process2(arr, 0)

def process2(arr, i):
    if i == len(arr):
        print(''.join(arr))
        return
    hashSet = set()
    for j in range(i, len(arr)):
        if not (arr[j] in hashSet) :
            hashSet.add(arr[j])
            swap(arr, i, j)
            process2(arr, i + 1)


def swap(arr, i, j):
     tmp = arr[i]
     arr[i] = arr[j]
     arr[j] = tmp

if __name__ == '__main__':
    test1= 'abc'
    printAllPermutations1(test1)
    print('========================')
    printAllPermutations2(test1)
    print('========================')

    test2= 'acc'
    printAllPermutations1(test2)
    print('========================')
    printAllPermutations2(test2)
    print('========================')