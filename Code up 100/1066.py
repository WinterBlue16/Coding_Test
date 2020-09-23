# 풀이 1
data = map(int, input().split())

for i in data:
    if i%2==0:
        print('even')
    else:
        print('odd')
    
# 풀이 2
a, b, c = map(int, input().split())

def oe(x):
    if x%2 ==0:
        return 'even'
    else:
        return 'odd'
        
print(oe(a), oe(b), oe(c), sep='\n')


