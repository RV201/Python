def convert_vowels_to_uppercase(str):
  vowels = "aeiou"
  str_list = list(str)
  for i in range(len(str_list)):
    if str_list[i].lower() in vowels:
      str_list[i] = str_list[i].upper()
  return "".join(str_list)
input_string = "end of the day"
print("Original String:", input_string)
print("String with Uppercase Vowels:",
convert_vowels_to_uppercase(input_string))