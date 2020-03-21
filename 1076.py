# 풀이 1
from string import ascii_lowercase

a = input()
li = list(ascii_lowercase)
idx = li.index(a)
li = li[:idx+1]
for i in li:
    print(i, end=' ')
 
    
# 풀이 2
from string import ascii_lowercase

a = input()
alpha_list = list(ascii_lowercase)

li=[]
li.append(a)

for i in alpha_list:
    if i!=a:
        li.append(i)
    else:
        break

li.sort(reverse=False)
for i in li:
    print(i, end=' ')


# 풀이 3
a = ord(input())
x = ord('a')

while x<=a:
    print(chr(x), end=' ')
    x+=1
    

    