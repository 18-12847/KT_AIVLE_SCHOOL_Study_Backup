#선형 탐색
def linear_search(lst, key):
    for idx, value in enumerate(lst):
        if key == value:
            print(f"index : {idx}")
        elif idx == len(lst) - 1:
            print("없음")

lst = list(map(int, input().split()))
print(f"lst : {lst}")
key = int(input())
print(f"key : {key}")
linear_search(lst, key)