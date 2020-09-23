# 풀이 1
a, b = map(int, input().split())
for i in range(1, a+1): 
    for j in range(1, b+1):
        print(i, j)
        
# 풀이 2
import itertools

a, b = map(int, input().split())
X = []
Y = []
for i in range(1, a+1):
    X.append(i)
for i in range(1, b+1):
    Y.append(i)

lisum=[X, Y]
result=list(itertools.product(*lisum))
for i in range(len(result)):
    v = list(result[i])
    for i in range(len(v)):
        print(v[i], end=' ')
    print(' ')
