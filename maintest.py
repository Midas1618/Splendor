from base import board
from players import player1 as p1
from players import player2 as p2
from players import player3 as p3
from players import player4 as p4
import pandas as pd
pVictory = None

def Victory(arr):
    arr_point = [i.score for i in arr]
    max_point = max(arr_point)
    if max_point > 15:
      arr_point = [1 if i == max else 0 for i in arr_point]
      arr_amount_card = [len(i.card_open) for i in arr]
      for i in len(arr_point):
        if arr_point[i] == 1 and arr_amount_card[i] < min:
          min = arr_amount_card[i]
          pVictory = arr[i]
      return pVictory
    else:
      return None

def save_excel(b ,arr):
  result = {}
  result[b.name + " Stocks"] = b.stocks
  for i in b.dict_Card_Stocks_Show.keys():
    result[b.name +" "+ i] = [j.id for j in b.dict_Card_Stocks_Show[i]]
  for i in arr:
    result[i.name + " Score"] = i.score
    result[i.name + " Stocks"] = i.stocks
    result[i.name + " Stocks Const"] = i.stocks_const
    result[i.name + " Open"] = [j.id for j in i.card_open]
    result[i.name + " Upsite Down"] = [j.id for j in i.card_upside_down]
  return result

# Khởi tạo bàn chơi

b = board.Board()
b.LoadBase()
b.setupCard()
turn = 1
result_turn = []
# b.hien_the()

def nguyenlieucannhat():
  nguyenlieucannhat = None
  soluongcan = 0
  for nguyenlieu in p1.player_01.card_upside_down[0].stocks.keys():
    if p1.player_01.card_upside_down[0].stocks[nguyenlieu] > soluongcan:
      soluongcan = p1.player_01.card_upside_down[0].stocks[nguyenlieu]
      nguyenlieucannhat = nguyenlieu
  return nguyenlieucannhat
def nguyenlieucon():
  nguyenlieucon = []
  for nguyenlieu in b.stocks.keys():
    if b.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color" and nguyenlieu != nguyenlieucannhat():
      nguyenlieucon.append(nguyenlieu)
  return nguyenlieucon
def nguyenlieucannhi():
  luongnguyenlieu = 10
  nguyenlieuthu2 = None
  for nguyenlieu in nguyenlieucon():
    if p1.player_01.card_upside_down[0].stocks[nguyenlieu]>0:
      return nguyenlieu
      luongnguyenlieu = -1
      break
    else:
      if b.stocks[nguyenlieu] < luongnguyenlieu:
        luongnguyenlieu = b.stocks[nguyenlieu]
        nguyenlieuthu2 = nguyenlieu
  if luongnguyenlieu != -1:
    return nguyenlieuthu2
def nguyenlieucanba():
  luongnguyenlieu = 10
  nguyenlieuthu3 = None
  for nguyenlieu in nguyenlieucon():
    if nguyenlieu != nguyenlieucannhi():
      if p1.player_01.card_upside_down[0].stocks[nguyenlieu]>0:
        return nguyenlieu
        luongnguyenlieu = -1
        break
      else:
        if b.stocks[nguyenlieu] < luongnguyenlieu:
          luongnguyenlieu = b.stocks[nguyenlieu]
          nguyenlieuthu3 = nguyenlieu
  if luongnguyenlieu != -1:
    return nguyenlieuthu3
#turn1
#nếu k có thẻ nào trên tay:
def moiturn():
  global b
  if len(p1.player_01.card_upside_down) == 0:
    thesenhat = None
    for a in b.dict_Card_Stocks_Show["III"]:
      if sum(a.stocks.values()) == 7:
        thesenhat = a
    for a in b.dict_Card_Stocks_Show["III"]:
      if sum(a.stocks.values()) == 10:
        thesenhat = a
    if thesenhat != None:
      b = p1.player_01.getUpsideDown(thesenhat,b,{})
    else:
      IIlonnhat = -1
      for a in b.dict_Card_Stocks_Show["II"]:
        if a.score > IIlonnhat:
          IIlonnhat = a.score
          thesenhat = a
      b = p1.player_01.getUpsideDown(thesenhat,b,{})
  else:
    # mua thẻ
    if p1.player_01.checkGetCard(p1.player_01.card_upside_down[0]) == True:
      print("mua thẻ")
      p1.player_01.getCard(p1.player_01.card_upside_down[0],b)
    #nhặt nguyên liệu
    #nhặt 2 nguyên liệu
    else:
      if p1.player_01.checkOneStock(b,nguyenlieucannhat()) == True:
        p1.player_01.getOneStock(nguyenlieucannhat(),b,{})
      else:
        #úp thẻ nếu có từ 9 nguyên liệu trở lên
        # tìm nguyên liệu dư
        if sum(p1.player_01.stocks.values()) > 8:
          for nguyenlieu in p1.player_01.stocks.keys():
            if p1.player_01.card_upside_down[0].stocks[nguyenlieu] == 0:
              bo1 = {nguyenlieu:1}
              break
          theseup = None
          for the in b.dict_Card_Stocks_Show["III"]:
            if sum(the.stocks.values()) == 7:
              theseup = the
          for the in b.dict_Card_Stocks_Show["III"]:
            if sum(the.stocks.values()) == 10:
              theseup = the
          if theseup != None:
            b = p1.player_01.getUpsideDown(theseup,b,bo1)
          else:
            IIlon = 0
            for the in b.dict_Card_Stocks_Show["II"]:
              if the.score > IIlon:
                IIlon = the.score
                theseup = the
            b = p1.player_01.getUpsideDown(theseup,b,bo1)
      # nhặt 3 nguyên liệu
        else:
          if p1.player_01.checkThreeStocks(b,nguyenlieucannhat(),nguyenlieucannhi(),nguyenlieucanba()) == True:
            bo = {}
            if sum(p1.player_01.stocks.values()) ==8:
              bo = {nguyenlieucanba():1}
            p1.player_01.getThreeStocks(nguyenlieucannhat(),nguyenlieucannhi(),nguyenlieucanba(),b,bo)
b.hien_the() 
for turn in range(7):
  print("Lượt: ",turn)
  # print(p1.player_01.stocks)
  moiturn()
  # print("NL Người chơi: ", p1.player_01.stocks)
# print(p1.player_01.card_upside_down[0].stocks)
  print("Điểm :", p1.player_01.score)
  # print("----------------------------")
# b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])
# print("done")
# b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])

# print(p1.player_01.stocks)
# print(b.stocks)


# while Victory([p1.player_01, p2.player_02, p3.player_03, p4.player_04]) == None:
#     print(turn)
#     b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])
#     b = p2.action(b, [p1.player_01, p3.player_03, p4.player_04])
#     b = p3.action(b, [p1.player_01, p2.player_02, p4.player_04])
#     b = p4.action(b, [p1.player_01, p2.player_02, p3.player_03])
#     turn += 1
#     result_turn.append({ "Turn": turn,
#     "Data" : save_excel(b ,[p1.player_01, p2.player_02, p3.player_03, p4.player_04])})

# data = pd.json_normalize(result_turn,max_level=1)
# data.to_csv("test.csv", index=False)