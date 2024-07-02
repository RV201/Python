def right_rotate(arr, d):
    return arr[-d % len(arr):] + arr[:-d % len(arr)]
arr = [1, 2, 3, 4, 5]
print(right_rotate(arr, 2))