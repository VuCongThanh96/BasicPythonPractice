print('Chương trình kiểm tra số nguyên tố')
x = int(input('Nhập vào số nguyên dương cần kiểm tra: '))
y = 0
if x <= 0:
    print('Bạn đã nhập sai, hãy nhập lại!')
elif x == 1:
    print('1 không phải số nguyên tố')
else:
    for i in range(1, x+1):
        if (x % i) == 0:
            y += 1
if y == 2:
    print(x, 'là số nguyên tố')
else:
    print(x, 'không là số nguyên tố')
