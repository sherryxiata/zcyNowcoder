#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 12:19
# @Author  : wenlei

'''
对于输入的每个字符串，查找其中的最大字母，在该字母后面插入字符串"(max)"。
样例输入
abcdefgfedcba
xxxxx
样例输出
abcdefg(max)fedcba
x(max)x(max)x(max)x(max)x(max)
'''

def maxC(str):
    if not str: return None
    ma = str[0]
    for c in str:
        if c > ma: ma = c
    arr = []
    for c in str:
        arr.append(c)
        if c == ma: arr.append('(max)')
    return ''.join(arr)

if __name__ == '__main__':
    str = input()
    print(maxC(str))