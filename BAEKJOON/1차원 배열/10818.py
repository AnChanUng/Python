# [백준 10818번] - 최소, 최대 - (브론즈3, 1차원배열)
import sys
input = sys.stdin.readline

N = int(input()) # 정수의 개수
k = list(map(int, input().split())) # N개의 정수를 공백입력

print(min(k), max(k))