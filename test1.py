s1 = input()
s2 = input()
n, m = len(s1), len(s2)
t = 2 * n - m
s = ['0'] * t
i, j = 0, n - 1
k, l = 0, 0
while i <= j:
    if s1[i] != s2[k]:
        s[l] = s1[i]
        s[t - l - 1] = s1[i]
        i += 1
    elif s1[j] != s2[k]:
        s[l] = s1[j]
        s[t - l - 1] = s1[j]
        j -= 1
    else:
        s[l] = s1[j]
        s[t - l - 1] = s1[j]
        j -= 1
        i += 1
        k += 1
    l += 1
    print(s)
print(''.join(s))
