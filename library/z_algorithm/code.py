def z_algorithm(S):
    n = len(S)
    res = [0] * n
    res[0] = n
    l = r = 0
    for i in range(1, n):
        if res[i - l] < r - i:
            res[i] = res[i - l]
        else:
            l = i
            r = max(i, r)
            while r < n and S[r - l] == S[r]:
                r += 1
            res[i] = r - l
    return res

if __name__ == "__main__":
    S = "abracadabra"
    print(z_algorithm(S))