# [실습5-4] 비재귀적으로 재귀 함수 구현하기(꼬리 재귀를 제거)

from pickletools import read_unicodestring4


def recur(n: int) -> int:
    """꼬리 재귀를 제거한 recur() 함수"""
    while n > 0:
        recur(n - 1)
        print(n)
        n = n -2

x = int(input())

recur(x)