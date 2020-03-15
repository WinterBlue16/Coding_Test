# 풀이 1
a, b = map(int, input().split())
print(int(a==b))

# 풀이 2
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print(int(int(a)==int(b)))

# 풀이 3
a, b = map(int, input().split())

def both(a, b):
    if (a==1 and b==1) or (a==0 and b==0):
        return 1
    else:
        return 0

print(both(a, b))
