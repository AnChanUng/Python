n = int(input())  # 한변의 길이
x, y = 1, 1  # 좌표 1,1로 초기화
plans = input().split()  # 문자열로 이동 계획 입력 받기

# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]  # 좌우 이동
dy = [-1, 1, 0, 0]  # 상하 이동
move_types = ['L', 'R', 'U', 'D']  # 이동방향의 문자열 표현

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 자표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if n < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)
