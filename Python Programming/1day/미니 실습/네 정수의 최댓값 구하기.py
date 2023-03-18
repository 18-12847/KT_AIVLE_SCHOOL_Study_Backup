def max4(a, b, c, d):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    if d > maximum:
        maximum = d
    return maximum

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))
print(f"maximum : {max4(a, b, c, d)}")

# ans = list(map(int, input().split()))
# print(max(ans))