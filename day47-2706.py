def odd_numbers(arr):
    return [x for x in arr if x % 2 != 0]
arr = [1, 2, 3, 4, 5]
print(odd_numbers(arr))