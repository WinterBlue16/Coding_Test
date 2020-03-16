# 풀이 1
a, b = map(int, input().split())
print(a^b)

# 풀이 2
a, b = map(int, input().split())
x = int(bin(a), 2)
y = int(bin(b), 2)
xy = bin(x^y)
print(int(xy, 2))