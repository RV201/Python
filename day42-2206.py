def insert_at_index(arr, index, element):
    arr[index:index] = [element]
    return arr
arr = [1, 2, 3, 4, 5]
print(insert_at_index(arr, 2, 6))