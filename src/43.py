def calculate_sums(n):
    sums = []
    for i in range(1, n + 1):
        sum_i = sum(range(i))
        sums.append(sum_i)
    return sums

n = int(input("Enter a number: "))
print(calculate_sums(n))
