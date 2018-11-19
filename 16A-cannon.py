import turtle as t
import random

def turn_up():
    t.left(2)    #위로 올릴때 2도 왼쪽

def turn_down():
    t.right(2)   #내릴때 2도 오른쪽

def fire(): #발사
    ang = t.heading() #각도 기억
    while t.ycor() > 0: # 거북이 땅위에 있는동안 반복
        t.forward(15)
        t.right(5)

    # while문이 끝나면 거북이는 땅
    d = t.distance(target, 0) #목표 지점과 거리
    t.sety(random.randint(10, 100)) #성공 실패 표시할 위치 지정

    if d < 25: #거리 차이가 25미만 명중
        t.color("blue")
        t.write("Good!",False,"center",("",15))
    else: #아니면 실패
        t.color("red")
        t.write("Bad!",False,"center",("",15))
    t.color("black") #거북이 색 검정색으로 되돌리기
    t.goto(-200, 10) #거북이 위치 처음 발사 했던 곳으로 되돌리기
    t.setheading(ang) #각도가 처음 기억해둔 각도로 되돌리기

# 땅그리기
t.goto(-300,0)
t.down()
t.goto(300,0)

# 목표 지점 설정그리기
target = random.randint(50, 150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target - 25,2)
t.down()
t.goto(target + 25,2)

# 거북이 색 검은색 지정 처음 발사했던곳으로 되돌리기
t.color("black")
t.up
t.goto(-200, 10)
t.setheading(20)

# 거북이 동작
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()
        
