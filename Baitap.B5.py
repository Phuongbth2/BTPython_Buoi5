{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 119,
   "source": [
    "# Bài 1: For/While loop và Dictionary/Tuple/Set - Find Pair\r\n",
    "#Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.\r\n",
    "#Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum\r\n",
    "#vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []\r\n",
    "\r\n",
    "print(\"Mời bạn nhập list cần kiểm tra:\")\r\n",
    "list_B1=[]\r\n",
    "list_kq=[]\r\n",
    "tuple_b1=()\r\n",
    "a= (input(\"Mời bạn nhập số, nếu xong nhập done \"))\r\n",
    "while a !=\"done\":\r\n",
    "    a= int(a)\r\n",
    "    list_B1.append(a)\r\n",
    "    a= (input(\"Mời bạn nhập số, nếu xong nhập done \"))\r\n",
    "list_B1=list(list_B1)\r\n",
    "print(\"List bạn vừa nhập là: \",list_B1)\r\n",
    "sum=int(input(\"Nhập số SUM cần check: \"))   \r\n",
    "i=0\r\n",
    "j=1\r\n",
    "while i < len(list_B1):\r\n",
    "    while j < len(list_B1):\r\n",
    "        sum_check=list_B1[i]+list_B1[j]\r\n",
    "        if sum_check==sum:\r\n",
    "            tuple_b1=(list_B1[i],list_B1[j])\r\n",
    "            list_kq.append(tuple_b1)\r\n",
    "        j=j+1\r\n",
    "    i=i+1\r\n",
    "    j=i+1\r\n",
    "\r\n",
    "    print()\r\n",
    "print(\"Cặp số thỏa mãn tổng = \",sum,\" là\",set(list_kq))"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Mời bạn nhập list cần kiểm tra:\n",
      "List bạn vừa nhập là:  [1, 2, 2, 3, 3, 3]\n",
      "Cặp số thỏa mãn tổng =  5  là {(2, 3)}\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "source": [
    "print(\"Mời bạn nhập list cần kiểm tra:\")\r\n",
    "list_B1=[]\r\n",
    "list_kq=[]\r\n",
    "tuple_b1=()\r\n",
    "a= (input(\"Mời bạn nhập số, nếu xong nhập done \"))\r\n",
    "while a !=\"done\":\r\n",
    "    a= int(a)\r\n",
    "    list_B1.append(a)\r\n",
    "    a= (input(\"Mời bạn nhập số, nếu xong nhập done \"))\r\n",
    "list_B1=list(list_B1)\r\n",
    "print(\"List bạn vừa nhập là: \",list_B1)\r\n",
    "sum=int(input(\"Nhập số SUM cần check: \"))  \r\n",
    "for i in range(len(list_B1)):\r\n",
    "    for j in range(i+1,len(list_B1)):\r\n",
    "        sum_check=list_B1[i]+list_B1[j]\r\n",
    "        if sum_check==sum:\r\n",
    "            tuple_b1=(list_B1[i],list_B1[j])\r\n",
    "            list_kq.append(tuple_b1)\r\n",
    "print(\"Cặp số thỏa mãn tổng = \",sum,\" là\",set(list_kq))"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Mời bạn nhập list cần kiểm tra:\n",
      "List bạn vừa nhập là:  [1, 2, 3, 3, 3]\n",
      "Cặp số thỏa mãn tổng =  5  là {(2, 3)}\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 121,
   "source": [
    "# Bài 2: For/While loop và Dictionary/Tuple/Set - Unique value Dictionary\r\n",
    "#Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.\r\n",
    "#VD1:Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.\r\n",
    "#unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]) == {22, 25, 26, 27, 38}\r\n",
    "print(\"Bài 2\")\r\n",
    "print(\"VD1: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ:\") \r\n",
    "print(\"unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]\")\r\n",
    "dict_1=dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)\r\n",
    "mylist_1=list(dict_1.values())\r\n",
    "mylist_unique=list(dict.fromkeys(mylist_1))\r\n",
    "mylist_unique.sort()\r\n",
    "print (\"Set các tuổi duy nhất là: \",mylist_unique)\r\n",
    "\r\n"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Bài 2\n",
      "VD1: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ:\n",
      "unique_value_dict([dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]\n",
      "Set các tuổi duy nhất là:  [22, 25, 26, 27, 38]\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "source": [
    "#VD2: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.\r\n",
    "#unique_value_dict([{\"V\":\"S001\"}, {\"V\": \"S002\"}, {\"VI\": \"S001\"}, {\"VI\": \"S005\"}, {\"VII\":\"S005\"}, {\"V\":\"S009\"},{\"VIII\":\"S007\"}]) == {'S009', 'S007', 'S002', 'S001', 'S005'}\r\n",
    "\r\n",
    "print(\"Bài 2\")\r\n",
    "print(\"VD2: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.\")\r\n",
    "dict2 =[{\"V\":\"S001\"}, {\"V\": \"S002\"}, {\"VI\": \"S001\"}, {\"VI\": \"S005\"}, {\"VII\":\"S005\"}, {\"V\":\"S009\"},{\"VIII\":\"S007\"}]\r\n",
    "print (dict2)\r\n",
    "list_unique_none=[]\r\n",
    "i=0\r\n",
    "\r\n",
    "for diction in dict2:\r\n",
    "    a=list(dict2[i].values())\r\n",
    "    list_unique_none.append(a)\r\n",
    "    i=i+1\r\n",
    "mylist_unique_3=list(list_unique_none)\r\n",
    "z=0\r\n",
    "while z< len(mylist_unique_3):\r\n",
    "    s=mylist_unique_3.count(mylist_unique_3[z])\r\n",
    "    if s>1:\r\n",
    "        mylist_unique_3.remove(mylist_unique_3[z])\r\n",
    "        \r\n",
    "    z=z+1\r\n",
    "print(\"List value unique là: \",mylist_unique_3)"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Bài 2\n",
      "VD2: Trường hợp dưới đây danh sách đầu vào có 7 dicts, mỗi dict chỉ có 1 cặp key-values. 5 giá trị trả về là duy nhất.\n",
      "[{'V': 'S001'}, {'V': 'S002'}, {'VI': 'S001'}, {'VI': 'S005'}, {'VII': 'S005'}, {'V': 'S009'}, {'VIII': 'S007'}]\n",
      "List value unique là:  [['S002'], ['S001'], ['S005'], ['S009'], ['S007']]\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 128,
   "source": [
    "#Bài 3: For/While loop và Dictionary/Tuple/Set - Đếm ngược đến XMas\r\n",
    "#Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.\r\n",
    "#vd in ra sau mỗi 5s:\r\n",
    "#Countdown to Xmas 2021: 112 days, 11:47:01.339588\r\n",
    "#Countdown to Xmas 2021: 112 days, 11:46:56.324008\r\n",
    "#Countdown to Xmas 2021: 112 days, 11:46:51.310473\r\n",
    "from time import sleep\r\n",
    "from datetime import datetime\r\n",
    "date_Xmas = \"12-25-2021 00:00:00\"\r\n",
    "Xmas_string = \"%m-%d-%Y %H:%M:%S\"\r\n",
    "Xmas_time=datetime.strptime(date_Xmas,Xmas_string)\r\n",
    "Xmas_timestamp=datetime.timestamp(Xmas_time)\r\n",
    "\r\n",
    "\r\n",
    "while True:\r\n",
    "    # Get current time\r\n",
    "    currTime = datetime.now()\r\n",
    "    curr_string = currTime.strftime(\"%d/%m/%Y %H:%M:%S\")\r\n",
    "    curr_timestamp=datetime.timestamp(currTime)\r\n",
    "    Count_down_stamp=(Xmas_timestamp- curr_timestamp)\r\n",
    "    Count_down=datetime.fromtimestamp(Count_down_stamp)\r\n",
    "    Count_down_date = Count_down.strftime(\"%j\")\r\n",
    "    Count_down_hour=Count_down.strftime(\" %H:%M:%S.%f\")\r\n",
    "    print(\"Thời gian hiện tại là: \", curr_string)\r\n",
    "    print(\"Countdown to Xmas 2021: \",Count_down_date,\" giờ\",Count_down_hour)\r\n",
    "    print(\"\")\r\n",
    "    sleep(5)\r\n",
    "\r\n"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Thời gian hiện tại là:  06/09/2021 23:24:57\n",
      "Countdown to Xmas 2021:  110  giờ  07:35:02.966388\n",
      "\n",
      "Thời gian hiện tại là:  06/09/2021 23:25:02\n",
      "Countdown to Xmas 2021:  110  giờ  07:34:57.962477\n",
      "\n",
      "Thời gian hiện tại là:  06/09/2021 23:25:07\n",
      "Countdown to Xmas 2021:  110  giờ  07:34:52.955911\n",
      "\n"
     ]
    },
    {
     "output_type": "error",
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\PHUONG~1\\AppData\\Local\\Temp/ipykernel_3688/258169328.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     25\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Countdown to Xmas 2021: \"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mCount_down_date\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m\" giờ\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mCount_down_hour\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     26\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 27\u001b[1;33m     \u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     28\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 129,
   "source": [
    "#Bài 4: Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list\r\n",
    "#my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]\r\n",
    "#Trả ra: {10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}\r\n",
    "my_list_4 = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]\r\n",
    "print(\"Có list số: \",my_list_4)\r\n",
    "mylist_4_unique=list(dict.fromkeys(my_list_4))\r\n",
    "my_dict_4={}\r\n",
    "i=0\r\n",
    "while i< len(mylist_4_unique):\r\n",
    "    my_dict_4[mylist_4_unique[i]]=my_list_4.count(mylist_4_unique[i])\r\n",
    "    i=i+1\r\n",
    "print(\"List từ điển với key là các số trong list, value là số lần xuất hiện của số trong list tương ứng là: \")\r\n",
    "print(my_dict_4)"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Có list số:  [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]\n",
      "List từ điển với key là các số trong list, value là số lần xuất hiện của số trong list tương ứng là: \n",
      "{10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "source": [
    "#Bài 5: Print Star\r\n",
    "#Hãy viết chương trình in ra các hình sau (dùng ký tự '*' và ký tự space) với n là số dòng. Vd: n = 4:\r\n",
    "\r\n",
    "print(\"Bài 5 - Hình 1 - Print Star\")\r\n",
    "n=int(input(\"Mời bạn nhập số dòng muốn vẽ: \"))\r\n",
    "print(\"Tôi muốn vẽ \",n,\" dòng\")\r\n",
    "i=1\r\n",
    "while i<=n:\r\n",
    "    star=i*' *'\r\n",
    "    space=(n-i)*\"  \"\r\n",
    "    print(space,star)\r\n",
    "    i=i+1\r\n",
    "print (\"\")\r\n",
    "print (\"\")"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Bài 5 - Hình 1\n",
      "Mời bạn nhập số dòng muốn vẽ:\n",
      "Tôi muốn vẽ  4  dòng\n",
      "        *\n",
      "      * *\n",
      "    * * *\n",
      "  * * * *\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 130,
   "source": [
    "print(\"Bài 5 - Hình 2 - Print star\")\r\n",
    "n=int(input(\"Mời bạn nhập số dòng muốn vẽ: \"))\r\n",
    "print(\"Tôi muốn vẽ \",n,\" dòng\")\r\n",
    "i=1\r\n",
    "while i<n:\r\n",
    "    star=i*' *'\r\n",
    "    space=(n-1-i)*\"  \"\r\n",
    "    print(space,star)\r\n",
    "    i=i+1\r\n",
    "print((n*2)*'* ')\r\n",
    "j=n*2-1\r\n",
    "while 0<j<2*n:\r\n",
    "    star_2=(j-n)*'* '\r\n",
    "    space_2=(2*n-1-j)*\"  \"\r\n",
    "    print((n-1)*\"  \",star_2,space_2)\r\n",
    "    j=j-1\r\n",
    "\r\n"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "Bài 5 - Hình 2 - Print star\n",
      "Tôi muốn vẽ  8  dòng\n",
      "              *\n",
      "            * *\n",
      "          * * *\n",
      "        * * * *\n",
      "      * * * * *\n",
      "    * * * * * *\n",
      "  * * * * * * *\n",
      "* * * * * * * * * * * * * * * * \n",
      "               * * * * * * *  \n",
      "               * * * * * *    \n",
      "               * * * * *      \n",
      "               * * * *        \n",
      "               * * *          \n",
      "               * *            \n",
      "               *              \n",
      "                              \n",
      "                                \n",
      "                                  \n",
      "                                    \n",
      "                                      \n",
      "                                        \n",
      "                                          \n",
      "                                            \n"
     ]
    }
   ],
   "metadata": {}
  }
 ],
 "metadata": {
  "orig_nbformat": 4,
  "language_info": {
   "name": "python",
   "version": "3.7.8",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.8 64-bit"
  },
  "interpreter": {
   "hash": "04635d289a519a1410467dd0afb0db42f9184808881ca68b2eb5a687a20a5a94"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}