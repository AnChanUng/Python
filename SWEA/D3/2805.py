T = int(input())

for test_case in range(1, T+1):
    N = input()
    data = [list(map(int, input())) for _ in range(N)]
    start, end = N // 2, N // 2

    result = 0
    for i in range(N):
        for j in range(start, end+1):
            result += data[i][j]  # result에 누적시킴

        if i < N//2:  # i가 중간값 보다 작으면
            start -= 1  # start 1감소
            end += 1  # end 1증가
        else:  # 그렇지 않다면
            start += 1  # start 1증가
            end -= 1  # end 1감소

    print(f'#{test_case} {result}')
