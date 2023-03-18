import sys
n = int(sys.stdin.readline())
cnt, tmp = 0, n
while True:
    tmp = tmp % 10 * 10 + (tmp // 10 + tmp % 10) % 10 
    cnt += 1
    if n == tmp:
        break
print(cnt)