# 문자열의 끝에 있는 문자들을 간편하게 제거할 수 있다
txt='.Hello.world.'

print(txt.rstrip('.')) # 오른쪽 끝 글자 제거
print(txt.lstrip('.')) # 왼쪽 끝 글자 제거
print(txt.strip('.')) # 양쪽 끝 문자 모두 제거