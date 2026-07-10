def divisors(n):
    primes = []
    divisors = [1]
    p = 2
    while p * p <= n:
        if n % p == 0:
            primes.append((l := len(divisors), p))
            while n % p == 0:
                divisors += [d * p for d in divisors[-l:]]
                n //= p
        p += 1
    if n > 1:
        primes.append((len(divisors), n))
        divisors += [d * n for d in divisors]
    return primes, divisors

print(divisors(12))