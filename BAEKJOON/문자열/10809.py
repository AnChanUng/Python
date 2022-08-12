# [백준 10809번] - 알파벳 찾기 - (브론즈5, 문자열)

s = input()
abc = 'abcdefghijklmnopqrstuvwxyz'

for i in abc:
    if i in s:
        print(s.index(i), end= ' ')
    else:
        print(-1, end = ' ')