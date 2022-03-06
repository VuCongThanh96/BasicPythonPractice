
print("Đây là bộ chuyển đổi thòi gian bạn đã sống tính theo giây đến thời điểm 0h0'0s ngày 01/03/2022 không tính ngày nhuận")
print("Nhập vào năm sinh của bạn:")
y=float(input())
print("Nhập vào tháng sinh của bạn:")
m=float(input())
print("Nhập vào ngày sinh của bạn:")
d=float(input())
a=24*60*60
s=((2022-y)*365*a)+(12-m)*30*a+(30-d)*d
print("Số giây bạn đã sống là:",s)
