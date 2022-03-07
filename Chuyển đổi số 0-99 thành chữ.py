print("Nhập vào số bạn muốn chuyển đổi thành chữ 0-99")
a = int(input())
b = a//10
c = a % 10
if a < 10 or a > 99:
    print("Bạn đã nhập sai, hãy nhập lại")
else:
    if b == 1:
        m = "mười"
    if b == 2:
        m = "hai mươi"
    if b == 3:
        m = "ba mươi"
    if b == 4:
        m = "bốn mươi"
    if b == 5:
        m = "năm mươi"
    if b == 6:
        m = "sáu mươi"
    if b == 7:
        m = "bảy mươi"
    if b == 8:
        m = "tám mươi"
    if b == 9:
        m = "chín mươi"
    if c == 1:
        n = "một"
    if c == 2:
        n = "hai"
    if c == 3:
        n = "ba"
    if c == 4:
        n = "bốn"
    if c == 5:
        n = "năm"
    if c == 6:
        n = "sáu"
    if c == 7:
        n = "bảy"
    if c == 8:
        n = "tám"
    if c == 9:
        n = "chín"
    if c == 0 and b != 10:
        n = ""
    print("Đây là số:", m, n)
