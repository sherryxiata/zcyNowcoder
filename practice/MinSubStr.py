#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/13 15:22
# @Author  : wenlei

'''
【题目】

　　给定字符串str1和str2，求str1的子串中含有str2所有字符的最小子串长度。

【举例】

　　str1 = “aabcde”, str2 = “ca”。返回3.
　　str1 = “12345”, str2 = “344”。返回0.

【基本思路】

　　使用一个哈希表记录str2中每一个字符出现的次数。需要四个变量：left，right表示str1子串str1[left…right]的两边界下标，match表示在子串str1[left…right]中目前一共欠str2多少个字符。minlength记录整个遍历过程中出现的最小的子串长度。初始时，left = right = 0，match = len(str2)，minlength = 系统的最大值。
　　
　　遍历str1，先向右扩张right，当遇到str2中的字符是，将map中相应的值 -1，同时match也 -1；如果遇到的不是str2中的字符，将(str1[right]，-1)记录到map中。当match == 0时，说明str1[left…right]已经包含了str2中的所有字符，但是此时的子串长度还不是该子串的最小长度，例如，例1中开始出现两个a，但是第二个a到c的距离才是最小距离。所以接下来还有一个向右扩张left的过程。
　　
　　向右扩张left，如果map[str1[left]] < 0，说明此时如果把这个字符捡起来，str1[left…right]中也不会欠str2字符，所以捡起该字符。如果map[str1[left]] == 0，说明一旦捡起该字符，那么str1[left…right]必然会欠str2一个字符，所以此时left扩张终止，此时left到right的值便是一个最小子串。
　　
　　令match+1，map[str1[left]]＋1，从left的下一个位置开始，继续扩张right和left寻找下一个最小的子串。整个过程中使用minlength记录最小的子串长度。
'''

import sys

#最小包含子串的长度
#最小包含子串的长度
def minLength(str1, str2):
    if str1 == None or str2 == None or len(str1) < len(str2):
        return 0
    map = [0 for i in range(256)]
    for i in range(len(str2)):
        map[ord(str2[i])] += 1
    left = 0
    right = 0
    match = len(str2)
    minlength = sys.maxsize
    while right < len(str1):
        map[ord(str1[right])] -= 1
        if map[ord(str1[right])] >= 0:
            match -= 1
        if match == 0:
            while map[ord(str1[left])] < 0:
                map[ord(str1[left])] += 1
                left += 1
            minlength = min(minlength, right - left + 1)
            match += 1
            map[ord(str1[left])] += 1
            left += 1
        right += 1
    return minlength if minlength != sys.maxsize else 0

s1 = '12345'
s2 = '344'
print(minLength(s1, s2))