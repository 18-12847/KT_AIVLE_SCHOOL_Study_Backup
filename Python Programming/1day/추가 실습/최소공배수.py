def solution(a, b):
    ans = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans.append(i)
    return max(ans)

n, m = map(int, input().split())
gcd = solution(n, m)
print(f"{n}, {m}의 최소공배수 : {gcd * n // gcd * m // gcd}")