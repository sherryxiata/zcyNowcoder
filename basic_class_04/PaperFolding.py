#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 14:04
# @Author  : wenlei

'''
折纸问题
'''

def printAllFolds(N):
    printProcess(1, N, True) # 第一层，共N层，is fro

def printProcess(i, N, isfro):
    if i > N:
        return
    printProcess(i + 1, N, True)
    print('fro', end = ',') if isfro == True else  print('up', end = ',')
    printProcess(i + 1, N, False)

if __name__ == '__main__':
    N = 4
    printAllFolds(4)
