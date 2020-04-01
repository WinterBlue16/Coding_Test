# 풀이 1
a = int(input())
li = []
for i in range(1, a+1):
    li.append(i)
    if sum(li) >= a:
        print(sum(li))
        break
        
        
    
# 풀이 2 
a = int(input())
s=0
for i in range(1, a+1):    
    s+=i    
    if s >= a:
        print(s)
        break