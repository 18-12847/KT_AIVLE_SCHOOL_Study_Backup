#for문
def lin_search(a, key):
	for i in range(len(a)):
		if a[i] == key:
			return i
	return -1

a = [2, 5, 1, 3, 9, 6, 7]
idx = lin_search(a, 3)
if idx == -1:
    print("검색 실패")
else:
    print(f"검색값은 a[{idx}]에 위치")

'''
#while문
def lin_search(a, key):
    i = 0
    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1   
        
a = [2, 5, 1, 3, 9, 6, 7]
idx = lin_search(a, 3)
if idx == -1:
    print("검색 실패")
else:
    print(f"검색값은 a[{idx}]에 위치")

#while문 보초법
def seq_search_sentinel(b, key):
    a = b.copy()
    a.append(key)
    i, cnt = 0, 0
    while True:
        cnt += 1
        if a[i] == key:
            print(cnt)
            break
        i += 1
    return -1 if i == len(b) else i

a = [2, 5, 1, 3, 9, 6, 7]
index = seq_search_sentinel(a, 7)
if index == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다.')
else:
    print(f'검색값은 a[{index}]에 있습니다.')
'''