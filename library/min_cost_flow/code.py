from heapq import heappop, heappush
INF = 1 << 60
class MinCostFlow(object):
    def __init__(self, n):
        self.n = n
        self.E = []
        self._E = []
        self._G = [[] for _ in range(n + 1)]
        self._b = [0] * (n + 1)
        self._u = 1

    def add_supply(self, v, amount):
        self.add_edge(self.n, v, amount, amount, 0, False)

    def add_edge(self, u, v, lower, upper, cost, append=True):
        e = [v, upper, cost, 0]
        rev = [u, -lower, -cost, e]
        e[-1] = rev
        self._G[u].append(e)
        self._G[v].append(rev)
        self._u = max(self._u, upper - lower)
        if not lower <= 0 <= upper:
            self._push(e, lower)
        if append:
            self._E.append((e, upper))

    def _push(self, e, f):
        rev = e[-1]
        self._b[rev[0]] -= f
        self._b[e[0]] += f
        e[1] -= f
        rev[1] += f

    def _saturate(self, delta):
        for v in range(self.n + 1):
            for e in self._G[v]:
                nv, cap, cost, _ = e
                if cap >= delta and cost + self._p[v] - self._p[nv] < 0:
                    self._push(e, cap)

    def _shortest_path(self, delta):
        n = self.n + 1
        dist = [INF] * n
        heap = []
        for v, b in enumerate(self._b):
            if b >= delta:
                dist[v] = 0
                heap.append(v)
        prev = [None] * n
        word = n.bit_length()
        mask = (1 << word) - 1
        while heap:
            v = heappop(heap)
            d, v = v >> word, v & mask
            if dist[v] != d:
                continue
            if self._b[v] <= -delta:
                t = v
                f = -self._b[v]
                while prev[v]:
                    f = min(f, prev[v][1])
                    v = prev[v][-1][0]
                f = min(f, self._b[v])
                while prev[t]:
                    self._push(prev[t], f)
                    t = prev[t][-1][0]
                for v in range(n):
                    self._p[v] += min(d, dist[v])
                return True
            for e in self._G[v]:
                nv, cap, cost, _ = e
                if cap < delta:
                    continue
                if dist[nv] > d + cost + self._p[v] - self._p[nv]:
                    prev[nv] = e
                    dist[nv] = d + cost + self._p[v] - self._p[nv]
                    heappush(heap, dist[nv] << word | nv)
        return False

    def solve(self):
        self._p = [0] * (self.n + 1)
        delta = 1 << (self._u - 1).bit_length()
        while delta:
            self._saturate(delta)
            while self._shortest_path(delta):
                pass
            delta >>= 1
        if any(self._b):
            return None
        f = 0
        for e, upper in self._E:
            nv, cap, cost, rev  = e
            v = rev[0]
            f += cost * (upper - cap)
            self.E.append((v, nv, upper - cap))
        return f
    
    @property
    def edges(self):
        return self.E

if __name__ == "__main__":
    mcf = MinCostFlow(3)

    mcf.add_supply(0, 2)
    mcf.add_supply(2, -2)

    mcf.add_edge(0, 1, 0, 5, 1)
    mcf.add_edge(1, 2, 0, 5, 1)
    mcf.add_edge(0, 2, 0, 5, 5)

    print(mcf.solve())
    print(mcf.edges)