# Các tháng có 30 ngày là 4,6,9,11. Năm nhuận tháng 2 có 29 ngày
print("Chương trình tìm ngày kế tiếp sau ngày kiểm tra (sau công nguyên)")
print("Nhập ngày")
d = int(input())
print("Nhập tháng")
m = int(input())
print("Nhập năm")
y = int(input())
# Các tháng đều có đủ 28 ngày nên 1->27 có thể tính chung cho 12 tháng
if 0 < d < 28:
    print("Ngày tiếp theo là: ", d + 1, " tháng ", m, "năm ", y)
elif d == 28:
    if m == 2:
        if (y % 4 == 0 and y & 100 != 0) or (y % 400 == 0):
            print("Ngày tiếp theo là: ", d + 1, " tháng ", m, "năm ", y)
        else:
            print("Ngày tiếp theo là: ", 1, " tháng ", 3, "năm ", y)
    else:
        print("Ngày tiếp theo là: ", d + 1, " tháng ", m, "năm ", y)
elif d == 29:
    if m == 2:
        if (y % 4 == 0 and y & 100 != 0) or (y % 400 == 0):
            print("Ngày tiếp theo là: ", 1, " tháng ", 3, "năm ", y)
        else:
            print("Bạn đã nhập sai tháng, hãy nhập lại!")
    else:
        print("Ngày tiếp theo là: ", 30, " tháng ", m+1, "năm ", y)
elif d == 30:
    if m == 4 or m == 6 or m == 9 or m == 11:
        print("Ngày tiếp theo là: ", 1, " tháng ", m+1, "năm ", y)
    else:
        print("Ngày tiếp theo là: ", 30, " tháng ", m, "năm ", y)
elif d == 31:
    if m == 2 or m == 4 or m == 6 or m == 9 or m == 11:
        print("Bạn đã nhập sai tháng, hãy nhập lại!")
    elif m == 12:
        print("Ngày tiếp theo là: ", 1, " tháng ", 1, "năm ", y+1)
    else:
        print("Ngày tiếp theo là: ", 1, " tháng ", m+1, "năm ", y)
else:
    print("Bạn đã nhập sai ngày/tháng/năm, hãy nhập lại!")
