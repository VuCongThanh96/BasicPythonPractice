#:ax^2+bx+c=0
import math

print("Chương trình Giải phương trình bậc 2: ax^2+bx+c=0")
print("Nhập vào tham số a:")
a = float(input())
if a == 0:
    print("Với a=0 thì đây là phương trình bậc 1, hãy làm lại!")
else:
    print("Nhập vào tham số b:")
    b = float(input())
    print("Nhập vào tham số c:")
    c = float(input())
    d = (b**2-4*a*c)
    if d < 0:
        print("Phương trình vô nghiệm")
    elif d > 0:
        print("Phương trình có 2 nghiệm phân biệt x1=", (-b+math.sqrt(d))/(2*a), "và x2=", (-b-math.sqrt(d))/(2*a))
    else:
        print("Phương trình có nghiệm kép x1=x2=", -b/(2*a))
