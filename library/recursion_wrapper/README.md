# Recursion Wrapper

Wrapper function that makes recursive functions iterative using an explicit stack. This improves performance, as recursion in Python is notoriously slow.

In the recursive function, `yield` must be used to return the value of the recursive call instead of `return`, even though it doesn't return anything (returns `None`).

## bootstrap

### Arguments

- `cache: bool`: Whether to enable memoization.

### Returns

- `Callable`: The wrapped function.