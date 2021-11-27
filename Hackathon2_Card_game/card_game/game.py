from player import Player
from deck import Deck
class Game:
    '''
    Class chứa các chức năng chính của game
    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.number = []
        self.deck = Deck()
        self.deck.build()
        self.flag=False
    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        while True:
            try:
                number_player = int(input("Mời nhập số người chơi: "))
                if number_player>=2 and number_player<=10:
                    break
                else:
                    print("Bạn chỉ được nhập số người chơi trong khoảng 2-10")
            except:
                print("Thông tin nhập không đúng, mời bạn nhập lại!")
                
            
        name=[]
        for i in range(number_player):
            name_player = input("Nhập tên người chơi thứ " +str(i+1))
            self.number.append(Player(name_player))

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        print("1. Danh sách người chơi")
        print("2. Thêm người chơi")
        print("3. Loại người chơi")
        print("4. Chia bài")
        print("5. Lật bài")
        print("6. Xem lại game vừa chơi")
        print("7. Xem lịch sử chơi hôm nay")
        print("8. Công an tới, tốc biến :)")

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print("Danh sách người chơi là: ")
        for i in self.number:
            print(i.name)

    def add_player(self):
        '''Thêm một người chơi mới'''
        if len(self.number)==10:
            print("Đã đạt số người chơi tối đa")
        else:
            name = input("Nhập tên người chơi mới: ")
            self.number.append(Player(name))

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        if len(self.number)==2:
            print("Trò chơi cần tối thiểu 2 người chơi!")
        else:
            number_player = int(input("Nhập ID người chơi bạn muốn loại: "))
            self.number.pop(number_player)

    def deal_card(self):
        '''Chia bài cho người chơi'''
        self.deck.shuffle_card()
        n = len(self.number)
        for i in range (0,3):
            for player in self.number:
                player.add_card(self.deck.deal_card(self.number.index(player)))
        self.flag=True
        
    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
       
        max_player=""
        max_point = 0
        max_biggis = "" 
        for player in self.number:
            if player.point > max_point: 
               max_player = player.name
               max_point = player.point
               max_biggis = player.biggest_card
            
            elif player.point == max_point:
                if player.biggest_card > max_biggis :
                    max_player = player.name
                    max_point = player.point
                    max_biggis = player.biggest_card
        self.flag=False
        return max_player