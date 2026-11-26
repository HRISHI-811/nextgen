# 11. Missing Number

nums = [3, 0, 1]

freq = {}

for num in nums:
    freq[num] = 1

for i in range(len(nums) + 1):
    if i not in freq:
        print(i)
        break
