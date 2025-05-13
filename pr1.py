def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_primes(numbers):
    return [num for num in numbers if is_prime(num)]

# Приклад використання:
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
prime_numbers = filter_primes(numbers)
print(prime_numbers)  # Виведе: [2, 3, 5, 7, 11]