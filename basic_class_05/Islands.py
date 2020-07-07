#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 17:06
# @Author  : wenlei

'''
岛问题
'''

def countIslands(m):
    if not m or len(m) == 0 or len(m[0]) == 0:
        return 0
    M = len(m)
    N = len(m[0])
    res = 0
    for i in range(M):
        for j in range(N):
            if m[i][j] == 1:
                res += 1
                infect(m, i, j, M, N)
    return res

def infect(m, i, j, M, N):
    if i < 0 or i >= M or j < 0 or j >= N or m[i][j] == 0 or m[i][j] == 2:
        return
    m[i][j] = 2
    infect(m, i + 1, j, M, N)
    infect(m, i - 1, j, M, N)
    infect(m, i, j + 1, M, N)
    infect(m, i, j - 1, M, N)

if __name__ == '__main__':
    m1 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 0, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(countIslands(m1))

    m2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 1, 1, 1, 1, 1, 0],
          [0, 1, 1, 1, 0, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 0, 1, 1, 0],
          [0, 0, 0, 0, 0, 1, 1, 0, 0],
          [0, 0, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(countIslands(m2))