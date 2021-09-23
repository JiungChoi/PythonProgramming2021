# 1부터 10까지 제곱의 합을 출력하는 프로그램을 작성해 보자


for i in range(1, 11):
    ary = []
    for j in range(1, 5):
        ary.append(int(i)**int(j)) 
    print(ary)

