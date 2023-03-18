def solution(arr):
    answer = []
    arr.reverse()
    i = 0
    while len(arr):
        answer.append(arr.pop())
        while len(arr) > 0 and answer[i] == arr[-1]:
            arr.pop()
        i += 1
    return answer