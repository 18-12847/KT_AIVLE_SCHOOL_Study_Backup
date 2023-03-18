def solution(left, right):
    tot = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, int(i ** 0.5) + 1):
            if j ** 2 == i:
                cnt += 1
            elif i % j == 0:
                cnt += 2
        if cnt % 2:
            tot -= i
        else:
            tot += i
    return tot