#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 17:29
# @Author  : wenlei

'''
分解质因数
'''

def factor(n):
    res = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                res.append(i)
                n //= i
                break
    return res

if __name__ == '__main__':
    n = int(input())
    print(factor(n))