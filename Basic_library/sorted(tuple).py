# sorted 함수를 활용해 튜플의 값 하나를 기준으로 오름차순/내림차순 정렬

# 숫자를 기준으로 오름차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x : x[1])
print(result)

# 숫자를 기준으로 내림차순 정렬
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key=lambda x : x[1], reverse=True)
print(result)
