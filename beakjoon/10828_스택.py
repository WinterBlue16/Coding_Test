import sys

n=int(sys.stdin.readline())
stack=[]
commend=[sys.stdin.readline().split() for i in range(n)]

for i in range(n):
    if commend[i][0]=='push':
        stack.append(commend[i][-1])
    elif commend[i][0]=='pop':
        print(-1 if not stack else stack.pop())
    elif commend[i][0]=='size':
        print(len(stack))
    elif commend[i][0]=='empty':
        print(1 if not stack else 0)
    else:
        print(-1 if not stack else stack[-1])