import sys
area = int(sys.stdin.readline().rstrip())
for i in range(1, area + 1):
    if area % i:
        continue
    print(f"{i} * {area // i}")