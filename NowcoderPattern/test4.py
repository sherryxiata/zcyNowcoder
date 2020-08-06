import sys

n = int(sys.stdin.readline())
str = list(sys.stdin.readline().strip().split())
str.sort()
result = ''
for i in range(n-1):
    result += str[i] + ' '
result += str[n-1]
print(result)
