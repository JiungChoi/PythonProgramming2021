## 10,000,000원이 있다. 현재 은행 이율은 복리 7%이다. 
## 은행에 저금한 돈이 두 배가 되려면 몇 년이 걸릴까?


money = 10000000
cnt = 0
while( money < 20000000 ):
    cnt += 1
    money += (0.07*money)  

print(f"{cnt}년이 되면 원금의 두 배가 됩니다.")

    
    
