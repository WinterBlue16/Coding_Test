# itertools 라이브러리 활용 2
from itertools import combinations

data = ['A', 'B', 'C'] # 데이터 준비

result = list(combinations(data, 2)) # 데이터에서 2개를 뽑는 모든 조합 구하기
print(result) 