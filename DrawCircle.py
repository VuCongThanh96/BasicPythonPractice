import turtle
t = turtle.Turtle()
# Vẽ 1 hình tròn đơn giản
t.circle(50)
# Đổi màu cho pen
t.pencolor("blue")
# Vẽ và tô màu bên trong hình tròn tại 1 điểm tọa độ mới
t.penup()
t.goto(150, 100)
t.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()
# Thay đổi kích thước pen
t.right(90)
t.forward(250)
t.pensize(7)
for i in range(4):
    t.left(90)
    t.forward(150)
# Vẽ một chấm tròn
t.goto(-25, -230)
t.dot(150)
turtle.done()
