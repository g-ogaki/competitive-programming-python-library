# Chinese Remainder Theorem

Solves the system of congruences:

$$
\begin{aligned}
x &\equiv R_0 \pmod{M_0} \\
x &\equiv R_1 \pmod{M_1} \\
&\vdots \\
x &\equiv R_{n-1} \pmod{M_{n-1}}
\end{aligned}
$$

given two arrays $R$ and $M$ of length $n$.

## crt

### Arguments

- `R: list[int]`: array of remainders
- `M: list[int]`: array of moduli
- `MOD: int = 0`: (optional) modulo for the solution

### Returns

- `int`: minimum non-negative solution $x$ (or $x \mod{\text{MOD}}$ if specified) to the system of congruences, or `-1` if no solution exists

### Complexities

- $O(n \log \text{lcm}(M))$   