def solution(lottos, win_nums):
    cnt = 0
    if sorted(lottos) == sorted(win_nums):
        return [1, 1]
    for i in win_nums:
        if i in lottos:
            cnt += 1
    if lottos.count(0) == 0 and cnt == 0:
        return [6, 6]
    elif lottos.count(0) == 6:
        return [1, 6]
    for i in range(6):
        if lottos.count(0) == i:
            return [6 - lottos.count(0) - cnt + 1, 6 - cnt + 1]