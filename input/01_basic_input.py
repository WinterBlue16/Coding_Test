# 가장 보편적인 입력(input) 코드
# 문자열(str) 1개 입력
x = input()
print(x)

# 정수형(int) 1개 입력
n = int(input())
print(n)

# 실수형(float) 1개 입력
f = float(input())
print(f)

# 공백을 기준으로 다수 입력
# 문자열
x, y, z = input().split() 
print(x, y, z)
# 정수형, 실수형
x, y, z = map(int, input().split())
# print(x, y, z)
x, y, z = map(float, input().split())
# print(x, y, z)

# 공백을 기준으로 다수 입력, 리스트화
data = list(map(int, input().split()))
print(data)
print(data[0])