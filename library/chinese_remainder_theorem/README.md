# Chinese Remainder Theorem

Solves the system of congruences:

$$
x \equiv R_0 \mod{M_0} \\
x \equiv R_1 \mod{M_1} \\
\vdots \\
x \equiv R_{n-1} \mod{M_{n-1}}
$$

given two arrays $R$ and $M$ of length $n$.

## Arguments

- `R: list[int]`: array of remainders
- `M: list[int]`: array of moduli
- `MOD: int`: (optional) modulo for the solution

## Returns

- `int`: minimum non-negative solution $x$ (or $x \mod{\text{MOD}}$ if specified) to the system of congruences

## Complexities

- $O(n \log \text{lcm}(M))$   