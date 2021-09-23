## 구구단표를 출력하는 프로그램을 작성하라. 형식은 정확히 일치하지 않아도 된다.


for i in range(1, 10):
    ary = []
    for j in range(1, 10):
        ary.append(i*j)
    print(f"{ary}")
        
        