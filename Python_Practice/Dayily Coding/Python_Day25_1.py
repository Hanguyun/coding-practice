import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")

choice = int(input(f"{today}으로 새 일기장을 쓰시려면 1번, 기존 날짜에 내용 추가는 0번을 눌러주세요: "))

if choice == 1:
    with open('일기장.txt', 'w', encoding='utf-8') as f:
        f.write(f"{today}\n")
        w = input("일기 내용을 작성하세요: ")
        f.write(f"{w}\n")
        f.close()
# else :
#     with open('일기장.txt', 'w', encoding='utf-8') as f:
