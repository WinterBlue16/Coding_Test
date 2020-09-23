# 풀이 1
a = int(input())
while a > 0:
    print(a-1)
    a-=1
    
# 풀이 2
a = int(input())
li = list(range(a))
li.sort(reverse=True)

print(li[0])
for i in li:
    if i!=0:
        y=i-1
        print(y)
    else:
        break
