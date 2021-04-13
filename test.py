s = [1,5,4,2,4]

# 最大的一个元素的序号
max_ind, ma = 0, 0
for i in range(len(s)):
    if s[i] > ma:
        max_ind = i
        ma = s[i]
print(max_ind)

# 最大的三个元素的序号

