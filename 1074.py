# 풀이 1
a = int(input())
while a > 1:
    print(a-1)
    a-=1
    
# # 풀이 2
a = int(input())
li = list(range(a+1))
li.sort(reverse=True)

print(li[0])
for i in li:
    if i!=1:
        y=i-1
        print(y)
    else:
        break