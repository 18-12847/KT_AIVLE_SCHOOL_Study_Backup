import sys
a, b = map(int, sys.stdin.readline().split())
ans = list(map(int, sys.stdin.readline().split()))
print(*[i for i in ans if i < b])