# 풀이 1
num = map(int, input().split())
num = list(num)
for i in num:
    if i != 0:
        print(i)
    else:
        break
    
# 풀이 2
a = input().split()

for i in a:
    if int(i)==0:
        break
    else:
        print(i)