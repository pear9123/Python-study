import turtle as t
import random

te = t.Turtle() #악당거북이
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle() #먹이
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_rigth():
    t.setheading(0) # 오른쪽 방향

def turn_up():
    t.setheading(90) # 위쪽 방향

def turn_left():
    t.setheading(180) # 왼쪽 방향

def turn_down():
    t.setheading(270) # 아래 방향

def play(): # 실제 플레이 함수
    t.forward(10)   #주인공 거북이 앞으로 10 이동
    ang = te.towards(t.pos()) 
    te.setheading(ang) # 악당 거북이 주인공 거북이랑 바라보게함
    te.forward(9) # 악당 거북이 9만큼 앞으로 이동

    if t.distance(ts) < 12:#주인공과 먹이의 거리가 12보다 작으면
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y) #먹이를 다른 곳으로 옮김
    if t.distance(te) >= 12: # 주인공과 악당이 거리가 12이상이면
        t.ontimer(play, 100) # 0.1초 후 play 함수 실행

t.setup(500,500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")
t.onkeypress(turn_rigth,"Right")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_down,"Down")
t.listen()
play() # play 호출
