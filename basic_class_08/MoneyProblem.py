#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 9:10
# @Author  : wenlei

'''
数组累加和
'''

def money1(arr, aim):
    return process1(arr, 0, 0, aim)

def process1(arr, i, sum, aim):
    if sum == aim:
        return True
    if i == len(arr):
        return False
    return process1(arr, i + 1, sum, aim) or process1(arr, i + 1, sum + arr[i], aim)

def money2(arr, aim):
    row = len(arr) + 1
    col = aim + 1
    dp = [[False] * col for _ in range(row)]
    for i in range(len(dp)):
        dp[i][aim] = True
    for i in range(row - 2, -1, -1):
        for j in range(col - 2, -1, -1):
            dp[i][j] = dp[i + 1][j]
            if j + arr[i] <= aim:
                dp[i][j] = dp[i][j] or dp[i + 1][j + arr[i]]
    return dp[0][0]

if __name__ == '__main__':
    arr = [1, 4, 8]
    aim = 10
    print(money1(arr, aim))
    print(money2(arr, aim))