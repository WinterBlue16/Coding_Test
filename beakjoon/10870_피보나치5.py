# 재귀함수를 이용한 피보나치 수열
def p(n):
    if n <= 1:
        return n
    else:
        return p(n-1)+p(n-2)

if __name__=='__main__':
    n=int(input())
    print(p(n))
