# Number Theoretic Transform

Calculates the convolution of two polynomials modulo a prime number $p$ where $p$ must be NTT-friendly (mostly $p = 998244353$).

Given two arrays $A_0, \cdots, A_{n-1}$ and $B_0, \cdots, B_{m-1}$ representing $f(x) = \displaystyle \sum_{i=0}^{n-1} A_i x^i$ and $g(x) = \displaystyle \sum_{i=0}^{m-1} B_i x^i$ respectively, the convolution
$f(x)g(x) = \displaystyle \sum_{i=0}^{n+m-2} C_i x^i$
is defined as $C_k = \displaystyle \sum_{i=0}^{k} A_i B_{k-i} \mod p$.

## convolve

### Arguments

- `f: list[int]`: The first array of coefficients of the polynomial $f(x)$.
- `g: list[int]`: The second array of coefficients of the polynomial $g(x)$.

### Returns

- `list[int]`: The array of coefficients of the polynomial $f(x)g(x)$ modulo $p$.

### Complexities

- Time: $O((n + m) \log (n + m))$
- Space: $O(n + m)$