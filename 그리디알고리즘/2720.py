# [백준 2720번] - 세탁소 사장 동혁 - (브론즈3, greedy)

T = int(input())

for i in range(T):
    C = int(input())
    Q = C // 25
    D = C % 25 // 10
    N = C % 25 % 10 // 5
    P = C % 25 % 10 % 5

    print(Q, D, N, P)