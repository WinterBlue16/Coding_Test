import sys

n=int(input())
x=[sys.stdin.readline().rstrip() for i in range(n)]
print(x[::-1])

# for i in range(n):
#     print('YES' if x[i].count('(')==x[i].count(')') else 'NO')
