# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        def binarySearch(arr, l, r):
            if l > r:
                return 0
            m = l + (r - l) // 2
            if k < arr[m]:
                return binarySearch(arr, l, m - 1)
            elif k > arr[m]:
                return binarySearch(arr, m + 1, r)
            else:
                return 1

        binarySearch(data, 0, len(data) - 1)

if __name__ == '__main__':
    arr = [1,2,2,3,5]
    print(Solution().GetNumberOfK(arr, 2))