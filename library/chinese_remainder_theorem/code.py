from math import gcd
from collections import Counter, defaultdict

N = 1_000_000
primes = []
sieve = list(range(N + 1))
for i in range(2, N + 1):
    if sieve[i] == i:
        primes.append(i)
    for p in primes:
        if sieve[i] < p or i * p > N:
            break
        sieve[i * p] = p

def _primality_test(n):
    d = (n - 1) // ((n - 1) & -(n - 1))
    s = ((n - 1) // d).bit_length()
    for a in (2, 7, 61) if n < 4_759_123_141 else (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        y = pow(a, d, n)
        if y == 1:
            continue
        for _ in range(s):
            if y == n - 1:
                break
            y = y * y % n
        else:
            return False
    return True

def prime_factorization(n):
    res = Counter()
    queue = [n]
    for n in queue:
        if n < len(sieve):
            while n > 1:
                res[sieve[n]] += 1
                n //= sieve[n]
            continue
        if _primality_test(n):
            res[n] += 1
            continue
        c, m = 0, 1 << n.bit_length() - 3
        while True:
            c += 1
            y = g = q = r = 1
            while g == 1:
                x, k = y, 0
                for _ in range(r):
                    y = (y * y + c) % n
                while k < r and g == 1:
                    ys = y
                    for i in range(min(m, r - k)):
                        y = (y * y + c) % n
                        q = q * abs(x - y) % n
                    g = gcd(q, n)
                    k += m
                r <<= 1
            if g == n:
                g = 1
                while g == 1:
                    ys = (ys * ys + c) % n
                    g = gcd(abs(x - ys), n)
            if g != n:
                queue.append(g)
                queue.append(n // g)
                break
    return res

def modinv(a, m):
    b, u, v = m, 1, 0
    while b:
        a, b, u, v = b, a - a // b * b, v, u - a // b * v
    return u % m

def garner(R, M):
    T = []
    for r, m in zip(R, M):
        c = 1
        for t, _m in zip(T, M):
            r -= c * t
            c = c * _m % m
        T.append(r * modinv(c, m) % m)
    return T

def crt(R, M, MOD=0):
    X = defaultdict(lambda:(0, 0))
    for r, m in zip(R, M):
        for p, e in prime_factorization(m).items():
            _e, _r = X[p]
            if (r - _r) % p**min(e, _e):
                return -1
            if e > _e:
                X[p] = (e, r)
    R, M = [], []
    for p, v in X.items():
        R.append(v[1])
        M.append(p**v[0])
    res = 0
    for t, m in zip(garner(R, M)[::-1], M[::-1]):
        res = (res * m + t) % MOD if MOD else res * m + t
    return res

if __name__ == "__main__":
    R = [2, 4, 1]
    M = [3, 5, 7]
    print(crt(R, M))
    print(crt(R, M, MOD=11))