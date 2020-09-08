#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 12:21
# @Author  : wenlei

'''
0-1背包问题
n个物品,最大容量为k,每个物品的重量和价值为w[i]和v[i]
思路：
对于0-1背包问题，最优解的子解也是最优解.
dp[i][j] 表示到第i个物品为止，当包的最大容量为k时的最大价值
1. i = 0 或 j = 0时，dp[i][j] = 0
2. w[i] > k: 不放入 dp[i][j] = dp[i - 1][j]
3. w[i] <= k: 可以放入 dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])

'''

# O(N*M) O(N*M)
def maxValue1(n, k, v, w):
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if w[i] <= j:
                dp[i][j] = max(dp[i - 1][j - w[i]] + v[i], dp[i - 1][j])
            else:
                # 超出最大容积
                dp[i][j]  = dp[i - 1][j]
    return dp[-1][-1]

# O(N*M) O(M)
def maxValue2(n, k, v, w):
    dp = [0] * (k + 1)
    for i in range(1, n + 1):
        for j in range(k, 0, -1):
            if w[i] <= j:
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[-1]