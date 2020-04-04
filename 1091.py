# 풀이 1
a, b, c, d = map(int, input().split())

li=[]
li.append(a)

for i in range(d):    
    a = a*b+c
    li.append(a)

print(li[d-1])
    