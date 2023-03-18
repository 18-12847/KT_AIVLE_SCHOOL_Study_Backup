def electricPay(n):
    if n > 200:
        print(f"전기요금은 {int(1.137 * (1600 + int(100 * 60.7) + int(100 * 125.9) + int((n - 200) * 187.9)))}원 입니다.")
    elif n >= 100:
        print(f"전기요금은 {int(1.137 * (910 + int(100 * 60.7) + int((n - 100) * 125.9)))}원 입니다.")
    else:
        print(f"전기요금은 {int(1.137 * (410 + int(n * 60.7)))}원 입니다.")
a = int(input("전기사용량을 입력하세요. : "))
electricPay(a)