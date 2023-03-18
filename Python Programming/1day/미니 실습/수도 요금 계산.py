def waterPay(n, m):
    if n.lower() == "a":
        m *= 100
    else:
        if m > 50:
            m = (m - 50) * 75 + 150 * 50
        else:
            m *= 150
    return print(f"{n} : {m}원")

a, b = input().split()
waterPay(a, int(b))