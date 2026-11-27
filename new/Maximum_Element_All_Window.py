arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
for i in range(len(arr) - k + 1):
    maximum = arr[i]
    for j in range(i, i + k):
        if arr[j] > maximum:
            maximum = arr[j]
    print(maximum, end=" ")