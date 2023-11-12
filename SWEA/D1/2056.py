T = int(input())

for test_case in range(1, T+1):

    date_str = input()

    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[6:8]

    if int(month) < 1 or int(month) > 12 or int(day) < 1 or int(day) > 31:
        result = -1
    elif int(month) in [4, 6, 9, 11] and int(day) > 30:
        result = -1
    elif int(month) == 2 and int(day) > 28:
        result = -1
    else:
        result = f"{year}/{month}/{day}"

    print(f"#{test_case} {result}")