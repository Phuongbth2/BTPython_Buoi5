
# Easy [1] Day different:
#Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code. Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05
def day_diff(release,dev_done):
    import datetime
    day_time=datetime.datetime.strptime(release,"%d/%m/%Y")-datetime.datetime.strptime(dev_done,"%Y-%d-%m")
    return day_time
day_diff("19/12/2021","2020-12-10")


#--------------------------------------

# Easy [2] Alphabet and Number:
#Viết hàm alpha_num() tìm tất cả những từ trong một câu có chứa cả chữ cái và số. Trả ra danh sách các từ như vậy trong một câu.
#Vd:
#str1 = "Emma25 is Data scientist50 and AI Expert"
#alpha_num(str1) == ["Emma25", "scientist50"]

def alpha_num(sentence):
    kq=[]
    for k in sentence.split(" "):
        c=list(k)
        i=0
        j=len(c)-1
        while i<len(c):
            if c[i].isalpha()==True and c[j].isnumeric()==True:
                kq.append(k)
                break
            else:
                i+=1
                j-=1
    return kq
alpha_num("Emma25 is Data scientist50 and AI Expert")

#--------------------------------------------------------------------------

# Medium [1] Anagram Number:
#Viết hàm anagram_number() có đầu vào là một số nguyên và trả ra True nếu sau khi đảo ngược thứ tự các chữ số của số đó vẫn cho ta số ban đầu. Trả ra False nếu không giống.
#vd: anagram_number(121121) == True
#    anagram_number(1254) == False
#*args, **kwargs

def anagram_number(number):
    if f"{number}"==f"{number}"[::-1]:
        return True
    return False
    
anagram_number(121121)

#-------------------------------------------------------------
# Medium [2] Roman to Integer
#Các chữ số La Mã được thể hiện bằng bảy biểu tượng khác nhau: I, V, X, L, C, D và M với
#I=1; V=5; X=10; L=50; C=100; D=500; M=1000
#Ví dụ: số 2 được viết là II bằng số La Mã, chỉ là hai chữ I được thêm vào với nhau. 12 được viết là XII, đơn giản là X + II. Con số 27 được viết là XXVII, là XX + V + II.
#Chữ số La mã thường được viết từ lớn nhất đến nhỏ nhất từ trái sang phải. Tuy nhiên, số 4 không viết là IIII mà được viết là IV. Bởi vì I đứng trước V, chúng ta lấy 5 - 1 = 4. Nguyên tắc tương tự cũng áp dụng cho số chín, được viết là IX. Có sáu trường hợp phép trừ được sử dụng:
#I có thể được đặt trước V (5) và X (10) để tạo thành 4 và 9.
#X có thể được đặt trước L (50) và C (100) để tạo ra 40 và 90.
#C có thể được đặt trước D (500) và M (1000) để tạo thành 400 và 900.
#Cho một chữ số la mã dạng string, hãy viết hàm roman_to_int() chuyển nó thành một số nguyên.

def roman_to_int(Str):
    b_list=list(Str)
    print(b_list)
    so=0
    i=0
    for i in range(len(b_list)):
        if i<len(b_list)-1:
            if b_list[i]=="I" and b_list[i+1]=="V":
                so=so+4-5
            elif b_list[i]=="I" and b_list[i+1]=="X":
                so=so+9-10
            elif b_list[i]=="X" and b_list[i+1]=="L":
                so=so+40-50
            elif b_list[i]=="X" and b_list[i+1]=="C":
                so=so+90-100
            elif b_list[i]=="C" and b_list[i+1]=="D":
                so=so+400-500
            elif b_list[i]=="C" and b_list[i+1]=="M":
                so=so+900-1000
            elif b_list[i]=="I":
                so=so+1
            elif b_list[i]=="V":
                so=so+5
            elif b_list[i]=="X":
                so=so+10
            elif b_list[i]=="L":
                so=so+50
            elif b_list[i]=="C":
                so=so+100
            elif b_list[i]=="D":
                so=so+500
            elif b_list[i]=="M":
                so=so+1000
        else:
            if b_list[i]=="I":
                so=so+1
            elif b_list[i]=="V":
                so=so+5
            elif b_list[i]=="X":
                so=so+10
            elif b_list[i]=="L":
                so=so+50
            elif b_list[i]=="C":
                so=so+100
            elif b_list[i]=="D":
                so=so+500
            elif b_list[i]=="M":
                so=so+1000
        i=i+1
    print(so)
roman_to_int("CMX")