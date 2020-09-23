# 풀이 1
a, b = map(int, input().split())
a = int(bool(a))
b = int(bool(b))
print(int(a!=b))

# 풀이 2
a, b = map(int, input().split())

def xor(a, b):
    if a!=b:
        return 1
    else:
        return 0
print(xor(a, b))

# 풀이 3
a, b = map(int, input().split())
b1 = bool(a)
b2 = bool(b)
xor = int((b1==True and b2==False) or (b1==False and b2==True))
print(xor)