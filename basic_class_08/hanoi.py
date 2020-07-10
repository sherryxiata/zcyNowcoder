#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 19:37
# @Author  : wenlei

'''
汉诺塔
'''

def hanoi(n):
    if n > 0:
        func(n, n, 'left', 'mid', 'right')

def func(rest, down, fro, to, help):
    'rest:挪动1 - N down：最下面的圆盘'
    if rest == 1:
        print('move', down, 'from', fro, 'to', to)
        return
    func(rest - 1, down - 1, fro, help, to)
    func(1, down, fro, to, help)
    func(rest - 1, down - 1, help, to, fro)

# 尝试的写法 6个函数 相互嵌套
def hanoi2(n):
    if n > 0:
        moveLeftToRight(n)

def moveLeftToRight(n):
    if n == 1:
        print('move 1 from left to right')
        return
    moveLeftToMid(n - 1)
    print('move', n, 'from left to right')
    moveMidToRight(n - 1)

def moveLeftToMid(n):
    if n == 1:
        print('move 1 from left to mid')
        return
    moveLeftToRight(n - 1)
    print('move', n, 'from left to mid')
    moveRightToMid(n - 1)

def moveMidToRight(n):
    if n == 1:
        print('move 1 from mid to right')
        return
    moveMidToLeft(n - 1)
    print('move', n, 'from mid to right')
    moveLeftToRight(n - 1)

def moveRightToMid(n):
    if n == 1:
        print('move 1 from right to mid')
        return
    moveRightToLeft(n - 1)
    print('move', n, 'from mid to right')
    moveLeftToMid(n - 1)

def moveMidToLeft(n):
    if n == 1:
        print('move 1 from mid to left')
        return
    moveMidToRight(n - 1)
    print('move', n, 'from mid to left')
    moveRightToLeft(n - 1)

def moveRightToLeft(n):
    if n == 1:
        print('move 1 from right to left')
        return
    moveRightToMid(n - 1)
    print('move', n, 'from right to left')
    moveMidToLeft(n - 1)

if __name__ == '__main__':
    n = 3
    hanoi2(n)