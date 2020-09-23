# 프로그래머스 코딩테스트 문제_완주하지 못한 선수

from collections import Counter

def solution(participant, completion):
    if len(participant) != len(set(participant)):
        value = Counter(participant).most_common(n=1)
        answer = value[0][0]

        return answer

    else:
        for j in participant:
            if j not in completion:
                return j
