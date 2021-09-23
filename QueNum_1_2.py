## 최대 공약수를 찾는 프로그램을 작성해 보자

x, y = map(int, input("두 수를 입력해주세요. [띄어쓰기 구분]: ").split())

nums = []
for i in range(1, x+1 if x>=y else y+1 ):
    if ((x%i == 0)and(y%i == 0)):
        nums.append(i)

print("약수: ", nums , "최대 공약수 :", max(nums))

