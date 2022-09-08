# 다음 셀에 문제에 대한 답을 up_and_down_game 함수로 작성하시오.
import random

answer = random.randint(0, 99) # 랜덤 숫자 생성
n = 0 # 초기화
guess = 0

while answer != guess:
    guess = int(input("숫자를 입력하세요(범위 0~99): "))

    if answer > guess:
        print("아닙니다. 더 큰 숫자입니다!")
    elif answer < guess:
        print("아닙니다. 더 작은 숫자입니다.")
    n += 1
print("정답입니다" + str(n) + "번 만에 맞추셨습니다.")
print("게임이 끝났습니다.")