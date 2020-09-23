# 풀이 1
a, b = map(int, input().split())

def bothf(a, b):
    if a==0 and b==0:
        return 1
    else:
        return 0

print(bothf(a, b))

# 풀이 2
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print(int((not a) and (not b)))