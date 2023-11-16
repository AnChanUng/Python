T = int(input())

for test_case in range(1, T+1):

    text = list(input())
    text.reverse()
    for i in range(len(text)):
        if text[i] == 'b':
            text[i] = 'd'
        elif text[i] == 'd':
            text[i] = 'b'
        elif text[i] == 'p':
            text[i] = 'q'
        elif text[i] == 'q':
            text[i] = 'p'

    print("#"+str(test_case), "".join(text))
