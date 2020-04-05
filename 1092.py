# 풀이 1
from math import gcd

a, b, c = map(int, input().split())
  
def solution(arr):
    def lcm(x, y):
        return x*y // gcd(x, y)
      
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr)==1:
            return arr[0]
          

print(solution([a, b, c]))


# 풀이 2
a, b, c = map(int, input().split())

d=1
while (d%a!=0 or d%b!=0 or d%c!=0):
    d+=1

print(d)