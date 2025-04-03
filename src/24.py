def calculate_sum_of_squares(n):
    total = sum(x**2 for x in range(1, n+1))
    return total

n = 5
result = calculate_sum_of_squares(n)
print("The sum of squares from 1 to", n, "is:", result)
