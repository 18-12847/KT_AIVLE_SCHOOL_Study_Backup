n = int(input("숫자를 입력하세요. : "))
flag = False
for i in range(2, 6):
    if n ** (1 / i) == int(n ** (1 / i)):
        print(f"{int(n ** (1 / i))} ** {i} = {n}입니다.")
        flag = True
if not flag:
    print("없음")