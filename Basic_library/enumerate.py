# 리스트 정렬 시 처음의 위치를 기억하는 데 유용한 함수
# 샘플 리스트
x=[1,2,3,4,5]

# 리스트 내의 각 값에 고유 index를 부여한다((index, 기존값)의 형태)
for i, j in enumerate(x):
    print(i, j)

# 첫 번째 값은 index
for i, j in enumerate(x):
    print(i)

# 두 번째 값은 기존의 리스트 값
for i, j in enumerate(x):
    print(j)

# 두 개가 아니라 하나의 변수로도 출력 가능하다
for v in enumerate(x):
    print(type(v)) # type은 tuple!
    print(v) # index는 v[0], 리스트 값은 v[1]

