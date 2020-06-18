#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/10 19:18
# @Author  : wenlei

#找数组的最大值（递归）

def getMax(arr,L,R):
    if L == R:
        return arr[L]
    mid = int((L+R)/2)
    l_max = getMax(arr,L,mid)
    r_max = getMax(arr,mid+1,R)
    return max(l_max,r_max)

if __name__ == '__main__':
    arr = [4,3,2,1]
    print(getMax(arr,0,len(arr)-1))

