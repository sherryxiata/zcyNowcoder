#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/4 9:57
# @Author  : wenlei

'''
给定一个整型数组，请打印出元素和为0的所有子数组。
'''

def subArraySum(nums):
    res = []
    dict = {0:[-1]}
    sum = 0
    for i in range(len(nums)):
        # print(dict)
        sum += nums[i]
        if sum in dict:
            # 如果和在之前出现过，表示至少有一个和为0的子数组
            index_list = dict[sum]
            for index in index_list:
                res.append(nums[index + 1: i + 1])
            dict[sum].append(i)
        else:
            dict[sum] = [i]
    return res

if __name__ == '__main__':
    nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    res = subArraySum(nums)
    for arr in res:
        print(arr)