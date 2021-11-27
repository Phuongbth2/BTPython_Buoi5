#Bài tập OOP buổi 1
#Thay đổi các thuộc tính account_number, account_name, balance trong class BankAccount thành thuộc tính ẩn, và triển khai thêm các phương thức:
#get_account_number()
#get_account_name()
#get_balance()
#set_balance() - balance phải lớn hơn hoặc bằng 0
#Thay đổi các phương thức display(), withdraw() và deposit() sử dụng các phương thức getter và setter trên.
#Chú ý:Với withdraw(), amount phải lớn hơn 0 và nhỏ hơn balance
# Với deposit(), amount phải lớn hơn 0
# Nếu giá trị không phù hợp thì thông báo ra console

class BankAccount:
    def __init__(self, account_number, account_name, balance):
        self._account_number = account_number
        self._account_name = account_name
        self.set_balance(balance)

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    def set_balance(self, new_balance):
        if new_balance >0:
            self._balance = new_balance
        else:
            print("Tài khoản đang bị âm")     

    def display(self):
        print(f"Thông tin tài khoản: {self.account_number}, {self.account_name}, {self.balance}")

    def withdraw(self, amount):
        if 0 < amount < self.balance:
            self._balance -= amount
        else:
            print("Số dư không đủ")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
        else:
            print("Không hợp lệ")
    

bank_account = BankAccount("99990000088888", "Phuongbth2", 1000000) 
bank_account.display() 

bank_account.withdraw(5000)
bank_account.display() 

bank_account.deposit(6000)
bank_account.display() 

bank_account.withdraw(1200000)