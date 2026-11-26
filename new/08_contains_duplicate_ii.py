# 8. Contains Duplicate II (LeetCode 219)

nums = [1, 2, 3, 1]
k = 3

last_index = {}

for i in range(len(nums)):
    if nums[i] in last_index:
        if i - last_index[nums[i]] <= k:
            print(True)
            break

    last_index[nums[i]] = i
else:
    print(False)
