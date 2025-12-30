# Union Find

Data structure for undirected graphs that supports:

- edge addition: connect two vertices
- connectivity detection: determine whether two vertices are in the same connected component

## \_\_init\_\_

### Arguments

- `n: int`: number of vertices

### Complexities

- Time: $O(n)$
- Space: $O(n)$

## root

Returns the representative of the connected component containing vertex `k`. While rarely used directly, this method can be used to determine if two vertices belong to the same component.

### Arguments

- `k: int`: vertex

### Returns

- `int`: representative of the connected component containing vertex `k`

### Complexities

- $\text{amortized } O(\alpha(n))$

## unite

Add an edge spanning between vertices `i` and `j`.

### Arguments

- `i: int`: vertex
- `j: int`: vertex

### Returns

- `bool`: `True` if the edge was added (`i` and `j` were not connected), `False` otherwise

### Complexities

- $\text{amortized } O(\alpha(n))$


## is_connected

Returns whether vertices `i` and `j` are connected.

### Arguments

- `i: int`: vertex
- `j: int`: vertex

### Returns

- `bool`: `True` if vertices `i` and `j` are connected, `False` otherwise

### Complexities

- $	\text{amortized } O(\alpha(n))$

## size

Returns the size of the connected component containing vertex `k`.

### Arguments

- `k: int`: vertex

### Returns

- `int`: size of the connected component containing vertex `k`

### Complexities

- $\text{amortized } O(\alpha(n))$