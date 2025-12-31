class LinkCutTree(object):
    def __init__(self, A, dot, e, compose, id, act):
        n = len(A)
        self._left = [-1] * n
        self._right = [-1] * n
        self._parent = [-1] * n
        self._value = A[:]
        self._size = [1] * n
        self._prod = A[:]
        self._reverse = [False] * n
        self._lazy = [id] * n
        self._dot, self._e, self._compose, self._id, self._act = dot, e, compose, id, act
    
    def _push(self, v):
        left, right = self._left, self._right
        if self._lazy[v] != self._id:
            lazy, compose, act = self._lazy, self._compose, self._act
            self._value[v] = act(lazy[v], self._value[v], 1)
            self._prod[v] = act(lazy[v], self._prod[v], self._size[v])
            if left[v] != -1:
                lazy[left[v]] = compose(lazy[left[v]], lazy[v])
            if right[v] != -1:
                lazy[right[v]] = compose(lazy[right[v]], lazy[v])
            lazy[v] = self._id
        if self._reverse[v]:
            reverse = self._reverse
            left[v], right[v] = right[v], left[v]
            if left[v] != -1:
                reverse[left[v]] ^= True
            if right[v] != -1:
                reverse[right[v]] ^= True
            reverse[v] = False
            return True
        return False
    
    def _update(self, v):
        left, right, size, prod = self._left, self._right, self._size, self._prod
        size[v] = 1
        prod[v] = self._value[v]
        if left[v] != -1:
            self._push(left[v])
            size[v] += size[left[v]]
            prod[v] = self._dot(prod[left[v]], prod[v])
        if right[v] != -1:
            self._push(right[v])
            size[v] += size[right[v]]
            prod[v] = self._dot(prod[v], prod[right[v]])
    
    def _rotate(self, v, p, d):
        left, right, parent = self._left, self._right, self._parent
        if d:
            left[p] = right[v]
            if right[v] != -1:
                parent[right[v]] = p
            right[v], parent[p] = p, v
        else:
            right[p] = left[v]
            if left[v] != -1:
                parent[left[v]] = p
            left[v], parent[p] = p, v
        self._update(p)
    
    def _splay(self, v):
        left, right, parent = self._left, self._right, self._parent
        push, rotate = self._push, self._rotate
        path, direction = [], []
        u = v
        while True:
            p = parent[u]
            if p == -1 or left[p] != u != right[p]:
                parent[v] = p
                break
            path.append(p)
            direction.append(u == left[p])
            u = p
        path.reverse()
        direction = [d ^ push(u) for u, d in zip(path, direction[::-1])]
        push(v)
        while len(path) >= 2:
            p, g = path.pop(), path.pop()
            dp, dg = direction.pop(), direction.pop()
            if dp == dg:
                rotate(p, g, dg)
                rotate(v, p, dp)
            else:
                rotate(v, p, dp)
                rotate(v, g, dg)
        if path:
            p = path.pop()
            d = direction.pop()
            rotate(v, p, d)

    def _expose(self, v):
        right, parent, splay = self._right, self._parent, self._splay
        prev, cur = -1, v
        while cur != -1:
            splay(cur)
            right[cur] = prev
            prev, cur = cur, parent[cur]
        splay(v)
        self._update(v)
        return prev
    
    def evert(self, v):
        self._expose(v)
        self._reverse[v] ^= True
    
    def lca(self, u, v):
        self._expose(u)
        return self._expose(v)
    
    def link(self, u, v):
        self.evert(u)
        self._parent[u] = v
    
    def cut(self, v):
        self._expose(v)
        self._parent[self._left[v]] = -1
        self._left[v] = -1
        self._update(v)
    
    def is_connected(self, u, v):
        if u == v:
            return True
        self._expose(u)
        self._expose(v)
        return self._parent[u] != -1
    
    def depth(self, v):
        self._expose(v)
        return self._size[v] - 1
    
    def act(self, u, v, f):
        self.evert(u)
        self._expose(v)
        self._lazy[v] = self._compose(self._lazy[v], f) 
    
    def prod(self, u, v):
        self.evert(u)
        self._expose(v)
        return self._prod[v]

if __name__ == "__main__":
    from operator import add

    A = [0, 1, 2, 3, 4]
    act = lambda f, x, size: x + f * size
    lct = LinkCutTree(A, add, 0, add, 0, act)
    lct.link(0, 1)
    lct.link(1, 2)
    print(lct.prod(0, 2))
    lct.act(0, 1, 10)
    print(lct.prod(0, 2))
    print(lct.is_connected(0, 2))
    print(lct.is_connected(0, 3))
    lct.cut(2)
    print(lct.is_connected(0, 2))