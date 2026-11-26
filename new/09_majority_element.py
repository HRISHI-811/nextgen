# 9. Majority Element

nums = [2, 2, 1, 1, 1, 2, 2]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    if freq[key] > len(nums) // 2:
        print(key)
        break
