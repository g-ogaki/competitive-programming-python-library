class SegmentTree(object):
    def __init__(self, A, dot, e):
        n = len(A)
        tree = [e] * n + A
        for i in range(n - 1, 0, -1):
            tree[i] = dot(tree[i << 1], tree[i << 1 | 1])
        self._n, self._tree, self._dot, self._e = n, tree, dot, e

    def __getitem__(self, i):
        return self._tree[i + self._n]

    def __setitem__(self, i, v):
        i += self._n
        self._tree[i] = v
        while i != 1:
            i >>= 1
            self._tree[i] = self._dot(self._tree[i << 1], self._tree[i << 1 | 1])
    
    def __repr__(self):
        return str(self._tree[self._n:])

    def prod(self, l, r):
        l += self._n
        r += self._n
        lv = rv = self._e
        while l < r:
            if l & 1:
                lv = self._dot(lv, self._tree[l])
                l += 1
            if r & 1:
                r -= 1
                rv = self._dot(self._tree[r], rv)
            l >>= 1
            r >>= 1
        return self._dot(lv, rv)

    def bisect_left(self, l, v):
        l += self._n
        r = 0
        w = 1
        l_val = self._e
        while r + w <= self._n:
            if l & 1:
                if self._dot(l_val, self._tree[l]) < v:
                    l_val = self._dot(l_val, self._tree[l])
                    l += 1
                    r += w
                else:
                    break
            l >>= 1
            w <<= 1
        while w:
            if r + w <= self._n and self._dot(l_val, self._tree[l]) < v:
                l_val = self._dot(l_val, self._tree[l])
                l += 1
                r += w
            l <<= 1
            w >>= 1
        return r

if __name__ == "__main__":
    from operator import add
    A = [1, 2, 3, 4, 5]
    tree = SegmentTree(A, add, 0)
    print(tree.prod(1, 3))
    tree[1] = 10
    print(tree.prod(1, 3))
    print(tree.bisect_left(0, 6))