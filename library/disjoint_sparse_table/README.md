# Disjoint Sparse Table

Data structure for arrays of semi-groups that supports range queries.

## \_\_init\_\_

### Arguments

- `A: list[T]`: array of the semi-group
- `dot: Callable[[T, T], T]`: binary operation of the semi-group

### Complexities

- Time: $O(n \log n)$
- Space: $O(n \log n)$

## prod

Calculates the product of $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$.

### Arguments

- `l: int`: left endpoint of the range (inclusive)
- `r: int`: right endpoint of the range (exclusive)

### Returns

- `T`: $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$

### Complexities

- $O(1)$