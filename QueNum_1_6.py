## 난수 생섬 함수를 사용하여 2개의 주사위를 던졌을 때 나오는 수를 출력해 보자

import random

state = "Y"
while(state =="Y"):
    print("첫 번째 주사위", random.randint(1, 6), "두 번째 주사위", random.randint(1, 6))
    state = input("계속 하시겠습니까? [ Y/N ]")

