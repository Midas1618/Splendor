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
# Tạo gốc chơi
result_turn = []
turn = 1

b.hien_the()
print(b.stocks)
print(p1.player_01.stocks)
print(p1.player_01.card_upside_down)

# nguyên liệu còn 
def nguyenlieuconlai():
  nguyenlieucon = []
  for nguyenlieu in b.stocks:
    if b.stocks[nguyenlieu] > 0:
      nguyenlieucon.append(nguyenlieu)
  nguyenlieucon.remove("auto_color")
  return nguyenlieucon
def nguyenlieucan():
  nguyenlieucan = {}
  for nguyenlieuconxot in nguyenlieuconlai():
    if p1.player_01.card_upside_down[0].stocks[nguyenlieuconxot] > 0:
      nguyenlieucan[nguyenlieuconxot] = p1.player_01.card_upside_down[0].stocks[nguyenlieuconxot]
  return nguyenlieucan
def nguyenlieucannhat():
  luongcan = 0
  nguyenlieucannhat = None
  for nguyenlieu in nguyenlieucan().keys():
    if nguyenlieucan()[nguyenlieu] >luongcan:
      luongcan = nguyenlieucan()[nguyenlieu]
      nguyenlieucannhat = nguyenlieu
  return nguyenlieucannhat
def nguyenlieucannhi():
  if len(nguyenlieucan()) > 1:
    for nguyenlieu in nguyenlieucan():
      if nguyenlieu != nguyenlieucannhat():
        if p1.player_01.card_upside_down[0].stocks[nguyenlieu] > p1.player_01.stocks[nguyenlieu]:
          break
    return nguyenlieu
  else:
    songuyenlieu = 10
    nguyenlieunhi = None
    for nguyenlieu in nguyenlieuconlai():
      if b.stocks[nguyenlieu] < songuyenlieu:
        songuyenlieu = b.stocks[nguyenlieu]
        nguyenlieunhi = nguyenlieu
    return nguyenlieunhi
def nguyenlieuthuba():
  if len(nguyenlieucan()) ==3:
    for nguyenlieuba in nguyenlieucan():
      if nguyenlieuba != nguyenlieucannhat() and nguyenlieuba != nguyenlieucannhi() and nguyenlieuba in nguyenlieuconlai():
        return nguyenlieuba
  else:
    soluong = 10
    nguyenlieu3 = None
    for nguyenlieuitnhat in nguyenlieuconlai():
      if b.stocks[nguyenlieuitnhat] <soluong and nguyenlieuitnhat != nguyenlieucannhat() and nguyenlieuitnhat != nguyenlieucannhi():
        soluong = b.stocks[nguyenlieuitnhat]
        nguyenlieu3 = nguyenlieuitnhat
    return nguyenlieu3
def nguyenlieubo1():
  bo = {}
  for nguyenlieu in [nguyenlieucannhat(),nguyenlieucannhi(),nguyenlieuthuba()]:
    if nguyenlieu not in nguyenlieucan():
      bo[nguyenlieu] = 1
      break
  return bo
def nguyenlieubo2():
  bo = {}
  for nguyenlieu in [nguyenlieucannhat(),nguyenlieucannhi(),nguyenlieuthuba()]:
    if nguyenlieu not in nguyenlieucan():
      bo[nguyenlieu] = 1
  if len(bo) == 1:
    for nguyenlieu in p1.player_01.stocks.keys():
      if nguyenlieu not in nguyenlieucan():
        if nguyenlieu in bo.keys():
          bo[nguyenlieu] = 2
        else:
          bo[nguyenlieu] = 1
        break
  return bo
def nguyenlieubo3():
  bo = nguyenlieubo2()
  for nguyenlieu in p1.player_01.stocks.keys():
    if nguyenlieu not in nguyenlieucan():
      if nguyenlieu in bo.keys():
        if nguyenlieu not in nguyenlieubo1():
          if p1.player_01.stocks[nguyenlieu] > bo[nguyenlieu]:
            bo[nguyenlieu] = bo[nguyenlieu] + 1
            break
      bo[nguyenlieu] = 1
      break
  return bo
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
      b = p1.player_01.getUpsideDown(thesenhat,b,True,"II","")
    else:
      IIlonnhat = 0
      for a in b.dict_Card_Stocks_Show["II"]:
        if a.score > IIlonnhat:
          IIlonnhat = a.score
          thesenhat = a
      b = p1.player_01.getUpsideDown(thesenhat,b,True,"II","")
  # nếu có thẻ
  else:
    if p1.player_01.checkGetCard(p1.player_01.card_upside_down[0]) == True:
      print("lấy thẻ")
      p1.player_01.getCard(p1.player_01.card_upside_down[0],b,True,"")
    else:
    #lấy nguyên liệu
      # tìm nguyên liệu cần nhất trong các nguyên liệu cần
      if p1.player_01.checkOneStock(b,nguyenlieucannhat()) == True:
        print("lấy 2 nguyên liệu", nguyenlieucannhat())
        p1.player_01.getOneStock(nguyenlieucannhat(),b,{})
      else:
        #lấy 3 nguyên liệu
        bo = {}
        if sum(p1.player_01.stocks.values()) == 8:
          bo = nguyenlieubo1()
        if sum(p1.player_01.stocks.values()) == 9:
          bo = nguyenlieubo2()
        if sum(p1.player_01.stocks.values()) == 10:
          bo = nguyenlieubo3()

        print("bỏ",bo)
        print("lấy 3 nguyên liệu", nguyenlieucannhat(),nguyenlieucannhi(),nguyenlieuthuba())
        p1.player_01.getThreeStocks(nguyenlieucannhat(),nguyenlieucannhi(),nguyenlieuthuba(),b,bo)


for luot in range(7):
  moiturn()
  print(p1.player_01.stocks)
# print (b.stocks)
b.hien_the()
print(p1.player_01.card_upside_down[0].stocks)

# b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])
# b.hien_the()
# print(b.stocks)
# print(p1.player_01.stocks)
# print(p1.player_01.card_upside_down[0])

# while Victory([p1.player_01, p2.player_02, p3.player_03, p4.player_04]) == None:
#     b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])
#     b = p2.action(b, [p1.player_01, p3.player_03, p4.player_04])
#     b = p3.action(b, [p1.player_01, p2.player_02, p4.player_04])
#     b = p4.action(b, [p1.player_01, p2.player_02, p3.player_03])
#     turn += 1
#     result_turn.append({ "Turn": turn,
#     "Data" : save_excel(b ,[p1.player_01, p2.player_02, p3.player_03, p4.player_04])})

# data = pd.json_normalize(result_turn,max_level=1)
# data.to_csv("test.csv", index=False)