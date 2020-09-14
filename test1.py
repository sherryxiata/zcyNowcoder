def maxMoney(nums):
    if len(nums) <= 5: return sum(nums)
    res = []
    res.append(sum(nums[-5:]))
    res.append(nums[0] + sum(nums[-4:]))
    res.append(sum(nums[0:2]) + sum(nums[-3:]))
    res.append(sum(nums[0:3]) + sum(nums[-2:]))
    res.append(sum(nums[0:4]) + nums[-1])
    res.append(sum(nums[0:5]))
    return max(res)

if __name__ == '__main__':
    moneys = input().strip('[')
    moneys = moneys.strip(']')
    # print(moneys)
    if not moneys:
        print(0)
        exit()
    moneys = list(map(int, moneys.split(',')))
    print(maxMoney(moneys))
