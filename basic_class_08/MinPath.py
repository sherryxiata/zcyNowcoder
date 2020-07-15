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

def minPath2(m):
    if not m or not m[0]:
        return 0
    row = len(m)
    col = len(m[0])
    dp = [[None] * col for _ in range(row)]
    dp[row - 1][col - 1] = m[row - 1][col - 1]
    for i in range(row - 2, -1, -1):
        dp[i][col - 1] = m[i][col - 1] + dp[i + 1][col - 1]
    for j in range(col - 2, -1, -1):
        dp[row - 1][j] = m[row - 1][j] + dp[row - 1][j + 1]
    for i in range(row - 2, -1, -1):
        for j in range(col - 2, -1, -1):
            dp[i][j] = m[i][j] + min(dp[i + 1][j], dp[i][j + 1])
    return dp[0][0]


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
    print(minPath2(m))

    m = generateRandomMatrix(6,7)
    print(m)
    print(minPath1(m))
    print(minPath2(m))
