from numpy.core.fromnumeric import take
from base.player import Player
from base import board
from players import p1 as p1
from players import p2 as p2
from players import p3 as p3
from players import p4 as p4
import pandas as pd
import random
import json
import time

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

def save_excel(b ,arr,turn):
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
  result["Turn"] = turn
  return result


def checkNone(b,player,turn):
  # saveAction("Lượt: " + str(turn) +" "+player.message)
  if b == None:
    print("Lỗi của :",player.name)

def RunGame(Luot):
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
    p = Victory([p1.player_01, p2.player_02, p3.player_03, p4.player_04])
    while p.name == "0":
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
          else:
            b = p4.action(b, [p1.player_01, p2.player_02, p3.player_03])
            checkNone(b,p4.player_04,turn)
        p = Victory([p1.player_01, p2.player_02, p3.player_03, p4.player_04])
    return p.name

for van in range(100):
  try:
    t = time.time()
    pVictory = Player("0", 0)
    p1.player_01 = p1.player.Player("1", 0)
    p2.player_02 = p2.player.Player("2", 0)
    p3.player_03 = p3.player.Player("3", 0)
    p4.player_04 = p4.player.Player("4", 0)
    p = RunGame(1234)
    f = open("p"+p + "learning.json")
    learning  = json.load(f)
    score = 0
    for luot in learning:
        score += 1
        for code in luot.keys():
            data = pd.read_csv('Knwldg/'+ code[:2] + "/" + code[2:8] + "/"+ code[8:13] + "/"+ code[13:19] + "/"+ code[19:] +".csv")
            data[luot[code]] += score
            data.to_csv('Knwldg/'+ code[:2] + "/" + code[2:8] + "/"+ code[8:13] + "/"+ code[13:19] + "/"+ code[19:] +".csv",index = False)
    with open("p4learning.json","w") as outfile:
        json.dump([],outfile)
    with open("p3learning.json","w") as outfile:
        json.dump([],outfile)
    with open("p2learning.json","w") as outfile:
        json.dump([],outfile)
    with open("p1learning.json","w") as outfile:
        json.dump([],outfile)
    print(p,"thắng trong",time.time()-t,"giây")
  except:
    with open("p4learning.json","w") as outfile:
        json.dump([],outfile)
    with open("p3learning.json","w") as outfile:
        json.dump([],outfile)
    with open("p2learning.json","w") as outfile:
        json.dump([],outfile)
    with open("p1learning.json","w") as outfile:
        json.dump([],outfile)
    print("skip lỗi")





