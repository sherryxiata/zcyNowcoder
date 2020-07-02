# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 10:27
# @Author  : wenlei

'''
找到数组中的局部最小位置
'''

def findLocalMin(arr):
    if not arr or len(arr) == 0:
        return -1 # 没有局部最小
    if len(arr) == 1 or arr[0] < arr[1]:
        return 0
    if arr[-1] < arr[-2]:
        return len(arr) - 1
    left = 1
    right = len(arr) - 2
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid - 1]:
            # 局部最小在左半边
            right = mid - 1
        elif arr[mid] > arr[mid + 1]:
            left = mid + 1
        else:
            return mid
    return left

if __name__ == '__main__':
    arr = [6, 5, 3, 4, 6, 7, 8 ]
    index = findLocalMin(arr)
    print(arr[index]) # 3