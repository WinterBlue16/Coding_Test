def solution(num):
    return min(num), max(num)

if __name__=='__main__':
    n=int(input())
    num=list(map(int, input().split()))
    for a in solution(num):
        print(a, end=' ')