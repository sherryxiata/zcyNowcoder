def minAdd(s):
    # dp[i][j]表示字符串从位置i到位置j是回文串所要添加字符的最少次数
    # 如果s[i] == s[j]: dp[i][j] = dp[i + 1][j - 1]
    # 如果s[i] != s[j]: 可以在s[i]前面加上s[j]/s[j]后面加上s[i]
    # dp[i][j] = min(dp[i + 1][j], dp[i][j + 1]) + 1
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    #  k表示i和j之间的间隔
    for k in range(1, n):
        i = 0
        while i + k < n:
            j = i + k
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1
    return dp[0][n - 1]

if __name__ == '__main__':
    s = input()
    print(minAdd(s))
