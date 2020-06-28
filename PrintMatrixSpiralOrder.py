# -*- coding: utf-8 -*-
# @Time    : 2020/6/28 11:26
# @Author  : wenlei

'''
转圈打印矩阵
'''

def printMatixSpiralOrder(matrix):
    tr = 0
    tc = 0
    dr = len(matrix) - 1
    dc = len(matrix[0]) - 1
    while tr <= dr and tc <= dc:
        printEdge(matrix, tr, tc, dr, dc)
        tr += 1
        tc += 1
        dr -= 1
        dc -= 1

def printEdge(matrix, tr, tc, dr, dc):
    # 在同一行
    if tr == dr:
        for i in range(tc, dc + 1):
            print(matrix[tr][i])
    # 在同一列
    elif tc == dc:
        for j in range(tr, dr + 1):
            print(matrix[j][tc])
    else:
        curR = tr
        curC = tc
        while curC != dc:
            print(matrix[tr][curC])
            curC += 1
        while curR != dr:
            print(matrix[curR][dc])
            curR += 1
        while curC != tc:
            print(matrix[dr][curC])
            curC -= 1
        while curR != tr:
            print(matrix[curR][tr])
            curR -= 1

if __name__ == '__main__':
    m = [[1,2,3,4],[5,6,7,8]]
    printMatixSpiralOrder(m)



