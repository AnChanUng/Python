# [백준 2720번] - 세탁소 사장 동혁 - (브론즈3, greedy)
#  쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수
#  니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수
#  $1.24 = 4쿼터 + 2다임 + 0니켈 + 4페니
T = int(input())

for i in range(T):
    C = int(input())
    Q = C // 25
    D = C % 25 // 10
    N = C % 25 % 10 // 5
    P = C % 25 % 10 % 5

    print(Q, D, N, P)