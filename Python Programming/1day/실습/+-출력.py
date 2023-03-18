n = int(input("몇 개를 출력할까요? "))
for i in range(n):
    if i % 2:
        print("-", end="")
    else:
        print("+", end="")

'''
n = int(input("몇 개를 출력할까요? "))
for i in range(n//2):
    print("+-", end="")
if n % 2:
    print("+", end="")
'''