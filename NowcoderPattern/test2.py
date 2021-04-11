import sys

t = int(sys.stdin.readline())

for line in range(t):
    a = list(map(int,sys.stdin.readline().strip().split()))
    print(a[0]+a[1])



