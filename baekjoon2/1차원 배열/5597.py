
submitted_numbers = set()  # 출석번호를 입력받아 저장
for _ in range(28):
    submitted_numbers.add(int(input()))

all_numbers = set(range(1, 31))  # 모든 학생 출석번호 집합을 생성

missing_numbers = all_numbers - submitted_numbers  # 찾은 출석번호를 정렬하여 출력

missing_numbers = sorted(list(missing_numbers))
print(missing_numbers[0])
print(missing_numbers[1])
