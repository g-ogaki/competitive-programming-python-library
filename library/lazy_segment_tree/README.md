# Lazy Segment Tree

Data structure for arrays of monoids $(M, \cdot, e)$ and its endomorphism monoid $(\text{End}(M), \circ, \text{id})$ that supports:

- range update: $A[l] \gets f(A[l]), A[l+1] \gets f(A[l+1]), \ldots, A[r-1] \gets f(A[r-1])$
- range query: find $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$

## \_\_init\_\_

### Arguments
- `A: list[T]`: array of monoid $M$
- `dot: Callable[[T, T], T]`: binary operator corresponding to $\cdot$
- `e: T`: identity element of $M$
- `compose: Callable[[U, U], U]`: binary operator corresponding to $\circ$
- `id: U`: identity element of $\text{End}(M)$
- `act: Callable[[T, U], T]`: binary operator corresponding to $\text{End}(M) \times M \ni (f, x) \mapsto f(x) \in M$

### Complexities
- time: $O(n)$
- space: $O(n)$

where $n$ represents the length of `A`.

## act

Updates the subarray $A[l:r]$ with the endomorphism $f$.

### Arguments
- `l: int`: left endpoint of the range (inclusive)
- `r: int`: right endpoint of the range (exclusive)
- `f: U`: endomorphism to act on the subarray $A[l:r]$

### Complexities
- $O(\log n)$

## prod

Calculates the product of the subarray $A[l:r]$.

### Arguments
- `l: int`: left endpoint of the range (inclusive)
- `r: int`: right endpoint of the range (exclusive)

### Returns
- `T`: $A[l] \cdot A[l+1] \cdot \ldots \cdot A[r-1]$

### Complexities
- $O(\log n)$