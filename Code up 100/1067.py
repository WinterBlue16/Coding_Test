# 풀이 1
a = int(input())
if a > 0:
    print('plus')
else:
    print('minus')
    
    if a%2==0:
        print('even')
    else:
        print('odd')

# 풀이 2
a = int(input())

def mp(a):
    if a > 0:
        return 'plus'
    else:
        return 'minus'

def oe(a):
    if a%2 == 0:
        return 'even'
    else:
        return 'odd'

print(mp(a), oe(a), sep='\n')
