# 풀이 1
a = int(input())
print(~a)

# 풀이 2
a = int(input())
x = int(bin(a), 2)
x = bin(~x)
print(int(x,2))