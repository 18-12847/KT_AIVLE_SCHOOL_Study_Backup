def prime():
    ans = [False, False] + [True] * 999
    for i in range(2, int(1000 ** 0.5) + 1):
        for j in range(i * 2, len(ans), i):
            ans[j] = False
    print([idx for idx, val in enumerate(ans) if val])

prime()