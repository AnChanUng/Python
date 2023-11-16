month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
         7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}  # 각 달의 일수를 나타내는 딕셔러니
T = int(input())

for test_case in range(1, T+1):

    change = 1  # 날짜의 차이를 나타내는 변수
    m1, d1, m2, d2 = list(map(int, input().split()))
    if m1 == m2:
        change += d2 - d1
    else:
        for i in range(m1, m2):  # 시작 월부터 끝 월까지 반복
            change += month[i]  # 각 월의 일 수를 더함
        change += d2 - d1  # 나머지 일 수를 더함
    print(f'#{test_case} {change}')
