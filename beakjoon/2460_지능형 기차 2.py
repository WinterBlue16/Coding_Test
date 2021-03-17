import sys

def solution(data):
    p_count=[]
    answer=0
    for i in range(10):
        answer=answer-data[i][0]+data[i][1]
        p_count.append(answer)

    return max(p_count)

if __name__=='__main__':
    train_data=[list(map(int, sys.stdin.readline().split())) for i in range(10)]
    print(solution(train_data))
