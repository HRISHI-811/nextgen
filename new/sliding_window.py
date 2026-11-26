def maxSubarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    left = 0
    for right in range(k, len(arr)):
        window_sum += arr[right] - arr[left]
        left += 1
        if window_sum > max_sum:
            max_sum = window_sum
    return max_sum
arr = [100, 200, 300, 400]
k = 2
print(maxSubarray(arr, k))
