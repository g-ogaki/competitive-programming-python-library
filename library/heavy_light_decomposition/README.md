# Heavy Light Decomposition

Data structure to decompose a tree into at most $O(\log n)$ paths. This is useful for answering point/path updates and path queries (most likely in combination with segment tree).

## \_\_init\_\_

### Arguments

- `G: list[list[int]]`: tree as an adjacency list
- `root: int = 0`: root of the tree

### Complexities

- time: $O(n)$
- space: $O(n)$

where $n$ represents the number of nodes in the tree.

## lca

Finds the lowest common ancestor of two nodes.

### Arguments

- `u: int`: first node
- `v: int`: second node

### Returns

- `int`: the lowest common ancestor of `u` and `v`

### Complexities

- $O(\log n)$

## node_to_order

Returns the decomposition order of nodes so that the nodes on the same path are consecutive.

### Returns

- `list[int]`: decomposition order mapping nodes to indices

## edge_to_order

Converts edges to the decomposition order.

### Arguments

- `E: list[tuple[int, int]]`: edges

### Returns

- `list[int]`: decomposition order mapping edges to indices

## path

Returns the decomposition order of the path from `u` to `v`.

### Arguments

- `u: int`: first node
- `v: int`: second node

### Returns

- `list[tuple[int, int]]`: list of paths from `u` to `v`
  - Each element `(i, j)` represents the consecutive indices $\{i, i + 1, \ldots, j - 1, j\}$ (or $\{j, j + 1, \ldots, i - 1, i\}$ if $i > j$) of a path.

### Complexities

- $O(\log n)$
