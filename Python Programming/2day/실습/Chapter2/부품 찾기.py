def solution(store, customer):
    ans = []
    for i in customer:
        if i in store:
            ans.append("yes")
        else:
            ans.append("no")
    return ans

store = [2,3,7,8,9]
customer = [7,5,9]
print(solution(store, customer))