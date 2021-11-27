#Xử lý chuỗi - Đảo ngược từ và kiểu hoa thường
#Cho 1 chuỗi A (vd: "tHE fOX iS cOMING fOR tHE cHICKEN").
# Viết hàm đảo ngược thứ tự các từ trong chuỗi và đổi tất cả các chữ cái từ hoa thành thường và ngược lại.
#(kết quả là "Chicken The For Coming Is Fox The")

def convert_str(s):
    s1=s.split(" ")
    s2=list(reversed(s1))
    s3=' '.join(s2)
    s3_new=''
    for i in s3:
        if i.isupper():
            s3_new +=i.lower()
        else: s3_new +=i.upper()
    return s3_new

convert_str("tHE fOX iS cOMING fOR tHE cHICKEN")