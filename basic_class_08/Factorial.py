#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 19:33
# @Author  : wenlei

'''
阶乘
'''

def factorial1(n):
    if n == 1:
        return 1
    return n * factorial1(n - 1)

def factorial2(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

if __name__ == '__main__':
    print(factorial1(5))
    print(factorial2(5))