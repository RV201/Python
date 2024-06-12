#taking 3 integer as input from the user
base = int(input("Enter the value for base :"))
exponent = int(input("Enter the value for exponent :"))
result=1;
print("The result of ",base,"raised to the power of ",exponent," is ",end = ' ')
#using ‘for’ loop with ‘range’ function
for exponent in range(exponent, 0, -1):
    result *= base
print(result)