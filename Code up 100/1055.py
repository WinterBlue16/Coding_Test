# 풀이 1
a, b = map(int, input().split())
a = int(bool(a))
b = int(bool(b))
print(a or b)

# 풀이 2
a, b = map(int, input().split())

def torf(a, b):
    if a==1 or b==1:
        return 1
    else:
        return 0

print(torf(a, b))