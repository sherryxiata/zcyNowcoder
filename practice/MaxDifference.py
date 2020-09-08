#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 17:32
# @Author  : wenlei

# 一个数组，求任一元素减去该元素右边任一元素的差值的最大值。
# 暴力解法时间复杂度是o(n^2)，下面的解法可以达到O(N)

def maxDifference(nums):
    res = float('-inf')
    ma = nums[0]
    for num in nums[1:]:
        res = max(res, ma - num)
        ma = max(ma, num)
    return res

if __name__ == '__main__':
    nums = [1, 1, 1]
    print(maxDifference(nums))
