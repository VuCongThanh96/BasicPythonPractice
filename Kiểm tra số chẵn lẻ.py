# Chương trình kiểm tra số chẵn lẻ bằng toán tử ba ngôi
print('Đây là chương trình kiểm tra số nguyên chẵn hay lẻ')
a = int(input('Nhập vào số bạn muốn kiểm tra: '))
b = 'số chẵn' if (a % 2 == 0) else 'số lẻ'
print('Số ', a, 'là', b)
