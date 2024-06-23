def delete_element(arr, element):
    arr.remove(element)
    return arr
arr = [1, 2, 3, 4, 5]
print(delete_element(arr, 3))