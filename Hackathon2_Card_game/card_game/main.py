from game import Game
from player import Player 
import db
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    user = Game()
    user.setup()
    user.guide()
    count=db.get_count()
    if count==None:
        count=0
    option = int(input("Chọn option:"))
    while option != 8:
        if option == 1:
            user.list_players() 
        if option == 2:
            if user.flag == True:
                print("Bạn đang ở trong ván rồi")
            else:
                user.add_player()
        if option == 3:
            if user.flag == True:
                print("Đang trong ván rồi, không thể xóa")
            else:
                user.remove_player()
        if option == 4:
            if user.flag == True:
                print("Bài đã được chia")
            else:
                user.deal_card()
                count=count+1
                db.log(user,count)     
        if option == 5:
            if user.flag == False:
                print("Mời chia bài trước khi lật")
            else:
                for i in user.number:
                    print(f'Người chơi: {i.name} Bộ bài: {i.flip_card()} Điểm: {i.point}')
                print("Người thắng: " +user.flip_card())    
                db.games(user.flip_card(),count)
                for nguoichoi in user.number:
                    nguoichoi.card.clear()
                user.deck.build()
        if option == 6:
           db.get_last_game()
        if option == 7:
            db.history()
        if option == 8:
            break
        user.guide()
        option = int(input("Chọn option:"))

if __name__ == '__main__':
    main()