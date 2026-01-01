# Fast Fourier Transform

Calculates the convolution of two polynomials.

Given two arrays $A_0, \cdots, A_{n-1}$ and $B_0, \cdots, B_{m-1}$ representing $f(x) = \displaystyle \sum_{i=0}^{n-1} A_i x^i$ and $g(x) = \displaystyle \sum_{i=0}^{m-1} B_i x^i$ respectively, the convolution
$f(x)g(x) = \displaystyle \sum_{i=0}^{n+m-2} C_i x^i$
is defined as $C_k = \displaystyle \sum_{i=0}^{k} A_i B_{k-i}$.

## convolve

### Arguments

- `f: list[complex]`: first array of coefficients of the polynomial $f(x)$
- `g: list[complex]`: second array of coefficients of the polynomial $g(x)$

### Returns

- `list[complex]`: array of coefficients of the polynomial $f(x)g(x)$

### Complexities

- time: $O((n + m) \log (n + m))$
- space: $O(n + m)$