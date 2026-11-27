arr = [9, 4, 1, 7]
k = 2
arr.sort()
minimum_diff = float('inf')
for i in range(len(arr) - k + 1):
    diff = arr[i + k - 1] - arr[i]
    if diff < minimum_diff:
        minimum_diff = diff
print("Minimum Difference:", minimum_diff)