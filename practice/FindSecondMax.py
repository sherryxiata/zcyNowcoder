#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 9:53
# @Author  : wenlei

'''
快速找出数组中最大、第二大的数
'''

def findSecondMax(nums):
    if len(nums) < 3: return nums
    ma, ma2 = nums[0], nums[0]
    for num in nums:
        if num > ma:
            ma2 = ma
            ma = num
        elif ma2 < num < ma:
            ma2 = num
    return [ma2, ma]

if __name__ == '__main__':
    arr = [1,8,8,8,6]
    print(findSecondMax(arr))