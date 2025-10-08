# 영화관 좌석 예매 시스템
# 영화관의 좌석은 총 5개가 있다고 가정한다.
# 프로그램이 랜덤하게 1~5 중 이미 예매된 좌석 번호를 한 개 선택한다.
# 사용자는 예매하고 싶은 좌석 번호(1~5 중 하나)를 입력한다.
# 조건문만 사용하여 다음과 같은 결과를 출력하시오.
import random

choice = [1,2,3,4,5]
computer = random.choice(choice)
print("이미 예매된 좌석", computer)
man = int(input("원하는 좌석 번호를 입력하세요 :"))
if man < 1 or man > 5 :
    print("존재하지 않는 좌석입니다.")
elif computer == man :
    print("이미 예약된 좌석입니다.")
else :
    print("예매에 성공하였습니다.")