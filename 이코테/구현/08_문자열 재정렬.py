data = input()
result = []
value = 0

# 문자열을 하나씩 확인
for x in data:
    if x.isalpha():  # 알파벳이면
        result.append(x)  # 리스트에 추가
    else:  # 아니면
        value += int(x)  # 숫자를 value 변수에 저장

result.sort()  # 리스트 오름정렬

if value != 0:  # value가 0이 아니면
    result.append(str(value))  # 리스트에 문자열 형태로 저장

print(''.join(result))  # 하나의 문자열로 반환 ex) ['a', 'b', 'c'] -> abc
