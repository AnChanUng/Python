# [백준 10162번] 전자레인지 - (브론즈4, greedy)

T = int(input())
x = T//300
x1 = T%300//60 
x2 = T%300%60
x3 = x2%10
x4 = x2//10

if x3 == 0:
    print(x, x1, x4)
elif x3 != 0:
    print(-1)