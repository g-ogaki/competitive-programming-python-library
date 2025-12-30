# Suffix Array

Calculate the suffix array (i.e., the lexicographical order of all suffixes) and the lcp array (i.e., the length of the longest common prefix of consecutive suffixes) of a string.

## \_\_init\_\_

### Arguments

- `S: str`: input string

### Complexities

- Time: $O(n)$
- Space: $O(n)$

## sa

### Returns

- `list[int]`: suffix array

## lcp

### Returns

- `list[int]`: lcp array