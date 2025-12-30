# Lowlink

Lists all the bridges in an undirected graph (i.e., the edges that, if removed, increase the number of connected components).

## lowlink

### Arguments

- `n: int`: number of vertices
- `E: list[tuple[int, int]]`: list of edges

### Returns

- `G, is_bridge: tuple[list[list[tuple[int, int]]], list[bool]]`
  - `G: list[list[tuple[int, int]]]`: adjacency list of the graph with edge indices
  - `is_bridge: list[bool]`: list of booleans indicating whether each edge is a bridge

### Complexities

- $O(V + E)$