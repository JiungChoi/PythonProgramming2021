# 다음 수열의 합을 계싼하는 프로그램을 작성하시오.
# 1/3 + 3/5 + 5/7 + .... +99/101

num1 = 1
total = 0
while(num1 < 100):
    total += num1 / (num1+2)
    num1 += 2

print(total)

