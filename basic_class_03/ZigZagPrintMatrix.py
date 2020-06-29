# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 11:23
# @Author  : wenlei

'''
之字形打印矩阵
'''

def zigZagPrintMatrix(matrix):
    aR, aC, bR, bC = 0, 0, 0, 0
    endR = len(matrix) - 1
    endC = len(matrix[0]) - 1
    formUp = False
    while aR != endR + 1:
        printLevel(matrix, aR, aC, bR, bC, formUp)
        aR = aR + 1 if aC == endC else aR
        aC = aC if aC == endC else aC + 1
        bC = bC + 1 if bR == endR else bC
        bR = bR if bR == endR else bR + 1
        formUp = not(formUp)

def printLevel(m, aR, aC, bR, bC, formUp):
    if formUp:
        while aR != bR + 1:
            print(m[aR][aC])
            aR += 1
            aC -= 1
    else:
        while bR != aR - 1:
            print(m[bR][bC])
            bR -= 1
            bC += 1

if __name__ == '__main__':
    m = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    zigZagPrintMatrix(m)
