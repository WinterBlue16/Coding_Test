import sys

k=int(input())
cash=[]

for i in range(k):
    c=int(sys.stdin.readline().rstrip())
    if c!=0:
        cash.append(c)
    else:
        cash.pop()

print(sum(cash))