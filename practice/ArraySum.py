#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 11:00
# @Author  : wenlei

'''
122333444455555............求前n个和
1. 第2004项是多少
数列一共有n(n + 1)/2个数，n = 62时，是1953；n = 63时，是2016，所以第2004项是63。
2. 前200个数的和
n= 19是190，n=20是210，所以第200个数是20，和为1*1 + 2*2 + 3*3 +...+19*19+20*(200-190)
'''

def nSum(n):
    if n == 0: return 0
    k, nn = 0, n
    while nn >= 0:
        k += 1
        nn -= k
    p, res = 0, 0
    for i in range(1, k):
        p += i
        res += i * i
    return res + (n - p) * k

print(nSum(11))


