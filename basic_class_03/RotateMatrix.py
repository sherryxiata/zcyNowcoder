# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 12:46
# @Author  : wenlei

'''
顺时针旋转矩阵90度
'''

def rotateMatrix(matrix):
    tr = 0
    tc = 0
    dr = len(matrix) - 1
    dc = len(matrix[0]) - 1
    while tr < dr:
        rotateEdge(matrix, tr, tc, dr, dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1

def rotateEdge(matrix, tr, tc, dr, dc):
    times = dc - tc
    for i in range(times):
        tmp = matrix[tr][tc + i]
        matrix[tr][tc + i] = matrix[dr - i][tc]
        matrix[dr - i][tc] = matrix[dr][dc - i]
        matrix[dr][dc - i] = matrix[tr + i][dc]
        matrix[tr + i][dc] = tmp

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])

if __name__ == '__main__':
    m = [[1,2,3],[4,5,6],[7,8,9]]
    rotateMatrix(m)
    printMatrix(m)
