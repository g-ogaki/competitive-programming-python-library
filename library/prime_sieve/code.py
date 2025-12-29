def prime_sieve(n):
    primes = []
    sieve = list(range(n + 1))
    for i in range(2, n + 1):
        if sieve[i] == i:
            primes.append(i)
        for p in primes:
            if sieve[i] < p or i * p > n:
                break
            sieve[i * p] = p
    return primes, sieve

if __name__ == "__main__":
    primes, sieve = prime_sieve(100)
    print(primes)