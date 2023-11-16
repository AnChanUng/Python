T = int(input())

for test_case in range(1, T+1):

    grade = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    N, K = map(int, input().split())
    scores = []

    for _ in range(N):
        mid_score, final_score, homework = map(int, input().split())
        score = mid_score * 0.35 + final_score * 0.45 + homework * 0.2
        scores.append(score)

    k_score = scores[K-1]  # k번째 학생의 정수
    scores.sort(reverse=True)  # 내림차순 정렬
    idx = scores.index(k_score) // (N//10)  # 상위 10%에 속하는 학생의 등급을 가져옴
    print(f'#{test_case} {grade[idx]}')
