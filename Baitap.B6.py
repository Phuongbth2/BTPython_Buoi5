#Bài 1: Function - Chỉ số thống kê mô tả
#Cho một list A các điểm thi (từ 0-10) của các học viên trong lớp. Viết 3 hàm tính:
#giá trị trung bình (mean) của dãy.
#trung vị (median) của dãy A. trung vị là một số đứng ở vị trí giữa trong dãy số đã được sắp xếp theo thứ tự tăng dần, median chia dãy số cho trước thành 2 nửa bằng nhau. Nếu độ dài của dãy số là số lẻ, thì số ở giữa là median, nếu chiều dài của dãy số là số chẵn thì median được xác định bằng cách lấy trung bình của hai số ở giữa.
#mode của dãy A. Mode là phần tử có số lần xuất hiện nhiều nhất trong dãy. Mode sẽ giúp ta trả lời câu hỏi: "Trong lớp này, học viên đạt Điểm số nào nhiều nhất?".
#Lưu ý: kết quả trả ra sẽ là 1 list vì mode có thể nhiều hơn 1 giá trị.

n=int(input("Nhập sĩ số học sinh của lớp:"))
lists=[]
for i in range(0,n):
    points=int(input("Nhập điểm số"))
    lists.append(points)
print ("Danh sách điểm môn toán của lớp: ",lists)
def Mean(a):
    if len(a)==0:
        return "Danh sách rỗng"
    else:
        return round(sum(a)/len(a),1)
Mean(lists)

def Median(b):
    b.sort()
    if len(b)%2!=0:
        return b[round(len(b)/2)]
    else:
        return (b[int(len(b)/2)]+b[int(len(b)/2-1)])/2

Median(lists)

def Mode(c):
    c.sort()
    my_dict={}
    count_max=[]
    for i in c:
        my_dict[i]=c.count(i)
    my_val=list(my_dict.values())
    my_keys=list(my_dict.keys())
    for i in range (len(my_val)):
        if my_val[i]==max(my_val):
            count_max.append(my_keys[i])
            i+=i
    return count_max
Mode(lists)
print("Kết quả Mean, Median, Mode là: ",(Mean(lists),Median(lists),Mode(lists)))


#Bài 2: Function - Đếm loại ký tự
#Viết hàm có đầu vào là 1 chuỗi, trả ra số chữ cái, số ký tự viết hoa, số ký tự viết thường và số chữ số trong chuỗi đó. Giả sử đầu vào sau được cấp cho hàm: s = "Hello World! 123"
#Hàm count_char_type(s) sẽ trả ra 1 dict {"LETTERS":10, "CASE": {"UPPER CASE":2, "LOWER CASE":8}, "DIGITS":3}. Lưu ý: value của key "CASE" là một dict có 2 keys là "UPPER CASE", "LOWER CASE".
#a) Viết hàm trên dùng bất kỳ hàm built in nào của python

s=input("Mời bạn nhập chuỗi")
print("Chuỗi bạn vừa nhập vào là: ",s)
def count_char_type(a):
    count_letters=0
    count_upper=0
    count_lower=0
    count_digits=0
    for i in a:
        if i.isalpha():
            count_letters+=1
        if i.isupper():
            count_upper+=1
        if i.islower():
            count_lower+=1
        if i.isnumeric():
            count_digits+=1
    mydict={"LETTERS":count_letters,"CASE":{"UPPER CASE":count_upper,"LOWER CASE":count_lower},"DIGITS":count_digits}
    print("Kết quả hàm count_char_type: ",mydict)
count_char_type(s)