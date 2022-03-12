# Tính S(x, n) = x + x^2/2! + x^3/3! + ....+ x^n/n! với x, n đều là số nguyên; n=!0
print('Chương trình tính S = x + x^2/2! + x^3/3! + ....+ x^n/n! (x, n đều là số nguyên, n=!o)')
x = int(input('Nhập vào giá trị x:'))
n = int(input('Nhập vào giá trị n:'))
s = 0
for i in range(1, n + 1):
    tu = x**i
    mau = 1
    for j in range(1, i + 1):
        mau = mau*j
    s = s+(tu/mau)
print('Kết quả là:', s)
