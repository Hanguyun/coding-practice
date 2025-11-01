# 학생 점수 관리 프로그램을 작성하시오.
# 5명의 점수를 리스트에 저장하고 출력
# 전체 평균 점수를 구해서 출력
# 60점 이상은 "합격", 60점 미만은 "불합격"
# 가장 높은 점수와 가장 낮은 점수를 출력
# 평균 이상인 학생 수를 출력
import random

scores = [random.randint(0, 100) for _ in range(5)]
print("학생 점수:", scores)

avg = sum(scores) / len(scores)
print(f"평균 점수: {avg:.1f}")

for i in range(len(scores)):
    if scores[i] >= 60:
        print(f"{i+1}번 학생: {scores[i]}점 → 합격")
    else:
        print(f"{i+1}번 학생: {scores[i]}점 → 불합격")

print("최고점:", max(scores))
print("최저점:", min(scores))

count = 0
for score in scores:
    if score >= avg:
        count += 1

print(f"평균 이상 학생 수: {count}명")
