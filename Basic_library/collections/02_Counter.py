# collections 라이브러리 활용 2
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장하는 횟수
print(counter['green']) # 'green'가 등장하는 횟수
print(dict(counter) # Counter 클래스를 dict로 변환
