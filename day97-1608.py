def left_rotate(arr, d):
    return arr[d % len(arr):] + arr[:d % len(arr)]
arr = [1, 2, 3, 4, 5]
print(left_rotate(arr, 2))