#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 19:48
# @Author  : wenlei

'''
在排好序的数组里找某个数
'''

def findNumInSortedMatrix(matrix, num):
    row = len(matrix) - 1
    col = 0
    while row > -1 and col < len(matrix[0]):
        if num == matrix[row][col]:
            return True
        elif num > matrix[row][col]:
            col += 1
        else:
            row -= 1
    return False

if __name__ == '__main__':
    m = [[0, 1, 2, 3, 4, 5, 6], [10, 12, 13, 15, 16, 17, 18], [23, 24, 25, 26, 27, 28, 29], \
         [44, 45, 46, 47, 48, 49, 50], [65, 66, 67, 68, 69, 70, 71], [96, 97, 98, 99, 100, 111, 122], \
         [166, 176, 186, 187, 190, 195, 200], [233, 243, 321, 341, 356, 370, 380]]
    k = 187
    print(findNumInSortedMatrix(m, k))