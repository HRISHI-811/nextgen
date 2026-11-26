# 3. Find All Non-Repeating Elements

arr = [1, 2, 2, 3, 1, 4, 2]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    if freq[key] == 1:
        print(key)
