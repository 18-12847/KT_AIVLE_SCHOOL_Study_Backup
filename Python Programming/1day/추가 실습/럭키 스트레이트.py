import sys
n = sys.stdin.readline().rstrip()
print("LUCKY") if sum(list(map(int, n[:len(n)//2]))) == sum(list(map(int, n[len(n)//2:]))) else print("READY")