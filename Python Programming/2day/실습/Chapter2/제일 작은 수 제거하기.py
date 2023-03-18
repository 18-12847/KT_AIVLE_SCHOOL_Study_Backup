def solution(arr):
    arr.remove(min(arr))
    return [-1] if len(arr) == 0 else arr

arr = [4, 3, 2, 1]
print(solution(arr))