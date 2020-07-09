#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 19:37
# @Author  : wenlei

'''
汉诺塔
'''

def hanoi(N, fro, to, help):
    if N == 1:
        print('move', 'from', fro, 'to', to)
    hanoi(N - 1, fro, help, to)
    hanoi(1, )