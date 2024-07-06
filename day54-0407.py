from collections import Counter
def highest_frequency(arr):
    count = Counter(arr)
    return max(count, key=count.get)
arr = [1, 2, 3, 4, 5, 3, 2, 2]
print(highest_frequency(arr))