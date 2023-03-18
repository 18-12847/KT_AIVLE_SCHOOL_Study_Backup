def solution(a, b):
    ans = []
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans.append(i)
    print(max(ans))

n, m = map(int, input().split())
solution(n, m)

'''
#a >= b
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

#a >= b
def gcd(a, b):
    while b != 0 :
	    a, b = b, a % b
'''