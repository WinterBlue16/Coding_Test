# bisect 라이브러리 활용 # 이진탐색
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value] 범위 내에 존재하는 데이터의 개수를 반환
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index-left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4)) # (4<=n) and (n<=4), 4보다 작거나 같고, 4보다 크거나 같은 값들의 수를 카운트한다

# 값이 [-1, 3](-1<=n<=3) 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))