#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 14:07
# @Author  : wenlei

'''
两个数组去重排序
'''

def sortArr(nums1, nums2):
    i, j = 0, 0
    res = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if nums1[i] not in res: res.append(nums1[i])
            i += 1
        else:
            if nums2[j] not in res: res.append(nums2[j])
            j += 1
    while i < len(nums1):
        if nums1[i] not in res:
            res.append(nums1[i])
        i += 1
    while j < len(nums2):
        if nums2[j] not in res:
            res.append(nums2[j])
        j += 1
    return res

if __name__ == '__main__':
    nums1 = [1, 2, 2, 5, 8]
    nums2 = [3, 5, 7, 9]
    print(sortArr(nums1, nums2))