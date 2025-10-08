# 운전면허 시험 프로그램
# 운전면허 필기시험 점수를 입력받아 다음 조건에 따라 결과를 출력하시오.
# 90 이상 합격(우수), 70점이상 90점 미만 합격, 60점 이상 70미만 보충교육대상, 60점 미만 불합격.

score = int(input("점수를 입력하세요:"))
if score > 100 :
    print("점수를 잘못 입력하셨습니다.")
elif score >= 90 :
    print(score,"점 합격(우수)")
elif score >= 70  :
    print(score,"점 합격")
elif score >= 60  :
    print(score, "점 보충교육 대상")
elif score < 60 :
    print(score, "점 불합격")
else :
    print("점수를 잘못 입력하셨습니다.")