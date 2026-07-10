# Divisors

Lists divisors of a number.

## divisors

### Arguments
- `n: int`: integer whose divisors will be listed

### Returns
- `primes, divisors: tuple[list[tuple[int, int]], list[int]]`
  - `primes: list[tuple[int, int]]`: prime factors and their indices in `divisors`
  - `divisors: list[int]`: divisors of $n$ whose indices follow the flattened Hasse diagram

### Complexities
- $O(\sqrt{n})$