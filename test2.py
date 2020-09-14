def max58(s):
    i = 0
    res = []
    while i < len(s):
        if int(s[i]) in [5, 6, 7, 8]:
            j = i
            while j < len(s) and int(s[j]) in [5, 6, 7, 8]:
                j += 1
            res.append(s[i:j])
            i = j
        else:
            i += 1
    # print(res)
    return max(res, key = len)

if __name__ == '__main__':
    s = input()
    print(max58(s))

