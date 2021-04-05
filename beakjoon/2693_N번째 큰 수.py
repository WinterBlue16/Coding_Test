import sys

def solution(t, data):
    for i in range(t):
        array=sorted(data[i], reverse=True)
        print(array[2])
    
if __name__=='__main__':
    t=int(input())
    data=[list(map(int, sys.stdin.readline().split())) for _ in range(t)]
    solution(t, data)

