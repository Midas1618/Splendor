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
# b.setupCard()
turn = 1
result_turn = []
b.hien_the()
print(p1.player_01.stocks)

b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])
print("done")
b = p1.action(b, [p2.player_02, p3.player_03, p4.player_04])

print(p1.player_01.stocks, p1.player_01.stocks_const, p1.player_01.score)
print(b.stocks)


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







