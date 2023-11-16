T = int(input())
yoil = {"MON": 1, "TUE": 2, "WED": 3, "THU": 4, "FRI": 5, "SAT": 6, "SUN": 7}

for test_case in range(1, T+1):
    s = input()
    if s == "SUN":
        print(f'#{test_case} 7')
    else:
        print(f'#{test_case} {yoil["SUN"] - yoil[s]}')
