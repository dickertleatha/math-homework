def calculate_derivative(f, x):
    return 2 * f(x + 1) - 3 * f(x)

f = lambda x: (x ** 2) / (x - 1)
derivative_f = calculate_derivative(f, 0.5)
print(derivative_f)
