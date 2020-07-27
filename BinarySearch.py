#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 9:49
# @Author  : wenlei

'''
二分查找：
1. 一个数 返回所在下标
2. 数的左右边界 [1,2,3,3,3,4] 查找3返回[2, 4]
参考：https://www.cnblogs.com/kyoner/p/11080078.html
'''

def binarySearch1(nums, target):
    '查找一个数'
    l, r = 0, len(nums) - 1
    while l <= r: # [l, r]
        m = l + (r - l) // 2
        if nums[m] < target: l = m + 1
        elif nums[m] > target: r = m - 1
        else: return m
    return -1 # 找不到该元素

def binarySearch2(nums, target):
    '查找左边界'
    if not nums: return -1
    l, r = 0, len(nums)
    while l < r: # [l, r)
        m = l + (r - l) // 2
        if nums[m] < target: l = m + 1
        elif nums[m] >= target: r = m
    # 此时l == r, l表示了target左边有多少个小于它的数, 取值范围为[0, len(nums)]
    if l == len(nums): return -1
    return l if nums[l] == target else -1

def binarySearch3(nums, target):
    '寻找右边界'
    if not nums: return -1
    l, r = 0, len(nums)
    while l < r:
        m = l + (r - l) // 2
        if nums[m] <= target: l = m + 1
        elif nums[m] > target: r = m
    # 此时l == r, r - 1表示了target右边有多少个大于它的数, 取值范围为[0, len(nums)]
    if r == 0: return -1
    return r - 1 if nums[r - 1] == target else -1

if __name__ == '__main__':
    nums = [1,2,3,3,4]
    target= 5
    print(binarySearch1(nums, target))