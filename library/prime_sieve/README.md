# Prime Sieve

Lists all prime numbers less than or equal to a given number.

## prime_sieve

### Arguments
- `n: int`: integer up to which prime numbers are calculated

### Returns
- `primes, sieve: tuple[list[int], list[int]]`
  - `primes: list[int]`: list of prime numbers
  - `sieve: list[int]`: lowest prime factor of each number

### Complexities
- $O(n)$