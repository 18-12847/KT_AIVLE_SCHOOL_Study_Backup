def reverse_lst(lst):
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - i - 1] = lst[len(lst) - i - 1], lst[i]
    return lst

lst = list(map(int, input().split()))
print(lst)
print(reverse_lst(lst))