# [백준 1157번] - 단어 공부 - (브론즈1, 문자열)

word = input().upper()
num = []
for i in range(ord('A'),ord('Z')+1):
    num.append(word.count(chr(i)))

if num.count(max(num)) == 1:
    print(chr(num.index(max(num))+ ord('A')))
else:
    print('?')