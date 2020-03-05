# 풀이 1
a, b, c = input().split('.')
print("%04d"%int(a), "%02d"%int(b), "%02d"%int(c), sep='.')

# 풀이 2
a, b, c = input().split('.')

def ex1(a):
    x = int(a)
    if x < 1000:
        return str(x).zfill(4)
    else:
        return x 
def ex2(b):
    y = int(b)
    if y < 10:
        return str(y).zfill(2)
    else:
        return y

print(ex1(a), ex2(b), ex2(c), sep=".")

# 풀이 3
a, b, c = input().split('.')
print("%04d"%int(a), end='.')
print("%02d"%int(b), end='.')
print("%02d"%int(c))    
    
    