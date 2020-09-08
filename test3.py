def find(matrix, m, n):
    mi, mi2 = matrix[0][0], matrix[0][0]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] < mi2:
                mi2 = matrix[i][j]
                if mi2 < mi:
                    mi, mi2 = mi2, mi
    # print(mi, mi2)
    if mi + 1 != mi2:
        return mi + 1
    else:
        return mi - 1

m = int(input())
n = int(input())
matrix = [[None] * n for _ in range(m)]
for i in range(m):
    tmp = list(map(int, input().split()))
    for j in range(n):
        matrix[i][j] = tmp[j]
# print(matrix)
print(find(matrix, m, n))