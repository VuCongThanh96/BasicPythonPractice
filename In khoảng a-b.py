print('Đây là chương trình in ra dãy số thuộc -1000<=[a;b]<=1000 (a,b đều là số nguyên tùy bạn chọn giá trị)')
a = int(input('Nhập vào số bắt đầu:'))
b = int(input('Nhập vào số kết thúc:'))
if a > b or a < -1000 or b > 1000:
    print('Bạn đã nhập sai, hãy nhập lại')
else:
    x = a
    print('Dãy số là:')
    for x in range(a, b+1):
        print(x, end='. ')
        x = x + 1
        if x > b:
            break
