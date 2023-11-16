T = int(input())

for test_case in range(1, T+1):

    time, minute, time1, minute1 = map(int, input().split())

    total_minute = (minute + minute1) % 60  # 분의 합
    carry_hour = (minute + minute1) // 60  # 분의 합으로 넘어간 시간

    total_time = (time + time1 + carry_hour) % 12  # 시간의 합
    if total_time == 0:
        total_time = 12

    print(f'#{test_case} {total_time} {total_minute}')
