import random

def generate_random_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]


random_numbers = generate_random_numbers(10)
print(random_numbers) 