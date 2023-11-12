S = input()
count = 0

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

print((count+1)//2)  # 변화 횟수에 1을 더한후 2로 나눈 몫

# # ------------------------ #
# data = input()
# count0 = 0
# count1 = 1

# # 첫 번째 원소에 대해서 처리
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(data)-1):
#     if data[i] != data[i+1]:
#         if data[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1

# print(min(count0, count1))
