#Given a count N, print the first N prime numbers.
#Example: if N = 20, print the first 20 primes, even though the final prime is greater than 20
n = int(input("Enter how many prime numbers you want: "))

primes = []
candidate = 2

while len(primes) < n:
    is_prime = True
    for divisor in range(2, int(candidate ** 0.5) + 1):
        if candidate % divisor == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(candidate)
    candidate += 1

print(primes)
