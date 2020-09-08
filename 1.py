n = int(input())
porkers = []
for _ in range(n):
    tmp = input()
    if tmp == 'J': porkers.append(11)
    elif tmp == 'Q': porkers.append(12)
    elif tmp == 'K': porkers.append(13)
    elif tmp == 'A': porkers.append(14)
    elif tmp == '2': porkers.append(15)
    else: porkers.append(int(tmp))
# print(porkers)

porkers = sorted(porkers)
# print(porkers)
res = []
for p in porkers:
    if p == 11: res.append('J')
    elif p == 12: res.append('Q')
    elif p == 13: res.append('K')
    elif p == 14: res.append('A')
    elif p == 15: res.append('2')
    else: res.append(str(p))

for c in res:
    print(c)

abilities = list(map(int, input().split()))
tasks = list(map(int, input().split()))
mi = min(abilities)
res = 0
while len(tasks) > 0:
    t = tasks.pop(0)
    if mi <= t:
        ma = mi
        for num in abilities:
            if num <= t:
                ma = max(ma, num)
        mi = min(abilities)
        res += 1
        abilities.pop(abilities.index(ma))
    # print(tasks)
    # print(abilities)
print(res)