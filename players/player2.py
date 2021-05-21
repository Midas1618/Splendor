from base import player
import random
import operator
player_02 = player.Player("Trang", 0)

def action(board, arr_player):
    return moiturn(board)

def moiturn(board):
    thelay = card_target(board)
    maudep = color_target(board)
    thegiu = card_holding(player_02)
    NLlay = NLcan(board)
    NLfail= NLkocan(board)
    NLcon = laynguyenlieucon(board)
    NLlay2 = nguyenlieucothelay2(board)
    if latthe(board,player_02) != None:
        return player_02.getCard(latthe(board, player_02),board)
    if thelay!= None:
        for the in thegiu:
            if the.score != thelay.score and player_02.checkUpsiteDown() == True:
                return player_02.getUpsideDown(thelay,board, boNL_Upsidedown(board,player_02,"auto_color"))  
    if len(player_02.card_upside_down) != 0:
        for the in player_02.card_upside_down:
            if the.score == 3 and player_02.checkOneStock(board,the.type_stock) == True:
                return player_02.getOneStock(the.type_stock,board,boNL_get1stock(board,player_02,the.type_stock,the.type_stock))
            if the.score == 5:
                for s in the.stocks.keys():
                    if the.stocks[s] == 7 and player_02.checkOneStock(board,s) == True :
                        return player_02.getOneStock(s,board,boNL_get1stock(board,player_02,s,s))
            if the.score == 4:
                for s in the.stocks.keys():
                    if the.stocks[s] == 7 and player_02.checkOneStock(board,s) == True:
                        return player_02.getOneStock(s,board,boNL_get1stock(board,player_02,s,s))
            if the.score == 2: 
                for s in the.stocks.keys():
                    if the.stocks[s] == 5 and player_02.checkOneStock(board,s) == True:
                        return player_02.getOneStock(s,board,boNL_get1stock(board,player_02,s,s))
            if the.score == 1: 
                for s in the.stocks.keys():
                    if the.stocks[s] == 4 and player_02.checkOneStock(board,s) == True:
                        return player_02.getOneStock(s,board,boNL_get1stock(board,player_02,s,s))
            if len(NLlay) > 2 and player_02.checkThreeStocks(board,NLlay[0],NLlay[1],NLlay[2])==True:
                return player_02.getThreeStocks(NLlay[0],NLlay[1],NLlay[2],board,boNL_get3stocks(board,player_02,NLlay[0],NLlay[1],NLlay[2]))
            if len(NLlay) == 2 and len(NLcon) > 0:
                for thefail in NLfail:
                    if thefail not in NLlay and thefail in NLcon and player_02.checkThreeStocks(board,NLlay[0],NLlay[1],thefail)==True:
                        return player_02.getThreeStocks(NLlay[0],NLlay[1],thefail,board,boNL_get3stocks(NLlay[0],NLlay[1],thefail,board,player_02))
                for the in NLcon:
                    if the not in NLlay and player_02.checkThreeStocks(board,NLlay[0],NLlay[1],the):
                        return player_02.getThreeStocks(NLlay[0],NLlay[1],the,board,boNL_get3stocks(board,player_02,NLlay[0],NLlay[1],the))
            if len(NLlay) == 1 and len(NLcon) > 1:
                for the in NLcon:
                    the0trung = []
                    if the != NLlay[0]:
                        the0trung.append(the)
                if len(the0trung)>1 and player_02.checkThreeStocks(board, NLlay[0],the0trung[0],the0trung[1]):
                    return player_02.getThreeStocks(NLlay[0],the0trung[0],the0trung[1],board,boNL_get3stocks(board,player_02,NLlay[0],the0trung[0],the0trung[1]))
    if theup(board)!= None:
        return player_02.getUpsideDown(theup(board),board,boNL_Upsidedown(board,player_02,"auto_color"))
    if len(player_02.card_upside_down) == 0:
        if len(NLlay2) >0:
            return player_02.getOneStock(NLlay2[0],board,boNL_get1stock(board,player_02,NLlay2[0],NLlay2[0]))
        else:
            return player_02.getThreeStocks(NLcon[0],NLcon[1],NLcon[2],board,boNL_get3stocks(board,player_02,NLcon[0],NLcon[1],NLcon[2]))
    else:
        return board

def theup(board):
    NL = []
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        max = 0
        for the in player_02.card_upside_down:
            if the.stocks[nguyenlieu] > max:
                the.stocks[nguyenlieu] = max
        if max > player_02.stocks[nguyenlieu]:
            NL.append(nguyenlieu)
    for n in NL:
        for the1 in board.dict_Card_Stocks_Show["III"]:
            if the1.type_stock == n:
                return the1
                    
def latthe(board,player_02):
    if len(player_02.card_upside_down) > 0:
        for the in player_02.card_upside_down:
            if player_02.checkGetCard(the):
                return the
    for thelat in List_card(board):
        if player_02.checkGetCard(thelat) == True:
            return thelat

def NLcan(board):
    List_NLcan = []
    dict_NLcan = {}
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        sum_NL = 0
        for the in player_02.card_upside_down:
            sum_NL += the.stocks[nguyenlieu]
        if sum_NL > player_02.stocks[nguyenlieu]:
            dict_NLcan[nguyenlieu] = sum_NL
    {k: v for k, v in sorted(dict_NLcan.items(), key=lambda item: item[1],reverse=True)}
    return list(dict_NLcan.keys())
                      
def NLkocan(board):
    List_NL0can = []
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        max = 0
        for the in player_02.card_upside_down:
            if the.stocks[nguyenlieu] > max:
                the.stocks[nguyenlieu] = max
        if max < player_02.stocks[nguyenlieu]:
            List_NL0can.append(nguyenlieu)
            
    return List_NL0can
def card_target(board):
    for card in List_card(board):
        if card.score == 3 and sum(card.stocks.values()) == 6:
            return card
        if card.score == 5 and sum(card.stocks.values()) == 10:
            for color in card.stocks.keys():
                if card.stocks[color] == 3:
                    return card
        if card.score == 4 and sum(card.stocks.values()) == 7:
            for color in card.stocks.keys():
                if card.stocks[color] == 7:
                    return card
        if card.score == 2:
            for color in card.stocks.keys():
                if card.stocks[color] == 5:
                    return card
        if card.score == 1:
            for color in card.stocks.keys():
                if card.stocks[color] == 4 :
                    return card
def card_holding(board):
    DS = []
    if len(player_02.card_open)>0:
        DS.extend(player_02.card_open)
        if len(player_02.card_upside_down):
            DS.extend(player_02.card_upside_down)
    return DS
        
    
def List_card(board):
    List = []
    List.extend(board.dict_Card_Stocks_Show["III"])
    List.extend(board.dict_Card_Stocks_Show["II"])
    List.extend(board.dict_Card_Stocks_Show["I"])
    return List
def TheII_III (board):   
    List_II_III = []
    List_II_III.extend(board.dict_Card_Stocks_Show["III"])
    List_II_III.extend(board.dict_Card_Stocks_Show["II"])
    return List_II_III
def color_target(board):
    NLMax = None
    max = 0
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        T = 0
        for the in TheII_III (board):
            T += the.stocks[nguyenlieu]
            NLMax = nguyenlieu
    return nguyenlieu

def laynguyenlieucon(board):
    nguyenlieucon = []
    dict_NLcon = {}
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and board.stocks[nguyenlieu] > 0:
            dict_NLcon[nguyenlieu] = board.stocks[nguyenlieu]
    {k: v for k, v in sorted(dict_NLcon.items(), key=lambda item: item[1])}
    return list(dict_NLcon.keys())
  

def nguyenlieucothelay2 (board):
    arr_NLlay2 = []
    if len(board.stocks.keys()) > 0:
        for nguyenlieu in board.stocks.keys():
            if nguyenlieu != "auto_color" and player_02.checkOneStock(board,nguyenlieu) == True:
                arr_NLlay2.append(nguyenlieu)
        return arr_NLlay2
    else:
        return board
def stocks_holding(board,player_02):
    dict_NLgiu = {}
    if len(player_02.stocks.keys()) > 0:
        for s in player_02.stocks.keys():
            dict_NLgiu[s] = player_02.stocks[s]
        {k: v for k, v in sorted(dict_NLgiu.items(), key=lambda item: item[1])}
    return list(dict_NLgiu.keys())       
            

def boNL_get3stocks(board,player_02,*args):
    dict_bo = {
        "red":0,
        "blue":0,
        "white":0,
        "green":0,
        "black":0,
        "auto_color": 0
    }
    dict_bd = player_02.stocks
    for x in args:
        dict_bd[x] += 1
    danhsachcon = laynguyenlieucon(player_02)
    a = stocks_holding(board,player_02)
    boNL = {}
    if len(player_02.stocks.keys()) == 10:
        boNL[a[0]] = 1
        boNL[a[1]] = 1
        boNL[a[2]] = 1

    if len(player_02.stocks.keys()) == 9:
        boNL[a[0]] = 1
        boNL[a[1]] = 1
        
    if len(player_02.stocks.keys()) == 8:
        boNL[a[0]]= 1
    return boNL

def boNL_get1stock(board,player_02,*args):
    dict_bo = {
        "red":0,
        "blue":0,
        "white":0,
        "green":0,
        "black":0,
        "auto_color": 0
    }
    dict_bd = player_02.stocks
    for x in args:
        dict_bd[x] += 1
    danhsachcon = laynguyenlieucon(player_02)
    a = stocks_holding(board,player_02)
    boNL = {}
    if len(player_02.stocks.keys()) == 10:
        boNL[a[0]] = 1
        boNL[a[1]] = 1
    if len(player_02.stocks.keys()) == 9:
        boNL[a[0]]= 1
    return boNL

def boNL_Upsidedown(board,player_02,*args):
    dict_bo = {
        "red":0,
        "blue":0,
        "white":0,
        "green":0,
        "black":0,
        "auto_color": 0
    }
    dict_bd = player_02.stocks
    for x in args:
        dict_bd[x] += 1
    danhsachcon = laynguyenlieucon(player_02)
    a = stocks_holding(board,player_02)
    boNL = {}
    if len(player_02.stocks.keys()) == 10:
        boNL[a[0]] = 1
    return boNL