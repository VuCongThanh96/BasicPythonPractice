print('Chương trình tìm số nguyên dương có thể chia hết cho 1 số bất kỳ trong đoạn [1;1000]')
a = []
c = int(input('Nhập vào số bất kỳ cần chia hết: '))
for b in range(1, 1001):
    if b % c == 0:
        a.append(str(b))
print(','.join(a))
