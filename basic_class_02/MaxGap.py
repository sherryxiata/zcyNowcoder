# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 9:00
# @Author  : wenlei


'''求排序后的数组相邻两数的最大差值
'''

import random

def maxGap(arr):
    if not arr or len(arr) < 2:
        return 0
    length = len(arr)
    mini = min(arr)
    maxi = max(arr)
    if mini == maxi:
        return 0
    # 有N个元素则准备N + 1个桶
    # 桶是否有元素
    hasNum = [False] * (length + 1)
    # 每个桶的最小值和最大值
    mins = [None] * (length + 1)
    maxs = [None] * (length + 1)
    for i in range(length):
        # 计算每个元素属于哪个桶
        bid = bucket(arr[i], length, mini, maxi)
        mins[bid] = min(mins[bid], arr[i]) if hasNum[bid] else arr[i]
        maxs[bid] = max(maxs[bid], arr[i]) if hasNum[bid] else arr[i]
        hasNum[bid] = True

    res = 0
    lastMax = maxs[0]
    for j in range(1, length + 1):
        if hasNum[j]:
            res = max(res, mins[j] - lastMax)
            lastMax = maxs[j]
    return res

def bucket(num, len, min, max):
    return int((num - min) * len / (max - min))

# for test
def comparator(arr):
    if not arr or len(arr) < 2:
        return 0
    arr.sort()
    res = 0
    for i in range(1, len(arr)):
        res = max(res, arr[i] - arr[i - 1])
    return res

def generateRandomArray(maxSize,maxValue):
    arr = [None] * int((maxSize + 1) * random.random())
    for i in range(len(arr)):
        arr[i] = int((maxValue + 1)*random.random()) - int((maxValue)*random.random())
    return arr

def copyArray(arr):
    if len(arr) == 0:
        return []
    arr1 = [None] * len(arr) # 必须要事先声明一个空数组，不然会始终和arr一模一样！！！
    for i in range(len(arr)):
        arr1[i] = arr[i]
    return arr1

if __name__ == '__main__':
    testTime = 50000
    maxSize = 100
    maxValue = 100
    success = True

    for i in range(testTime):
        arr1 = generateRandomArray(maxSize,maxValue)
        arr2 = copyArray(arr1)
        res1 = maxGap(arr1)
        res2 = comparator(arr2)

        if res1 != res2:
            success = False
            print(res1)
            print(res2)
            break

    print('Nice!') if success else print('Fuck!')
