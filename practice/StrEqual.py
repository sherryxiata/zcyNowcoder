#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 15:35
# @Author  : wenlei

'''
两个字符串，不考虑大小写和空格的问题，判断俩字符串是否相同

测试用例：
1. 空字符串
2. 空格字符串
3. 全小写
4. 全大写
5. 大小写混合
6. 字母+空格：空格在开头/中间/结尾 多个空格
7. 长度相等/不相等
'''

def my_strip(s):
    res = ''
    for c in s:
        if c != ' ':
            res += c
    return res

def isEqual(s1, s2):
    s1_strip = my_strip(s1)
    s2_strip = my_strip(s2)
    print(s1_strip, s2_strip)
    if len(s1_strip) != len(s2_strip): return False
    for i in range(len(s1_strip)):
        if not (s1_strip[i] == s2_strip[i] or abs(ord(s1_strip[i]) - ord(s2_strip[i])) == 32): return False
    return True



if __name__ == '__main__':
    s1 = 'a A bb BB cc CCCc'
    s2 = 'Aa B          Bbb    CCCc  cc'
    print(isEqual(s1, s2))