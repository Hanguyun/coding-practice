# 시험 과목 합격 판정 프로그램 (조건문 없이)
# 세 과목(국어, 영어, 수학) 점수를 입력한다.
# 각 과목의 합격 기준은 60점이다.
# 단, 세 과목 모두 60점 이상이면 "합격", 하나라도 60점 미만이면 "불합격"을 출력하라.
score1 = int(input("국어 점수를 입력하세요:"))
score2 = int(input("영어 점수를 입력하세요:"))
score3 = int(input("수학 점수를 입력하세요:"))
kor = score1
eng = score2
math = score3
level = {"국어":60,"영어":60,"수학":60}
result = ["불합격", "합격"][(kor >= 60) and (eng >= 60) and (math >= 60)]
print(f"국어{kor}점 영어{eng}점 수학{math} {result}")