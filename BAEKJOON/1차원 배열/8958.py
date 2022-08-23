# [백준 8958번] - OX퀴즈 - (브론즈2, 1차원배열)

T = int(input())

for i in range(T):
    OX = list(map(str, input()))
    ans = 0
    cnt = 1
    for j in OX:
        if j == "0":
            cnt += 1
            ans += cnt
        else:
            cnt = 0
    print(ans)