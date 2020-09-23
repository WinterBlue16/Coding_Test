# 풀이 1
a = int(input())
def b(a):
    if a==1:
        return 0
    else:
        return 1
    
print(b(a))

# 풀이 2
a = int(input())

def torf(a):
    if a!=0:
        return 0
    elif a!=1:
        return 1
print(torf(a))

# 풀이 3
a = int(input())
b = bool(a)

print(int(not b))