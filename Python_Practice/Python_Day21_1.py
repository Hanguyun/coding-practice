min = int(input("중간고사 점수를 입력하세요(0~30):"))
fin = int(input("중간고사 점수를 입력하세요(0~30):"))
hw = int(input("중간고사 점수를 입력하세요(0~30):"))
att = int(input("중간고사 점수를 입력하세요(0~30):"))

total = min+fin+hw+att

level = total//90+total//80+total//70+total//60

grade='FDCBA'
