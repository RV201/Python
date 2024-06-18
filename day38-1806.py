def top_two_maximum(numbers):
  sorted_numbers = sorted(set(numbers), reverse=True)
  return (sorted_numbers[0], sorted_numbers[1])
numbers = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 9, 9]
top_two = top_two_maximum(numbers)
print("The top two maximum numbers are:", top_two)