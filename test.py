def two(l1, l2):
    res = []
    for s2 in l2:
        for s1 in l1:
            res.append(s1 + '-' + s2)
    return res

def process(list):
    res = []
    l1 = list[0]
    for tmp in list[1:]:
        l2 = tmp
        two_res = two(l1, l2)
        l1 = two_res
    return l1

if __name__ == '__main__':
    n = int(input())
    all = []
    for _ in range(n):
        all.append(list(input().split()))
    res= process(all)
    for i in res:
        print(i)


def count(s):
    if not s or len(s) < 2: return 0
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    cnt = 0
    for j in range(n):
        for i in range(0, j + 1):
            length = j - i + 1
            if length == 1:
                dp[i][j] = True
            if length == 2 and s[i] == s[j]:
                dp[i][j] = True
                cnt += 1
            if length > 2 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                dp[i][j] = True
                cnt += 1
    return cnt

if __name__ == '__main__':
    s = input()
    print(count(s))


def distance(l1, l2):
    n1, n2 = len(l1), len(l2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for j in range(1, n2 + 1):
        dp[0][j] = dp[0][j - 1] + 1
    for i in range(1, n1 + 1):
        dp[i][0] = dp[i - 1][0] + 1
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            if l1[i - 1] == l2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
    return dp[-1][-1]

stop = list(input().split())
s1 = input().split()
s2 = input().split()
list1, list2 = [], []
for c in s1:
    if not c in stop:
        list1.append(c)
for c in s2:
    if not c in stop:
        list2.append(c)
# print(list1, list2)
print(distance(list1, list2))


