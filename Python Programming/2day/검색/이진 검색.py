#while문
def binary_search(lst, key):
    lt, rt = 0, len(lst) - 1
    while lt <= rt:
        pt = (lt + rt) // 2
        if lst[pt] == key:
            return pt
        elif key > lst[pt]:
            lt = pt + 1
        else:
            rt = pt - 1
    return "없음"

lst = list(map(int, input().split()))
print(f"lst : {lst}")
key = int(input())
print(f"key : {key}")
print(f"index : {binary_search(lst, key)}")

'''
#재귀함수
def binary_search(array, target, start, end, cnt):
    cnt += 1
    if start > end:
        return "없음"
    mid = (start + end) // 2
    if array[mid] == target:
        print(f"실행 횟수 : {cnt}")
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1, cnt)
    else:
        return binary_search(array, target, mid + 1, end, cnt)

lst = list(map(int, input().split()))
print(f"lst : {lst}")
key = int(input())
print(f"key : {key}")
print(f"Index : {binary_search(lst, key, 0, len(lst) - 1, 0)}")
'''