s = input()
dict = {}
for c in s:
    if c in dict:
        dict[c] += 1
    else:
        dict[c] = 1
dict = sorted(dict.items(), key = lambda x: x[0])
# print(dict)
for num in dict:
    print(num[0] + '=' + str(num[1]), end = ' ')
print()