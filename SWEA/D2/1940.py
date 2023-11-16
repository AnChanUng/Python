# command

# 0 현재 속도 유지
# 1 가속
# 2 감속

# n개의 command를 모두 수행했을 때, n초 동안 이동한 거리를 계산하는 프로그램

T = int(input())

for i in range(1, T+1):

    N = int(input())  # command의 수
    speed = 0
    distance = 0

    for _ in range(N):
        command = list(map(int, input().split()))
        if command[0] == 1:  # command[0]이 1인경우 속도를 증가시킴
            speed += command[1]
        elif command[0] == 2:  # command[0]이 2인 경우 속도를 감소 시킴
            if speed > command[1]:
                speed -= command[1]
            else:  # 현재 속도보다 감소하려는 속도가 더 클 경우 속도는 0으로 설정
                speed = 0
        distance += speed

    print(f'#{i} {distance}')
