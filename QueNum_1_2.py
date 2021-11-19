## 최대 공약수를 찾는 프로그램을 작성해 보자


#%%
def getGCD(a, b):
    while(1):    
        if (a%b):
            a, b = b, a%b           
        else :
            break
    return b
    
    
num1, num2 = map(int, input("두 수를 입력하세요 : ").split())
print( "두 수의 최대 공약수는 : ", getGCD(num1, num2), "입니다.")

