class SWAG(object):
    def __init__(self, dot):
        self._front = []
        self._back = []
        self._dot = dot

    def __bool__(self):
        return bool(self._front) or bool(self._back)

    def __len__(self):
        return len(self._front) + len(self._back)

    def __getitem__(self, i):
        if i < 0:
            i += len(self)
        return self._front[~i][0] if i < len(self._front) else self._back[i - len(self._front)][0]

    def __repr__(self):
        return str([self[i] for i in range(len(self))])

    def append(self, val):
        prod = self._dot(self._back[-1][1], val) if self._back else val
        self._back.append((val, prod))
    
    def appendleft(self, val):
        prod = self._dot(val, self._front[-1][1]) if self._front else val
        self._front.append((val, prod))

    def _distribute(self):
        N = len(self._front)
        N2 = N - 1 >> 1
        prod = self._front[N2][0]
        self._back.append((prod, prod))
        for val, _ in self._front[:N2][::-1]:
            prod = self._dot(prod, val)
            self._back.append((val, prod))
        prod = self._front[N2 + 1][0]
        front = [(prod, prod)]
        for val, _ in self._front[N2 + 2:]:
            prod = self._dot(val, prod)
            front.append((val, prod))
        self._front = front

    def pop(self):
        if not self._back:
            if len(self._front) == 1:
                return self._front.pop()[0]
            self._distribute()
        return self._back.pop()[0]

    def popleft(self):
        if not self._front:
            if len(self._back) == 1:
                return self._back.pop()[0]
            self._back.reverse()
            self._front, self._back = self._back, self._front
            self._distribute()
        return self._front.pop()[0]

    def prod(self):
        if not self._back:
            return self._front[-1][1]
        elif not self._front:
            return self._back[-1][1]
        else:
            return self._dot(self._front[-1][1], self._back[-1][1])

if __name__ == "__main__":
    deque = SWAG(max)
    deque.appendleft(1)
    deque.append(2)
    print(deque.prod())
    deque.append(3)
    print(deque)
    print(deque.prod())
    deque.pop()
    print(deque[1])
    print(deque.prod())