# A function tha calculates character frequencies in a string.
def letter_frequency(in_string):
    frequencies = {}
      
    for i in in_string:
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    return frequencies

# Example run    
freqs = letter_frequency("This is just test string")

print(freqs)