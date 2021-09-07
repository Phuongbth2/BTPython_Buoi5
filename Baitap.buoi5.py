 Bài 1: For/While loop và Dictionary/Tuple/Set - Find Pair
#Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.
#Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum
#vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []

print("Mời bạn nhập list cần kiểm tra:")
list_B1=[]
list_kq=[]
tuple_b1=()
a= (input("Mời bạn nhập số, nếu xong nhập done "))
while a !="done":
    a= int(a)
    list_B1.append(a)
    a= (input("Mời bạn nhập số, nếu xong nhập done "))
list_B1=list(list_B1)
print("List bạn vừa nhập là: ",list_B1)
sum=int(input("Nhập số SUM cần check: "))   
i=0
j=1
while i < len(list_B1):
    while j < len(list_B1):
        sum_check=list_B1[i]+list_B1[j]
        if sum_check==sum:
            tuple_b1=(list_B1[i],list_B1[j])
            list_kq.append(tuple_b1)
        j=j+1
    i=i+1
    j=i+1

    print()
print("Cặp số thỏa mãn tổng = ",sum," là",set(list_kq))

#Cách 2 Dùng for
print("Mời bạn nhập list cần kiểm tra:")
list_B1=[]
list_kq=[]
tuple_b1=()
a= (input("Mời bạn nhập số, nếu xong nhập done "))
while a !="done":
    a= int(a)
    list_B1.append(a)
    a= (input("Mời bạn nhập số, nếu xong nhập done "))
list_B1=list(list_B1)
print("List bạn vừa nhập là: ",list_B1)
sum=int(input("Nhập số SUM cần check: "))  
for i in range(len(list_B1)):
    for j in range(i+1,len(list_B1)):
        sum_check=list_B1[i]+list_B1[j]
        if sum_check==sum:
            tuple_b1=(list_B1[i],list_B1[j])
            list_kq.append(tuple_b1)
print("Cặp số thỏa mãn tổng = ",sum," là",set(list_kq))

# Bài 2: For/While loop và Dictionary/Tuple/Set - Unique value Dictionary
#Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.
#VD1:Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.
#unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}
print("Bài 2")
print("VD1: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ:") 
print("unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]")
dict_1=dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)
mylist_1=list(dict_1.values())
mylist_unique=list(dict.fromkeys(mylist_1))
mylist_unique.sort()
print ("Set các tuổi duy nhất là: ",mylist_unique)

#VD2: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.
#unique_value_dict([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}

print("Bài 2")
print("VD2: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.")
dict2 =[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print (dict2)
list_unique_none=[]
i=0

for diction in dict2:
    a=list(dict2[i].values())
    list_unique_none.append(a)
    i=i+1
mylist_unique_3=list(list_unique_none)
z=0
while z< len(mylist_unique_3):
    s=mylist_unique_3.count(mylist_unique_3[z])
    if s>1:
        mylist_unique_3.remove(mylist_unique_3[z])
        
    z=z+1
print("List value unique là: ",mylist_unique_3)


#Bài 3: For/While loop và Dictionary/Tuple/Set - Đếm ngược đến XMas
#Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.
#vd in ra sau mỗi 5s:
#Countdown to Xmas 2021: 112 days, 11:47:01.339588
#Countdown to Xmas 2021: 112 days, 11:46:56.324008
#Countdown to Xmas 2021: 112 days, 11:46:51.310473
from time import sleep
from datetime import datetime
date_Xmas = "12-25-2021 00:00:00"
Xmas_string = "%m-%d-%Y %H:%M:%S"
Xmas_time=datetime.strptime(date_Xmas,Xmas_string)
Xmas_timestamp=datetime.timestamp(Xmas_time)


while True:
    # Get current time
    currTime = datetime.now()
    curr_string = currTime.strftime("%d/%m/%Y %H:%M:%S")
    curr_timestamp=datetime.timestamp(currTime)
    Count_down_stamp=(Xmas_timestamp- curr_timestamp)
    Count_down=datetime.fromtimestamp(Count_down_stamp)
    Count_down_date = Count_down.strftime("%j")
    Count_down_hour=Count_down.strftime(" %H:%M:%S.%f")
    print("Thời gian hiện tại là: ", curr_string)
    print("Countdown to Xmas 2021: ",Count_down_date," giờ",Count_down_hour)
    print("")
    sleep(5)


    #Bài 4: Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list
#my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
#Trả ra: {10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}
my_list_4 = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
print("Có list số: ",my_list_4)
mylist_4_unique=list(dict.fromkeys(my_list_4))
my_dict_4={}
i=0
while i< len(mylist_4_unique):
    my_dict_4[mylist_4_unique[i]]=my_list_4.count(mylist_4_unique[i])
    i=i+1
print("List từ điển với key là các số trong list, value là số lần xuất hiện của số trong list tương ứng là: ")
print(my_dict_4)


#Bài 5: Print Star
#Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:

print("Bài 5 - Hình 1 - Print Star")
n=int(input("Mời bạn nhập số dòng muốn vẽ: "))
print("Tôi muốn vẽ ",n," dòng")
i=1
while i<=n:
    star=i*' *'
    space=(n-i)*"  "
    print(space,star)
    i=i+1
print ("")
print ("")


print("Bài 5 - Hình 2 - Print star")
n=int(input("Mời bạn nhập số dòng muốn vẽ: "))
print("Tôi muốn vẽ ",n," dòng")
i=1
while i<n:
    star=i*' *'
    space=(n-1-i)*"  "
    print(space,star)
    i=i+1
print((n*2)*'* ')
j=n*2-1
while 0<j<2*n:
    star_2=(j-n)*'* '
    space_2=(2*n-1-j)*"  "
    print((n-1)*"  ",star_2,space_2)
    j=j-1

