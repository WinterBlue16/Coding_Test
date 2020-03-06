# 풀이 1
a = int(input())
a = str(a)
def num(x):
    li=[]
    li.append(int(x[0])*10000)
    li.append(int(x[1])*1000)
    li.append(int(x[2])*100)
    li.append(int(x[3])*10)
    li.append(int(x[4])*1)
    return li

for i in num(a):
    print('['+str(i)+']')
    
# 풀이 2
a = input()
x = str(a)
for i in range(len(x)):
    b = [int(x[i])*10**(len(x)-(i+1))]
    print(b)
    
