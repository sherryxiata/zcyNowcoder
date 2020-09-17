s = input()
if not s: print()
years = []
i, j = 0, 0
while i < len(s):
    if '0' <= s[i] <= '9':
        j = i
        while j < len(s) and '0' <= s[j] <= '9':
            j += 1
        if len(s[i:j]) == 4 and '1000' <= s[i:j] <= '3999':
            years.append(s[i:j])
        i = j
    else:
        i += 1
for y in years:
    print(y, end = ' ')