def replace_space(string, char):
  return string.replace(" ", char)
input_string = "end of the day"
replacement_char = "-"
output_string = replace_space(input_string, replacement_char)
print(output_string)