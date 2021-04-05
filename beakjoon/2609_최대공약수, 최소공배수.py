from math import gcd


def solution(n, m):
    num_gcd=gcd(n, m) # 최대공약수
    num_lcm=(n//num_gcd)*(m//num_gcd)*num_gcd # 최소공배수

    return num_gcd, num_lcm

if __name__=='__main__':
    x,y=map(int, input().split())
    answer=solution(x,y)
    for a in answer:
        print(a)