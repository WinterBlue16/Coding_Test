# 풀이 1
data = map(int, input().split())
for i in data:
    if i % 2 == 0:
        print(i)
        
# 풀이 2
data = map(int, input().split())
data = list(data)

s_list = []
for i in data:
    if i % 2==0:
        s_list.append(i)

for i in s_list:
    print(i)
