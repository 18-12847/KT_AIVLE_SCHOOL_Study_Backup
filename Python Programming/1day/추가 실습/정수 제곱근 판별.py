import math
def solution(n):
    return (int(n ** 0.5) + 1) ** 2 if math.ceil(n ** 0.5) ** 2 == float(n) else -1