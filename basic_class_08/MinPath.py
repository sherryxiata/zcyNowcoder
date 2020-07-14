#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 15:17
# @Author  : wenlei

'''
最小路径和
'''

import random

def minPath1(matrix):
    return process1(matrix, 0, 0)

def process1(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])
    if i == m - 1 and j == n - 1:
        return matrix[i][j]
    elif i == m - 1:
        return matrix[i][j] + process1(matrix, i, j + 1)
    elif j == n - 1:
        return matrix[i][j] + process1(matrix, i + 1, j)
    else:
        return matrix[i][j] + min(process1(matrix, i, j + 1), process1(matrix, i + 1, j))

# for test
def generateRandomMatrix(rowSize, colSize):
    if rowSize < 0 or colSize < 0:
        return None
    result = [[None] * colSize for _ in range(rowSize)]
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = int(random.random() * 10)
    return result

if __name__ == '__main__':
    m = [[1, 3, 5, 9],[8, 1, 3, 4], [5, 0, 6, 1], [8, 8, 4, 0]]
    print(minPath1(m))

    m = generateRandomMatrix(2,3)
    print(m)
    print(minPath1(m))
