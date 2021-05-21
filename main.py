from base.player import Player
from base import board
from players import player1 as p1
from players import player2 as p2
from players import player3 as p3
from players import player4 as p4
from players import player5 as p5
import pandas as pd
import random



pVictory = None
def Victory(arr):
    global pVictory
    arr_point = [i.score for i in arr]
    max_point = max(arr_point)
    if max_point >= 15:
      arr_point = [1 if i == max_point else 0 for i in arr_point]
      arr_amount_card = [len(i.card_open) for i in arr]
      min = 100
      for i in range(len(arr_point)):
        if arr_point[i] == 1 and arr_amount_card[i] < min:
          min = arr_amount_card[i]
          pVictory = arr[i]
      return pVictory
    else:
      return None

def save_excel(b ,arr):
  result = {}
  result[b.name + " Stocks"] = b.stocks.copy()
  for i in b.dict_Card_Stocks_Show.keys():
    result[b.name +" "+ i] = [j.id for j in b.dict_Card_Stocks_Show[i]]
  for i in b.dict_Card_Stocks_UpsiteDown.keys():
    result[b.name +"UpsiteDown"+ i] = [j.id for j in b.dict_Card_Stocks_UpsiteDown[i]]
  for i in arr:
    result[i.name + " Score"] = i.score
    result[i.name + " Stocks"] = i.stocks.copy()
    result[i.name + " Stocks Const"] = i.stocks_const.copy()
    result[i.name + " Open"] = [j.id for j in i.card_open]
    result[i.name + " Noble"] = [j.id for j in i.card_noble]
    result[i.name + " Upsite Down"] = [j.id for j in i.card_upside_down]
  return result

df_message = pd.DataFrame({"Action":[]})
arr_message = []
def saveAction(t):
  arr_message.append(t)



def checkNone(b,player,turn):
  saveAction("Lượt: " + str(turn) +" "+player.message)
  if b == None:
    print("Lỗi của :",player.name)
b = board.Board()
b.LoadBase()
b.setupCard()
b.hien_the()
# p1.player_01.setStocks = {
#             "red": 7,
#             "blue": 7,
#             "green": 7,
#             "white": 7,
#             "black": 7,
#             "auto_color": 0,
#         }

# the = b.dict_Card_Stocks_Show["I"][0]
# max = -1
# nguyenlieu = "red"
# the.stocks["red"] = 10
# # if the.stocks[nguyenlieu] > max:
# #   the.stocks[nguyenlieu] = max
# for i in a.stocks.key():
#   a.stocks["red"] = 0

# print(a.stocks)
# b.hien_the()
# Khởi tạo bàn chơi
def RunGame(Luot):
    global pVictory
    pVictory = None
    b = board.Board()
    b.LoadBase()
    b.setupCard()
    turn = 0
    result_turn = []
    arr_stt = [1,2,3,4]
    random.shuffle(arr_stt)
    for i in range(len(arr_stt)):
        if arr_stt[i] == 1:
          p1.player_01.setName = p1.player_01.name +" "+ str(i+1)
        elif arr_stt[i] == 2:
          p2.player_02.setName = p2.player_02.name +" "+ str(i+1)
        elif arr_stt[i] == 3:
          p3.player_03.setName = p3.player_03.name +" "+ str(i+1)
        elif arr_stt[i] == 4:
          p4.player_04.setName = p4.player_04.name +" "+ str(i+1)
    result_turn.append(save_excel(b ,[p1.player_01, p2.player_02, p3.player_03, p4.player_04]))
    while Victory([p1.player_01, p2.player_02, p3.player_03, p4.player_04]) == None:
        print("Lượt:",turn)
        turn+=1
        for i in arr_stt:
          if i == 1:
            b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])
            checkNone(b,p1.player_01,turn)
          elif i == 2:
            b = p2.action(b, [p1.player_01, p3.player_03, p4.player_04])
            checkNone(b,p2.player_02,turn)
          elif i == 3:
            b = p3.action(b, [p1.player_01, p2.player_02, p4.player_04])
            checkNone(b,p3.player_03,turn)
          elif i == 4:
            b = p4.action(b, [p1.player_01, p2.player_02, p3.player_03])
            checkNone(b,p4.player_04,turn)
        a = save_excel(b ,[p1.player_01, p2.player_02, p3.player_03, p4.player_04])
        result_turn.append(a)
    print(pVictory.name)
    data = pd.json_normalize(result_turn,max_level=0)
    data.to_csv(Luot + ".csv", index=False)
    df_message["Action"] = arr_message
    df_message.to_csv("Action"+Luot+".csv",index=False) 
    print("So luong the quy toc con lai",len(b.dict_Card_Stocks_Show["Noble"]))
# RunGame("51")

