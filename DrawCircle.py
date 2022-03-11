import turtle
t = turtle.Turtle()
# Vẽ 1 hình tròn đơn giản
t.circle(75)
# Đổi màu cho pen và size cho pen
t.pensize(3)
t.pencolor("blue")
# Vẽ và tô màu bên trong hình tròn tại 1 điểm tọa độ mới
t.penup()
t.setpos(150, 50)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(30)
t.end_fill()
# Thay đổi kích thước pen
t.pencolor("red")
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
