# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        def printFrame(m, tr, tc, dr, dc):
            if tr == dr and dr == dc:
                return [m[tr][tc]]
            res = []
            for j in range(tc, dc):
                res.append(m[tr][j])
            for i in range(tr, dr):
                res.append(m[i][dc])
            for j in range(dc, tc, -1):
                res.append(m[dr][j])
            for i in range(dr, tr, -1):
                res.append(m[i][tc])
            return res

        if not matrix or not matrix[0]: return []
        res = []
        tr, tc, dr, dc = 0, 0, len(matrix) - 1, len(matrix[0]) - 1
        while tr < dr or tc < dc:
            res += printFrame(matrix, tr, tc, dr, dc)
            tr += 1
            tc += 1
            dr -= 1
            dc -= 1
        return res

if __name__ == '__main__':
    m = [[1,2,3],[5,6,7],[9,10,11],[13,14,15,16]]
    print(Solution().printMatrix(m))