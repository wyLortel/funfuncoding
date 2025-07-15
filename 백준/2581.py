M = int(input())
N = int(input())

primes = []

for i in range(M, N + 1):
    if i < 2:
        continue
    is_prime = True
    for k in range(2, int(i ** 0.5) + 1):
        if i % k == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

if primes:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)