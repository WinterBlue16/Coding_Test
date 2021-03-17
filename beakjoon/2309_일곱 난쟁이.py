import sys
from itertools import combinations

def solution(num_li):
    for a in list(combinations(num_li, 7)):
        if sum(a)==100:
            return a

if __name__=='__main__':
    num_li=[int(sys.stdin.readline()) for i in range(9)]
    answer=sorted(solution(num_li))
    for a in answer:
        print(a)
