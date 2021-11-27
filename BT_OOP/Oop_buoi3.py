#Khai báo class SavingAccount kế thừa từ BankAccount
class BankAccount:
    def __init__(self,account_number,owner, balance):
        self._account_number = account_number
        self._owner = owner
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
 
    def display(self):
         print(
            f"Thông tin KH: {self._owner.get_info()}\nSố tài khoản {self.account_number}\nSố dư: {self.balance}")

 
class SavingAccount(BankAccount):
    monthly_interest_rate = 0.005
   
    def calculate_interest(self):
        return self.monthly_interest_rate*self.balance

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone = phone

    def get_info(self):
        return f"{self.name}, {self.date_of_birth}, {self.email}, {self.phone}"    

Customer_NO1 = Customer("Bùi Thị Hồng Phương","14/11/1992","hongphuong.hvnh@gmail.com","0988122222")
bank_account = SavingAccount("123456789001", Customer_NO1,100000000) 
bank_account.display() 
print(f"Lãi mỗi tháng KH nhận được: {bank_account.calculate_interest()}")   

print("-"*100)
Customer_NO2 = Customer("Nguyễn Khắc Tuệ Minh","14/11/1992","phuongbth2@gmail.com","0987777666")
bank_account = SavingAccount("123456789002", Customer_NO2,500000000) 
bank_account.display() 
print(f"Lãi mỗi tháng KH nhận được: {bank_account.calculate_interest()}")   