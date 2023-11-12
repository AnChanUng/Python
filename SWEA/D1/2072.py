T = int(input())
answer = 0

for i in range(T):
    num = map(int, input().split())

    for j in num:
        if j % 2 != 0:
            answer += i
    print("#" + str(i), str(num))
