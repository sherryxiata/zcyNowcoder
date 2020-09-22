s = input()
years = []
i, j = 0, 0
while i < len(s):
    if '0' < s[i] <= '9':
        j = i
        while j < len(s) and '0' <= s[j] <= '9':
            j += 1
        if (j - i) == 4 and '1000' <= s[i:j] <= '3999':
            years.append(s[i:j])
        i = j
    else:
        i += 1
for y in years:
    print(y, end = ' ')

#abc 1000 3999 1000*,. *1000 *,10&67 1 0 0 1