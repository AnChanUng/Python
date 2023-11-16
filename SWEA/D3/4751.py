T = int(input())

for test_case in range(1, T+1):

    a = input()
    for i in range(1, 6):
        for j in range(1, 6):
            print("." + ".#." * len(a) * i + ".")
