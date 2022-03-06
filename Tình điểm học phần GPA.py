#Bài toán tính điểm tổng kết học phần với hệ số(m,n,p) không cố định
m=1
n=3
p=6
print("Nhập vào điểm đánh giá quá trình của bạn")
a=float(input())
if a<0 or a>10:
    print("Bạn đã nhập sai, hãy nhập lại")
else:
    print("Nhập vào điểm điểm tra giữa học phần của bạn")
    b=float(input())
    if b<0 or b>10:
        print("Bạn đã nhập sai, hãy nhập lại")
    else:
        print("Nhập vào điểm kết thúc học phần của bạn")
        c = float(input())
        if c<0 or c>10:
            print("Bạn đã nhập sai, hãy nhập lại")
        else:
            aver=round(((a*m+b*n+c*p)/10), 2)
            if aver<4:
                print("Bạn đã trượt môn học này, điểm GPA là 0, điểm học phần là F")
            elif 4<=aver<5:
                print("Điểm trung bình của bạn là ",aver,"Điểm TB môn là 1, điểm học phần là D")
            elif 5<=aver<5.5:
                print("Điểm trung bình của bạn là ",aver,"Điểm TB môn là 1.5, điểm học phần là D+")
            elif 5.5<=aver<6.5:
                print("Điểm trung bình của bạn là ",aver,"Điểm TB môn là ",round(((aver+0.5)/3), 2),", điểm học phần là C")
            elif 6.5<=aver<7:
                print("Điểm trung bình của bạn là ",aver,"Điểm TB môn là ",round(((aver+0.5)/3), 2),", điểm học phần là C+")
            elif 7<=aver<8:
                print("Điểm trung bình của bạn là ", aver,"Điểm TB môn là ",round(((aver-3.45)/1.42), 2),", điểm học phần là B")
            elif 8<=aver<8.5:
                print("Điểm trung bình của bạn là ", aver, "Điểm TB môn là ",round((aver/2.5), 2),", điểm học phần là B+")
            elif 8.5<=aver<9.5:
                print("Điểm trung bình của bạn là ", aver, "Điểm TB môn là ",round((aver/2.5), 2),", điểm học phần là A")
            else:
                print("Điểm trung bình của bạn là ", aver, "Điểm TB môn là ",round((aver/2.5), 2),", điểm học phần là A+")
