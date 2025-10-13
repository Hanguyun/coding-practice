# 조건문 없이 학점 계산 프로그램
# 학점 기준 100~90 = A, 80~89 = B, 70~79 = C, 60~69 D, 59이하 F
score = int(input("점수를 입력하세요:"))
index = score // 10
grades = ['F', 'F', 'F','F','F','F','D','C','B','A','A']
print(grades[index])