from collections import deque

def solution(priorities, location):
    sample=[0]*len(priorities)
    sample[location]=1
    q=deque(priorities)
    q2=deque(sample)
    count=0
    
    while sum(q2)!=0: # 핵심 # len(set(q2))!=1 # 이렇게 했을 때는 3개 틀림
        print(q2)
        if q[0]!=max(q):
            q.append(q[0])
            q2.append(q2[0])
            q.popleft()
            q2.popleft()
        else:
            q.popleft()
            q2.popleft()
            count+=1

    return count

# 처음엔 dictionary를 쓰려고 했으나 안됨(중복 key는 class를 따로 설정하지 않으면 자동으로 제거)


# 원래 풀려고 했던 코드
# from collections import deque
# import numpy as np
# import sys

# def solution(priorities, location):
#     x=priorities[location] # 출력할 문서의 중요도
#     sort_priorities=sorted(priorities, reverse=True) # 내림차순으로 정렬
#     idx=sort_priorities.index(x) # 중요도 순으로 정렬 시 x의 인덱스
#     priorities_arr=np.array(priorities)
#     stand_idx_li=np.where(priorities_arr==(sort_priorities[idx-1]))[0] # x보다 큰 수 중 가장 작은 수의 인덱스 
#     counts=priorities.count(x) # 중요도 중복 카운트
    
#     if counts==1: # 중요도가 같은 문서가 1개일 경우
#         return idx+1
    
#     else: # 중요도가 같은 문서가 다수일 경우
#         idx_li=np.where(priorities_arr==x)[0] # 중요도 x인 문서들의 모든 인덱스
#         idx_queue=deque(idx_li) # 큐로 변경
        
#         if any(ix > stand_idx_li[-1] for ix in idx_queue)==True: 
#                 while idx_queue[0] < stand_idx_li[-1]: 
#                     idx_queue.append(idx_queue[0])
#                     idx_queue.popleft()
#                 answer=len(sort_priorities[:idx])+idx_queue.index(location)+1
#                 return answer
    
#         else: # idx_li의 모든 idx가 stand idx보다 작을 경우
#             answer=len(sort_priorities[:idx])+idx_queue.index(location)+1
#             return answer
        
        
# n=int(input())
# answer=[]
# for i in range(n):
#     x,y=map(int, sys.stdin.readline().split())
#     case=list(map(int, sys.stdin.readline().split()))
#     answer.append(solution(case, y))

# for a in answer:
#     print(a)