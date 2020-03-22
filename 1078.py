# 풀이 1
a = int(input())
li=[]
for i in range(a+1):
    if i%2==0:
        li.append(i)

print(sum(li))

# 풀이 2
a = int(input())
li=list(range(a+1))
li_2=[]
for i in li:
    if i%2==0:
        li_2.append(i)

print(sum(li_2))

# 풀이 3
a = int(input())
x = 0
for i in range(1, x+1):
    if i%2==0:
        x+=i
print(x)