# Python program to find GCD of two numbers

# take inputs
x = int(input('Enter First Number: '))
y = int(input('Enter Second Number: '))

# choose the smaller number
if x > y:
    smaller = y
else:
    smaller = x
    
# find gcd of the number
for i in range (1,smaller+1):
    if((x % i == 0) and (y % i == 0)):
        gcd = i

# display result
print('The GCD of',x,'and',y,'is',gcd)