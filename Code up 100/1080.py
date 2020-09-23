# 풀이 1
a = int(input())

s=0
for i in range(1, a+1):    
    s+=i
    if s >= a:
        print(i)
        break
        
# 풀이 2
a = int(input())

li = []
for i in range(a):
    li.append(i)
    b = sum(li)
    if b >= a:
        print(i)
        break
    
# 풀이 3
a = int(input())

i = 0
s = 0
while s < a:
    i+=1
    s+=i
    
print(i)