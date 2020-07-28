class Solution:
    def findContinuousSequence(self, target):
        # 解法2：数学法
        # 这实际上是一个等差数列，首项为a1，项数为n，求满足数列和为target的[a1, n]对
        res = []
        for n in range(2, target + 1):
            tmp = target - n * (n - 1) / 2
            if tmp < 0:
                # 随着n的增长，a1会小于0，此时跳出循环
                break
            else:
                if not

