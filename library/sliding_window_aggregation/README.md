# Sliding Window Aggregation

Deque-based data structure that holds the product of semi-group operations.

## \_\_init\_\_

### Arguments
- `dot: Callable[[T, T], T]`: binary operator corresponding to the semi-group operator.

## \_\_getitem\_\_

Returns the `i`-th element of the deque.

### Arguments
- `i: int`: index

### Returns
- `T`: value at index `i`

### Complexities
- $O(1)$

## append

Appends a value to the right end of the deque.

### Arguments
- `val: T`: value to append

### Complexities
- $O(1)$

## appendleft

Appends a value to the left end of the deque.

### Arguments
- `val: T`: value to append

### Complexities
- $O(1)$

## pop

Removes the rightmost element of the deque.

### Returns
- `T`: value at the rightmost element

### Complexities
- $\text{amortized } O(1)$

## popleft

Removes the leftmost element of the deque.

### Returns
- `T`: value at the leftmost element

### Complexities
- $\text{amortized } O(1)$

## prod

Returns the product of all elements in the deque.

### Returns
- `T`: product of all elements

### Complexities
- $O(1)$