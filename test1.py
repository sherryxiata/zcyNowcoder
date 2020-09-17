n, m = map(int, input().split())
m = m * 100
day = 1
down = 0
while m >= 0:
    if n > m: break
    m -= n
    down += n / (2 ** day)
    m += down
    day += 1
print(day)