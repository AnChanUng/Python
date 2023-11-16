N = int(input())

for i in range(1, N+1):
    count_clap = str(i).count('3') + str(i).count('6') + str(i).count('9')
    # 각 숫자에 대해 3,6,9의 개수를 세기 위해 해당 숫자를 문자열로 변환하고, 문자열에서
    # '3', '6', '9'가 각각 몇번 나오는지 세어 count_clap에 저장

    if count_clap == 0:
        print(i, end=" ")
    else:
        print("-" * count_clap, end=" ")
