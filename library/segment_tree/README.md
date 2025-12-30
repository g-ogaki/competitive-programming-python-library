# Segment Tree

Data structure for arrays of monoids $(M, \cdot, e)$ that supports:

- point update: $A[i] \gets v$
- range query: Find $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$
- lower bound: Given $l$ and $x$, find the largest $r$ such that $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1] < x$.

## \_\_init\_\_

### Arguments
- `A: list[T]`: array of monoid $M$
- `dot: Callable[[T, T], T]`: binary operator corresponding to $\cdot$
- `e: T`: identity element corresponding to $e$

### Complexities
- Time: $O(n)$
- Space: $O(n)$

where $n$ represents the length of `A`.

## \_\_getitem\_\_

Returns the `i`-th element of the array.

### Arguments
- `i: int`: index

### Returns
- `T`: element at index `i`

### Complexities
- $O(1)$

## \_\_setitem\_\_

Sets the `i`-th element of the array

### Arguments
- `i: int`: index
- `x: T`: new element

### Complexities
- $O(\log n)$

## prod

Calculates the product of the subarray $A[l:r]$.

### Arguments
- `l: int`: left index
- `r: int`: right index

### Returns
- `T`: $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$

### Complexities
- $O(\log n)$

## bisect_left

Finds the largest $r$ such that product of subarray $A[l:r]$ is less than $x$.

### Arguments
- `l: int`: left index
- `x: T`: threshold

### Returns
- `int`: largest $r$ such that $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1] < x$.

### Complexities
- $O(\log n)$