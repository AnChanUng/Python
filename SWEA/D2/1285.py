T = int(input())

for test_case in range(1, T+1):

    N = int(input())  # 돌을 던지는 사람의 수
    dol = list(map(int, input().split()))

    for i in range(len(dol)):  # 0에서 가까운 거리를 찾아야 하므로 절대값으로 바꿔준다.
        dol[i] = abs(dol[i])

    print(f'#{test_case} {min(dol)} {dol.count(min(dol))}')
