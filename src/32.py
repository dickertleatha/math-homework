def sum_of_squares(numbers):
    total = 0
    for number in numbers:
        total += number * number
    return total

print(sum_of_squares([1, 2, 3]))
