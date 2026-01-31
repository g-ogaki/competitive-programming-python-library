# Rolling Hash

Calculates a hash of all substrings so that it can be compared in $O(1)$.

## \_\_init\_\_

Calculates the hash of all substrings.

### Arguments
- `S: str`: string to calculate hashes

### Complexities
- time: $O(n)$
- space: $O(n)$

where $n$ represents the length of the string `S`.

## add

Concatenates two hashes of strings.

### Arguments
- `hash1: tuple[int, int]`: hash of the first string
- `hash2: tuple[int, int]`: hash of the second string

### Returns
- `tuple[int, int]`: hash of the concatenated string

### Complexities
- $O(1)$

## \_\_getitem\_\_

Returns the hash of the substring $S[l:r]$.

### Arguments
- `l: int`: left index
- `r: int`: right index

### Returns
- `tuple[int, int]`: hash of the substring $S[l:r]$

### Complexities
- $O(\log n)$

## \_\_setitem\_\_

Changes the character at index `i` to `c`.

### Arguments
- `i: int`: index to change
- `c: str`: character to change

### Complexities
- $O(\log n)$
