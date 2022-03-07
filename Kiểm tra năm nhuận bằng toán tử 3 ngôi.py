print('Đây là chương trình kiểm tra năm nhuận')
y = int(input('Nhập vào năm bạn muốn kiểm tra:'))
x = 'là năm nhuận' if ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) else 'không phải năm nhuận'
print(y, x)
