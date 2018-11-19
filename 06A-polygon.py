import turtle as t

n=5
t.color("purple")
t.speed(1)
t.begin_fill()
for x in range(n):
    t.forward(50)
    t.left(360/n)
t.end_fill()
