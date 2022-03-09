import turtle
print('Chương trình vẽ hình chữ nhật theo yêu cầu (đơn vị: pixel)')
a = float(input("Nhập vào chiều dài:"))
b = float(input("Nhập vào chiều rộng:"))
hcn = turtle.Turtle()
for i in range(2):
    hcn.forward(a)
    hcn.right(90)
    hcn.forward(b)
    hcn.right(90)
turtle.done()
