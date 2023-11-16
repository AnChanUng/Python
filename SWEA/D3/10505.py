T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    person = list(map(int, input().split()))
    count = 0

    avg = sum(person) / N  # 평균값

    for i in range(N):
        if person[i] <= avg:
            count += 1

    print(f'#{test_case} {count}')
