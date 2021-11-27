'''Kết nối CSDL'''
from pymysql import connect, cursors, Error
import game as ga
from datetime import datetime
from datetime import date
config = {
  'host': 'localhost',
  'user': 'root',
  'password': '',
  'database': 'cardgame',
  }
cnx = connect(**config)

def log(game_info,count):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs
    Bảng games gồm tên người chiến thắng
    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game
    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''  
    for i in game_info.number:
        sql="INSERT INTO logs(player, cards, point, biggest_card,count) VALUES (%s,%s,%s,%s,%s)"
        value=(i.name, i.flip_card(), i.point, i.biggest_card,count)
        cur = cnx.cursor()    
        try:
            cur.execute(sql,value)
            cnx.commit()
        except:
            cnx.rollback()
def games(winner_name,count):
    sql="INSERT INTO `game`(`name_win`, `count`, `time`) VALUES (%s,%s,%s)"
    value=(winner_name, count, datetime.now())
    cur = cnx.cursor()    
    try:
        cur.execute(sql,value)
        cnx.commit()
    except:
        cnx.rollback()
def get_count():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    sql="SELECT MAX(count) as count1 FROM `logs` "
    cur = cnx.cursor()
    cur.execute(sql)
    for i in cur:
        result= i[0]
    return result
    

def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    sql="SELECT name_win,time FROM `game` WHERE `count`=(SELECT max(count) FROM game)"
    cur1 = cnx.cursor()
    cur1.execute(sql)
    for i in cur1:
       print(i[1])
       print(f"Người chiến thắng: {i[0]}")
    sql1="SELECT * FROM `logs` WHERE `count`=(SELECT max(count) FROM logs)"
    cur = cnx.cursor()
    cur.execute(sql1)
    for i in cur:
       print(f"Người chơi: {i[1]} Bộ bài: {i[2]} Điểm: {i[3]} Lá bài lớn nhất: {i[4]}")

      #  
def history():
    '''
    Lấy thông tin về lịch sử chơi
    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    sql=f"SELECT COUNT(id) as tong FROM `game` where time like '{date.today()}%'"
    cur = cnx.cursor()
    cur.execute(sql)
    for i in cur:
        print(f"Tổng số game đã chơi trong ngày: {i[0]}")
    sql1=f"SELECT name_win,COUNT(name_win) as tong FROM game where time like '{date.today()}%' GROUP BY name_win"
    cur1 = cnx.cursor()
    cur1.execute(sql1)
    for i in cur1:
        print(f"Người chơi: {i[0]}| ,số bàn thắng: {i[1]}")