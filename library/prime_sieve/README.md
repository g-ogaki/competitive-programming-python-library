# Prime Sieve

List all prime numbers less than or equal to a given number.

## Arguments
- `n: int`: integer up to which prime numbers are calculated

## Returns
- `primes, sieve: tuple[list[int], list[int]]`
  - `primes: list[int]`: list of prime numbers
  - `sieve: list[int]`: lowest prime factor of each number

## Complexities
- Time: $O(n)$
- Space: $O(n)$