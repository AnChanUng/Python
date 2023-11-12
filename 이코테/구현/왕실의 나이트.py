input_data = input()  # 체스판의 위치를 나타내는 문자열
row = int(input_data[1])  # 세로 좌표
column = int(ord(input_data[0])) - int(ord('a')) + 1  # 가로 좌표

steps = [(-2, -1), (-1. - 2), (1, -2), (2, -1), (2, 1),
         (1, 2), (-1, 2), (-2, 1)]  # 나이트가 가능한 모든 이동 방향을 튜플로

result = 0
for step in steps:  # 모든 이동 방향을 반복
    next_row = row + step[0]  # 세로 이동거리 더하여 다음 위치의 세로 좌표 계산
    next_column = column + step[1]  # 가로 이동거리를 더하여 다음 위치의 가로 좌표 계산

    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:  # 세로, 가로 좌표가 1이상 8이하면
        result += 1

print(result)
