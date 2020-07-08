#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 16:04
# @Author  : wenlei

'''
最低字典序的字符串拼接方式
'''

import functools

def myComparator(s1, s2):
    '比较器'
    if (s1 + s2) < (s2 + s1):
        return -1
    elif (s1 + s2) > (s2 + s1):
        return 1
    else:
        return 0

def lowestString(strs):
    if not strs:
        return None
    sort_strs = sorted(strs, key = functools.cmp_to_key(myComparator))
    res = ''
    for i in sort_strs:
        res += i
    return res

if __name__ == '__main__':
    strs1 = ["jibw", "ji", "jp", "bw", "jibw"]
    print(lowestString(strs1))

    strs2 = ["ba", "b"]
    print(lowestString(strs2))
