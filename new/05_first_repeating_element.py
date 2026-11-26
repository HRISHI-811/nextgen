# 5. First Repeating Element

arr = [10, 5, 3, 4, 3, 5, 6]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for num in arr:
    if freq[num] > 1:
        print(num)
        break
