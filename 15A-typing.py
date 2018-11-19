import random
import time

w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
n = 1 #문제 번호
print("[타자게임]준비하면 엔터!")
input()

start = time.time() # 시작시간 기록

q = random.choice(w)

while n <= 5:
    print("문제",n)
    print(q)
    x = input() #사용자 입력
    if q == x:
        print("통과!")
        n = n+1
        q = random.choice(w)
    else:
        print("오타!")

end = time.time()
et = end - start
et = format(et, ".2f") # 소수점 둘째자리까지 표기
print("타자 시간 :",et,"초")

    
        
