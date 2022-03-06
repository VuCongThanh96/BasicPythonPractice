#Các tháng có 30 ngày là 4,6,9,11. Năm nhuận tháng 2 có 29 ngày
print("Đây là chương trình kiểm tra số ngày trong tháng")
m=int(input("Nhập vào tháng bạn cần kiểm tra: "))
y=int(input("Nhập vào năm bạn cần kiểm tra: "))
if (m>12 or m==0):
    print("Bạn đã nhập sai, hãy nhập lại!")
elif (m==4 or m==6 or m==9 or m==11):
    print("Tháng ",m," năm ",y," có 30 ngày")
elif (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12):
    print("Tháng ",m," năm ",y," có 31 ngày")
else:
    if (y%4==0 and y%100!=0) or (y%400==0):
        print("Tháng ",m," năm ",y," có 29 ngày")
    else:
        print("Tháng ",m," năm ",y," có 28 ngày")
