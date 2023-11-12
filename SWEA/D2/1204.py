T = int(input())  # 전체 테케 수 입력받음

for _ in range(T):  # 테케 반복

    tc = int(input())  # 테케 번호 입력 받음
    score = list(map(int, input().split()))  # 학생 점수 입력받음
    data = [0] * 1001  # 1001개의 원소를 가지는 리스트 data 생성, 빈도 저장용

    for i in score:
        data[i] += 1  # 해당 점수의 빈도를 1 증가시킴

    max_value = max(data)  # data 리스트에서 가장 큰 값을 찾아 max_value 변수에 저장
    result = []  # 최빈수 점수 저장
    for i in range(len(data)):  # data리스트를 순회하면서
        if data[i] == max_value:  # 현재 점수의 빈도가 최빈수의 빈도와 같다면
            result.append(i)  # 현재 점수를 result에 추가

    print('#%d %d' % (tc, max(result)))
