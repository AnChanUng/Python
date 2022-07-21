# [백준 11034번] 캥거루 세마리2 - (브론즈3, greedy)

while True:
    try:
        a, b, c = map(int, input().split())
        print(max(a-b-1), (c-b-1))
    except:
        break