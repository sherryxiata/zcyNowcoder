# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    # 一层一层打印边框，难点是边界的coding能力 O(MN) O(1)
    def printMatrix(self, matrix):
        # write code here
        def printFrame(m, tr, tc, dr, dc):
            res = []
            # 在同一行
            if tr == dr:
                while tc <= dc:
                    res.append(m[tr][tc])
                    tc += 1
            # 在同一列
            elif tc == dc:
                while tr <= dr:
                    res.append(m[tr][tc])
                    tr += 1
            # 多行多列
            else:
                i, j = tr, tc
                while j < dc:
                    res.append(m[tr][j])
                    j += 1
                while i < dr:
                    res.append(m[i][dc])
                    i += 1
                while j > tc:
                    res.append(m[dr][j])
                    j -= 1
                while i > tr:
                    res.append(m[i][tc])
                    i -= 1
            return res

        if not matrix or not matrix[0]: return []
        res = []
        tr, tc, dr, dc = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while tr <= dr and tc <= dc:
            res += printFrame(matrix, tr, tc, dr, dc)
            tr += 1
            tc += 1
            dr -= 1
            dc -= 1
        return res

if __name__ == '__main__':
    m = [[1,2,3],[5,6,7],[9,10,11]]
    print(Solution().printMatrix(m))