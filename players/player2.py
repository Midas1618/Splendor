from base import player
import random
player_02 = player.Player("Trang", 0)

def action(board, arr_player):
    return moiturn(board)

def moiturn(board):
    # thecothelay = []
    # if len(player_02.card_upside_down) > 0:
    #     for the in player_02.card_upside_down:
    #         if player_02.checkGetCard(the) == True:
    #             thecothelay.append(the)
    # for the in board.dict_Card_Stocks_Show["III"]:
    #     if player_02.checkGetCard(the) == True:
    #         thecothelay.append(the)
    # for the in board.dict_Card_Stocks_Show["II"]:
    #     if player_02.checkGetCard(the) == True:
    #         thecothelay.append(the)
    # for the in board.dict_Card_Stocks_Show["I"]:
    #     if player_02.checkGetCard(the) == True:
    #         thecothelay.append(the)
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_02.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    NLcon = checknguyenlieucon(board)
    the3score = ChooseCard(board,3,6)
    if ChooseCard(board,3,6) != None and len(nguyenlieucothelay2)  > 0:
        for thelay2 in nguyenlieucothelay2:
            for card3diem in the3score:
                if thelay2 == card3diem.type_stock and player_02.checkOneStock(board,thelay2) == True:
                    return player_02.getOneStock(thelay2,board,Luachonbothe(thelay2,thelay2))
                elif player_02.checkUpsiteDown() == True:
                    return player_02.getUpsideDown(the3score[0],board,Luachonbothe("auto_color"))
    if ChooseCard(board,3,6) == None and len(nguyenlieucothelay2)  > 0:
        for the in nguyenlieucothelay2:
            if the == "red":
                return player_02.getOneStock(the,board, Luachonbothe(the,the))
            elif the == "black":
                return player_02.getOneStock(the,board, Luachonbothe(the,the))
            elif len(NLcon) >3 and player_02.checkThreeStocks(board, NLcon[0],NLcon[1],NLcon[2])==True:
                return player_02.getThreeStocks(NLcon[0],NLcon[1],NLcon[2],board,Luachonbothe(NLcon[0],NLcon[1],NLcon[2]))
            elif player_02.checkUpsiteDown() :
                return player_02.getUpsideDown(board.dict_Card_Stocks_Show["I"][0],board, Luachonbothe("auto_color"))
    
    if ChooseCard(board,4,7) != None and len(nguyenlieucothelay2) > 0:
        for card4diem in ChooseCard(board,4,7):
            for mau in card4diem.stocks.keys():
                for thelay2 in nguyenlieucothelay2:
                    if thelay2 == mau and player_02.checkOneStock(board,thelay2)==True:
                        return player_02.getOneStock(thelay2,board,Luachonbothe(thelay2,thelay2))
                    elif len(NLcon) >3 and player_02.checkThreeStocks(board, NLcon[0],NLcon[1],NLcon[2])==True:
                        return player_02.getThreeStocks(NLcon[0],NLcon[1],NLcon[2],board,Luachonbothe(NLcon[0],NLcon[1],NLcon[2]))
    elif  len(NLcon) >3 and player_02.checkThreeStocks(board,NLcon[0],NLcon[1],NLcon[2]):
        return player_02.getThreeStocks(NLcon[0],NLcon[1],NLcon[2],board,Luachonbothe(NLcon[0],NLcon[1],NLcon[2]))

    # elif player_02.checkUpsiteDown():
    #     return player_02.getUpsideDown(thecothelay[0],board,Luachonbothe("auto_color")) 
    
    elif len(player_02.card_upside_down) != 0 :
        for thecothelat in player_02.card_upside_down:
            if player_02.checkGetCard(thecothelat) == True:
                return player_02.getCard(thecothelat,board)
    return board
        


def ChooseCard_score(board,score):
  arr_Card = []
  for i in board.dict_Card_Stocks_Show.keys():
    if i != "Noble":
      for j in board.dict_Card_Stocks_Show[i]:
        if j.score == score:
          arr_Card.append(j)
  return arr_Card 

def ChooseCard_stock(board,sum_stock):
  arr_Card = []
  for i in board.dict_Card_Stocks_Show.keys():
    if i != "Noble":
      for j in board.dict_Card_Stocks_Show[i]:
        if sum(j.stocks.values()) == sum_stock:
          arr_Card.append(j)
  return arr_Card 

def ChooseCard(board,score,sum_stock):
  Thedep = []
  Card_score = ChooseCard_score(board,score)
  Card_stocks = ChooseCard_stock(board,sum_stock)
  for i in Card_score:
    for j in Card_stocks:
      if i.id == j.id:
        Thedep.append(i)
  return Thedep

min = 8
def min_stocks(player_02):
  for m in player_02.stocks.keys():
    if player_02.stocks[m] < min:
      min = player_02.stocks[m]
  return m
def checknguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon

def Luachonbothe(*args):
    dict_bo = {
        "red":0,
        "blue":0,
        "white":0,
        "green":0,
        "black":0,
        "auto_color": 0
    }
    dict_bd = player_02.stocks.copy()
    for x in args:
        dict_bd[x] += 1
    danhsachcon = checknguyenlieucon(player_02)
    if sum(dict_bd.values()) > 10:
        n = sum(dict_bd.values()) - 10
        i = 0
        while n != 0:
            if dict_bd[danhsachcon[i]] != 0:
                dict_bo[danhsachcon[i]] +=1
                dict_bd[danhsachcon[i]] -=1
                n -= 1
            else:
                i += 1
    return dict_bo