print('a부터 b까지 정수의 합을 구합니다.')
a, b = map(int, input('정수 a를 입력하세요.: ').split())
if a > b:
    a, b = b, a    
tot = 0
for i in range(a, b + 1):
    if i < b:
        print(f'{i} + ', end='')
    tot += i
print(f'{i} = {tot}', end='')