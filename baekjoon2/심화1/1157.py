word = input().lower()  # 입력 문자열을 소문자로 변환
count = [0] * 26  # 알파벳 빈도를 저장할 리스트 초기화

for char in word:
    if char.isalpha():  # 알파벳인 경우에만 처리
        count[ord(char) - ord('a')] += 1

max_count = max(count)  # 가장 많이 나온 알파벳의 빈도

if count.count(max_count) > 1:
    print("?")  # 가장 많이 나온 알파벳이 여러 개인 경우
else:
    max_index = count.index(max_count)  # 가장 많이 나온 알파벳의 인덱스
    most_frequent_char = chr(max_index + ord('a')).upper()  # 대문자로 변환
    print(most_frequent_char)
