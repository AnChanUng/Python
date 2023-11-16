T = int(input())

for test_case in range(1, T+1):

    N = int(input())

    arr = [[0] * N for _ in range(N)] # N*N 빈 2차원 배열 만들기

    for i in range(N):
        # 열의 크기는 행의 인덱스 + 1
        for j in range(i+1):
            if i == j or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{test_case}')

    for row in arr:
        result = []
        for x in row:
            if x:
                result += [x]
        print(*result)
