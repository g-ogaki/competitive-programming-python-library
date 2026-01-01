# Link Cut Tree

Data structure that extends lazy segment tree for dynamic trees with vertices of monoid $(M, \cdot, e)$ to support:

- link: given two vertices `u` and `v`, make `u`'s parent `v`.
- cut: remove the edge between a node and its parent.
- evert: make a node the root of the tree.
- connectivity detection: determine whether two vertices are in the same connected component
- range update: update all vertices on the path between two vertices with a function $f \in \text{End}(M)$ (assuming these vertices are connected)
- range query: find the product of all vertices on the path between two vertices (assuming these vertices are connected)

## \_\_init\_\_

### Arguments
- `A: list[T]`: array of monoid $M$
- `dot: Callable[[T, T], T]`: binary operator corresponding to $\cdot$
- `e: T`: identity element of $M$
- `compose: Callable[[U, U], U]`: binary operator corresponding to $\circ$ in $(\text{End}(M), \circ, \text{id})$
- `id: U`: identity element of $\text{End}(M)$
- `act: Callable[[U, T, int], T]`: binary operator corresponding to $\text{End}(M) \times M \ni (f, x) \mapsto f(x) \in M$  
  - The third argument represents the size (length) of the path being updated.
  - This supports aggregations dependent on component size, such as range add/range sum (conceptually extending $M$ to $M \times \mathbb{N}_0$, which is called interval extension).

### Complexities
- time: $O(n)$
- space: $O(n)$

where $n$ represents the length of `A`.

## evert

Make a given node `v` the root of the tree including `v`.

### Arguments
- `v: int`: node to make the root of the tree

### Complexities
- $\text{amortized } O(\log n)$

## lca

Returns the lowest common ancestor of two given nodes `u` and `v`.

Note: Ancestors are dependant on the root, so you must explicitly call `evert` before using this method.

### Arguments
- `u: int`: first node
- `v: int`: second node

### Returns
- `int`: lowest common ancestor of `u` and `v`

### Complexities
- $\text{amortized } O(\log n)$

## link

Given two nodes `u` and `v`, make `u`'s parent `v`.

### Arguments
- `u: int`: the child node of `v`
- `v: int`: the parent node of `u`

### Complexities
- $\text{amortized } O(\log n)$

## cut

Given a node `u`, remove the edge between `u` and its parent.

### Arguments
- `u: int`: node to remove the edge from

### Complexities
- $\text{amortized } O(\log n)$

## is_connected

Returns whether vertices `u` and `v` are connected.

### Arguments

- `u: int`: vertex
- `v: int`: vertex

### Returns

- `bool`: `True` if vertices `u` and `v` are connected, `False` otherwise

### Complexities

- $	\text{amortized } O(\log n)$

## depth

Returns the depth of a given node `v`.

### Arguments

- `v: int`: node

### Returns

- `int`: depth of `v` (0-indexed)

### Complexities

- $\text{amortized } O(\log n)$

## act

Applies a function $f \in \text{End}(M)$ to all vertices on the path between two given nodes `u` and `v`.

### Arguments

- `u: int`: first node
- `v: int`: second node
- `f: U`: endomorphism to apply to the path between `u` and `v`

### Complexities

- $\text{amortized } O(\log n)$

## prod

Calculates the product of all vertices on the path between two given nodes `u` and `v`.

### Arguments

- `u: int`: first node
- `v: int`: second node

### Returns

- `T`: product of all vertices on the path between `u` and `v`

### Complexities

- $\text{amortized } O(\log n)$