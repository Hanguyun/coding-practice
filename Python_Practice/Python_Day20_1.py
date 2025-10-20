# # 시험대비 기초(조건문) 복습
# 1. 주민등록번호 13자리를 입력받아 남자,여자인지 판별하여 출력하는 프로그램을 작성하시오.
#    남자는 1,3 여자는 2,4
# num = input("주민등록번호 13자리를 입력하세요:")
# a = num[6]
#
# if a == '1' or a == '3' :
#     print("남자입니다.")
# elif a == '2' or a == '4' :
#     print("여자입니다.")
# else :
#     print("잘못된 입력입니다.")
#------------------------------------------------------------------
# 2. 나이를 입력받아 입장료를 출력하는 프로그램을 작성하시오.
#    입장료 0~6 무료, 7~17 10,000원, 18~ 64 20,000원, 65세 이상 무료
# age = int(input("나이를 입력하세요:"))
# if 0 <= age <= 6 :
#     print(f"{age}세 무료입니다.")
# elif 7 <= age <= 17 :
#     print(f"{age}세 10,000원입니다.")
# elif 18 <= age <= 64 :
#     print(f"{age}세 20,000원입니다.")
# else :
#     print(f"{age}세 무료입니다.")
#------------------------------------------------------------------
# 3-1. 운전면허 점수와 시험종류(1종, 2종)를 입력 받아,
# 종류와 점수에 따라 합격/불합격을 출력하는 프로그램을 작성하시오
# 1종 70, 2종 60
# jong = int(input("종을 입력하세요:"))
# score = int(input("점수를 입력하세요:"))
# if jong == 1 :
#     if score >= 70 :
#         print(f"{jong}종 {score}점으로 합격입니다.")
#     else :
#         print(f"{jong}종 {score}점으로 불합격입니다.")
# elif jong == 2 :
#     if score >= 60 :
#         print(f"{jong}종 {score}점으로 합격입니다.")
#     else :
#         print(f"{jong}종 {score}점으로 불합격입니다.")
# else :
#     print("잘못된 입력입니다.")

# 3-2. 3-1을 조건문 한 개를 사용하여 작성하세요
# jong = int(input("종을 입력하세요(1종, 2종):"))
# score = int(input("점수를 입력하세요:"))
#
# cut = 80 - jong * 10
#
# if score >= cut :
#     print(f"{jong}종 {score}점으로 합격입니다.")
# else :
#     print(f"{jong}종 {score}점으로 불합격입니다.")

# 4-1 세 과목 성적을 입력받아 점수에 따라 합격, 불합격을 판정하는 프로그램을 작성하세요.
# 각 과목의 점수는 100점 만점으로 입력(0~100)
# 세 과목의 평균 점수가 60점 이상이면 합격.
# 한 과목이라도 점수가 40점 미만이면 편균 점수에 상관없이 불합격이다.
score1 = int(input("첫 번째 과목의 점수를 입력하세요:"))
score2 = int(input("두 번째 과목의 점수를 입력하세요:"))
score3 = int(input("세 번째 과목의 점수를 입력하세요:"))
hap = score1 + score2 + score3
average = (score1+score2+score3)/3

if not (0 <= score1 <= 100 and 0 <= score2 <= 100 and 0 <= score3 <= 100) :
    print("점수를 잘못 입력했습니다.")
elif score1 < 40 or score2 < 40 or score3 < 40 :
    print(f"40점 미만인 과목이 있습니다. 불합격입니다.")
elif average >= 60 :
    print(f"{average}점으로 합격입니다.")
else :
    print(f"{average}점으로 불합격입니다.")
    