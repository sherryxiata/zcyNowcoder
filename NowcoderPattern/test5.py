import sys
import math

for line in sys.stdin:
    n,m = map(int,line.strip().split())
    sum = n
    for i in range(m-1):
        n = math.sqrt(n)
        sum += n
    print('%.2f' % sum)