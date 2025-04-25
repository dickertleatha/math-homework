import numpy as np

def calculate_greatest_common_divisor(a, b):
    if b == 0:
        return a
    else:
        gcd = calculate_greatest_common_divisor(b, a % b)
        return int(gcd)

# Example usage:
a = 48
b = 18
print("GCD of", a, "and", b, "is:", calculate_greatest_common_divisor(a, b))
