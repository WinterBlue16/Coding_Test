# 풀이 1
a, b, c = map(int, input().split())
li = []
for i in range(c):
    answer = a*(b**i)
    li.append(answer)

print(li[c-1])

# 풀이 2
a, b, c = map(int, input().split())
for i in range(c-1):
    a = a*b
    
print(a)