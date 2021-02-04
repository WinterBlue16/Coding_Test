# itertools 라이브러리 활용 3
from itertools import product

data = ['A', 'B', 'C'] # 데이터 준비

result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(값, 순서 중복 허용 ex.'A','A','A') # permutations과의 차이점
print(result)