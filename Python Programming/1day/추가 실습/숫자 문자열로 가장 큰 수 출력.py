data = input('숫자로 이루어진 문자열을 입력하세요. ')
data = sorted(list(map(int, data)))
tot = 1
for i in range(len(data)):
    if data[i]:
        tot *= data[i]
        if i == len(data) - 1:
            print(f"{data[i]} ", end = "")
        else:
            print(f"{data[i]} * ", end = "")
    else:
        print(f"{data[i]} + ", end = "")
print(f"= {tot}")

#숫자로 이루어진 문자열을 입력하세요. 02984
#0 + 2 x 9 x 8 x 4 = 576