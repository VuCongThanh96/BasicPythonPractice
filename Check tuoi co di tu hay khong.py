print("Ôn tập lại python do lâu rồi k code, vui thôi đừng căng quá")
x = int(input("Nhập vào năm sinh của bạn: "))
y = 2022 - x
if y < 13:
    print("Bạn là thiếu nhi! Hãy đọc nhiều sách báo và chăm chơi thể thao nhé!")
elif 13 <= y < 18:
    a = input("Bạn đã chich bao giờ chưa? (Nhập True hoặc Flase)" "\n")
    def StrToBool (a):
        return a.lower() in ("yes")
    if a == 1:
        b = input(print("Bạn chịch của bạn bao lúc đó bao nhiêu tuổi"))
        if b < 18:
            print("Cả 2 đều chưa trưởng thành, cả 2 đều có thể phải đi tù đó!")
        else:
            print("Bạn đang tuổi thiếu niên, bạn chịch của bạn sẽ phải đi tù!")
    else:
        print("You are a good boy, hãy chăm chỉ học tập, xem tin tức, đọc sách báo và chơi thể thao nhiều vào nhé!")
else:
    m = input("Bạn đã chich bao giờ chưa? (yes/no)" "\n")
    def StrToBool (m):
        return m.lower() in ("yes")
    if m == 1:
        o = int(input("Bạn chịch lần đầu tiên năm bao nhiêu tuổi" "\n"))
        n = int(input("Bạn chịch của bạn lúc đó bao nhiêu tuổi?" "\n"))
        if o < 18:
            if n < 18:
                print("Cả 2 đều chưa trưởng thành, cả 2 đều có thể phải đi tù đó!")
            else:
                print("Bạn lúc đó chưa trưởng thành, bạn chịch của bạn sẽ phải đi tù!")
        else:
            if n < 18:
                print("Bạn chịch của bạn lúc đó chưa trưởng thành, bạn sẽ phải đi tù!")
            else:
                print("Cả 2 đều đã trưởng thành và có thể chịch thoải mái nhưng hãy biết giữ gìn sức khỏe bản thân và phòng tránh đúng cách nhé!")
    else:
        print("You are a good boy, Chúc bạn gỡ mạng nhện sớm!")
