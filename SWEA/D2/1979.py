T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())  # n 가로세로 길이, k 단어의 길이
    # 퍼즐의 2차원 정보
    # 퍼즐의 흰색부분 1 검은색 부분 0
