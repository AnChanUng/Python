T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    seen_digits = set()  # 현재까지 보았던 숫자들을 저장하는 집합
    count = 0

    while len(seen_digits) < 10:  # 길이가 10 미만인 동안 반복
        count += 1
        current_number = N * count  # 양의 번호

        for digit in str(current_number):  # 각 자릿수를 seen_digits에 추가
            seen_digits.add(int(digit))

    print('#{} {}'.format(test_case, N * count))
