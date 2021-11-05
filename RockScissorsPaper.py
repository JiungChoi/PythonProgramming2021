import random

RSP = ["가위", "바위", "보"]

while(1):
    computer = random.randrange(0, 3)
    mine = int(input("당신의 패를 입력하세요. 가위(0), 바위(1), 보(2) : "))
    winnumber = (computer + 1) % 3

    print(f"당신: {RSP[mine]} 컴퓨터: {RSP[computer]}")
    print("비겼습니다.") if (mine == computer) else print("당신이 이겼습니다.") if (winnumber == mine) else print(f"컴퓨터가 이겼습니다.")
