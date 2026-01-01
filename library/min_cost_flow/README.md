# Min Cost Flow

Solves minimum cost (b-)flow problem.

As of 2025/12/31, this implementation is the [fastest](https://judge.yosupo.jp/submissions/?problem=min_cost_b_flow&user=&dedupUser=false&status=AC&lang=pypy3&order=%2Btime&page=0&pagesize=100) in Python3 (PyPy).

## \_\_init\_\_

### Arguments

- `n: int`: number of nodes

## add_supply

Adds a supply of `amount` units to a node if `amount > 0` or a demand of `-amount` units if `amount < 0`.

### Arguments

- `v: int`: node
- `amount: int`: amount of supply

## add_edge

Appends an edge with capacity to the graph.

### Arguments

- `u: int`: from node
- `v: int`: to node
- `lower: int`: lower bound of flow
- `upper: int`: upper bound of flow
- `cost: int`: cost of flow

## solve

Finds the minimum cost of the b-flow.

### Returns

- `int | None`: the minimum cost of the b-flow if the b-flow is feasible, `None` otherwise

### Complexities

- $O(m^2 \log m \log U)$

where $m$ represents the number of edges and supplies added, and $U$ represents the maximum capacity (`upper - lower`) of the edges.

## edges

Returns the edges of the graph with flow that achieves the minimum cost.

Note: you must call `solve` before using this method.

### Returns

- `list[tuple[int, int, int]]`: list of edges with flow that achieves the minimum cost
  - Each element `(u, v, flow)` represents an edge from node `u` to node `v` with flow `flow`.