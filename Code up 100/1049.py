# 풀이 1
a, b = map(int, input().split())
if a > b:
    print(1)
else:
    print(0)
    
# 풀이 2
a, b = input().split()
a = int(a)
b = int(b)

def plusminus(a, b):
    if a > b:
        return 1
    else:
        return 0
print(plusminus(a, b))

# 풀이 3
a, b = map(int, input().split())
print(int(a > b))


# 두 변수에 >만 사용해 비교했을 경우 output은 1, 0이 아니라 True, False 값만 나온다.
# 때문에 int()를 씌워주어 숫자로 변환해야 한다.