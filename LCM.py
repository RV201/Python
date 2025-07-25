def compute_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def compute_lcm(x, y):
    return (x * y) // compute_gcd(x, y)

# Example usage
num1 = 54
num2 = 24
print("The L.C.M. is", compute_lcm(num1, num2))
