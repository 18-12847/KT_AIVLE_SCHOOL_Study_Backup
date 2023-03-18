a = [2, 5, 1, 3, 9, 6, 7]
•왼쪽 원소 인덱스 i와 오른쪽 원소의 인덱스 n - i - 1을 교환

def reverse_list(a):
	n = len(a)
	for i in range(n // 2):
		a[i], a[n-i-1] = a[n-i-1], a[i]

'''
def reverse_list(a):
    n = len(a)
    for i in range(n // 2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
    return a

print("리스트를 역순으로 출력합니다.")
n = int(input("원소 수를 입력하세요.: "))
x = [int(input(f"x[{i}] 값을 입력하세요.: ")) for i in range(n)]
print("리스트를 역순으로 출력합니다.")
reverse_list(x)
for idx, val in enumerate(x):
    print(f"x[{idx}] = {val}")
'''