# 풀이 1
a = int(input())
for i in range(1, a+1):
    if i%3!=0:
        print(i, end=' ')
    else:
        print('X', end=' ')
    