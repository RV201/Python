def delete_at_index(arr, index):
    return arr[:index] + arr[index+1:]
arr = [1, 2, 3, 4, 5]
print(delete_at_index(arr, 2))