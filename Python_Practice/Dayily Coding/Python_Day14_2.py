# 조건문 없이 운전면허 시험 프로그램 작성
# 1종의 합격 점수 70, 2종의 합격 점수 60
jong = int(input("종을 입력하세요:"))
score = int(input("점수를 입력하세요:"))
level = {1 : 70, 2 : 60}
result = ["불합격", "합격"][(score >= level[jong])]
print(f"{jong}종 {score}점 {result}")
