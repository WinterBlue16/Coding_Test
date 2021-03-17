def solution(t, num):
    for n in num:
        answer=bin(n)[2:]
        count=0
        for a in answer[::-1]:
            if a=='1':
                count+=1
                print(count-1, end=' ')
            else:
                count+=1

if __name__=='__main__':
    t=int(input())
    n=[int(input()) for _ in range(t)]
    solution(t, n)