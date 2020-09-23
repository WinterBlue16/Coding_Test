# 풀이 1
a, b = map(int, input().split())
print(a+b, a-b, a*b, a//b, a%b, '%.2f'%(a/b), sep='\n')

# 풀이 2
a, b = input().split()
a = int(a)
b = int(b)
print(a+b, a-b, a*b, a//b, a%b, '%.2f'%(a/b), sep='\n')
