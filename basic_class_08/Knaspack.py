#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 9:43
# @Author  : wenlei

'''
背包问题
'''

def bag1(c, p, bag):
    return process1(c, p, 0, 0, bag)

def process1(weight, value, i, w_sum, bag):
    if w_sum > bag:
        return 0
    if i == len(weight):
        return 0
    if w_sum + weight[i] <= bag:
        return max(process1(weight, value, i + 1, w_sum, bag), value[i] + process1(weight, value, i + 1, w_sum + weight[i], bag))
    return process1(weight, value, i + 1, w_sum, bag)

def bag2(w, v, bag):
    m = len(w) + 1
    n = bag + 1
    dp = [[0] * n for _ in range(m)]
    for i in range(m - 2, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = dp[i + 1][j]
            if w[i] + j <= bag:
                dp[i][j] = max(dp[i][j], v[i] + dp[i + 1][j + w[i]])
    return dp[0][0]

if __name__ == '__main__':
    weights = [3, 2, 4, 8, 5]
    values = [5, 6, 3, 19, 9]
    bag = 6
    print(bag1(weights, values, bag))
    print(bag2(weights, values, bag))