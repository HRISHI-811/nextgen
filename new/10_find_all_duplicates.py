# 10. Find All Duplicates in an Array

nums = [4, 3, 2, 7, 8, 2, 3, 1]

freq = {}

for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    if freq[key] > 1:
        print(key)
