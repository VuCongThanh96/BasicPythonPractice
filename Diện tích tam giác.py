import math
# Chương trình tín diện tích hình tam giác khi chỉ biết độ dài 3 cạnh
# Công thức Heron S=căn bậc 2[(a+b+c)(a+b-c)(a+c-b)(b+c-a)] chia cho 4
'''Công thức Heron dạng khác:
p=Nửa chu vi tam giác
s=Căn bậc 2 của [p(p-a)(p-b)(p-c)]'''
print('Đây là chương trình tính diện tích hình tam giác với chiều dài 3 cạnh')
a = float(input('Nhập vào chiều dài cạnh thứ nhất:'))
b = float(input('Nhập vào chiều dài cạnh thứ hai:'))
c = float(input('Nhập vào chiều dài cạnh thứ ba:'))
S = (math.sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a)))/4
print('Diện tích tam giác là: ', S)
