T = int(input())

for t in range(1, T+1):
    N = int(input())

    print("#{}".format(t), end=" ")
    for i in range(N):
        print("1/" + str(N), end=" ")
    print()
