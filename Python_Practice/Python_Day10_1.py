# 로또 추첨기 - 당첨 판정 프로그램
# 컴퓨터가 1~45 사이의 숫자 6개를 랜덤으로 추첨(set 사용) 한다.
# 사용자는 자신의 6개 번호를 직접 입력한다.
# 조건문만 사용해서 다음과 같은 결과를 판정하라.
# 6개 모두 일치 1 등 당첨, 5개 일치 2등 당첨, 4개 일치 3등 당첨, 3개 일치 4등 당첨, 2개 이하 꽝
import random

computer = set(random.sample(range(1,46), k=6))
user = set(map(int, input("1~45 중 6개의 숫자를 입력하세요 (공백으로 구분): ").split()))
match = computer.intersection(user)

print("내 번호:", user)
print("맞춘 번호:", match)
print("맞춘 개수:", len(match))
if len(match) == 6 :
    print("1등 당첨!")
elif len(match) == 5 :
    print("2등 당첨!")
elif len(match) == 4 :
    print("3등 당첨!")
elif len(match) == 3 :
    print("4등 당첨!")
else :
    print("꽝")