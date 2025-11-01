# 동전 던지기 게임
# 프로그램이 동전을 10번 던진다. 앞면이면 "front" 뒷면이면 "back"을 출력한다.
# 10번 던진 후 결과를 요약해서 출력하라.
# 앞면은 1, 뒷면은 0으로 랜덤하게 나온다고 가정 10번 반복
# 앞면의 개수와 뒷면의 개수를 세서 마지막에 출력
# 만약 앞면이 더 많으면 "Lucky" 같으면 "Average luck!", 뒷면이 더 많으면 "Unlucky"를 출력

import random

coin_front = 0
coin_back = 0

for i in range(10) :
  coin = random.randint(0,1)
  if coin == 1 :
    print("front")
    coin_front += 1
  else :
    print("back")
    coin_back += 1

if coin_front == coin_back :
  print("Average luck")
elif coin_front < coin_back :
  print("Unlucky")
else :
  print("Lucky")

print("front :", coin_front)
print("back :", coin_back)
