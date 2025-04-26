import numpy as np

def find_primes(n):
    """
    Find all prime numbers up to n.
    
    Parameters:
        n (int): The upper limit to search for primes. If n is less than 2, the function returns an empty list.

    Returns:
        list: A list of prime numbers up to n.
    """
    if n < 2:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, n + 1, i):
                sieve[j] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

# Example usage
n = 30
print(f"Primes up to {n}: {find_primes(n)}")
