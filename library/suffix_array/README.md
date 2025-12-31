# Suffix Array

Calculate the suffix array (i.e., the lexicographical order of all suffixes) and the lcp array (i.e., the length of the longest common prefix of consecutive suffixes) of a string.

As of 2025/12/31, this implementation is the [fastest](https://atcoder.jp/contests/practice2/submissions?f.LanguageName=Python&f.Status=AC&f.Task=practice2_i&f.User=&orderBy=time_consumption) in Python3 (PyPy).

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