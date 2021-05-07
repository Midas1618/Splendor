from base import board
from players import player1 as p1
from players import player2 as p2
from players import player3 as p3
from players import player4 as p4

# khởi tạo bàn chơi
b = board.Board()
b.LoadBase()
b.setupCard()

b.hien_the()
b = p1.action(b,[p2.player_02,p3.player_03,p4.player_04])
print(b.stocks)
print(p1.player_01.stocks)
print("----")
b.hien_the()
b = p1.action(b,[p2.player_02,p3.player_03,p4.player_04])
print(b.stocks)
print(p1.player_01.stocks)
print("----")
b.hien_the()
b = p1.action(b,[p2.player_02,p3.player_03,p4.player_04])
print(b.stocks)
print(p1.player_01.stocks)
print("----")
b.hien_the()
b = p1.action(b,[p2.player_02,p3.player_03,p4.player_04])
print(b.stocks)
print(p1.player_01.stocks)
print("----")
for i in p1.player_01.card_upside_down:
  print(i.id)
# Bắt đầu chơi
# while True:
#   Board = player2.action(Board,[p1.player_01,p3.player_03,p4.player_04])
#   Board = player3.action(Board,[p1.player_01,p2.player_02,p4.player_04])
#   Board = player4.action(Board,[p1.player_01,p2.player_02,p3.player_03])

