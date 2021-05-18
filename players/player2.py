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
        #####print(18)
        return player_02.getCard(latthe(board, player_02),board)
    if thelay!= None and thegiu != None:
        #####print(21)
        for the in thegiu:
            if the.score != thelay.score and player_02.checkUpsiteDown() == True:
                #####print(24)
                return player_02.getUpsideDown(thelay,board, Luachonbothe(board,"auto_color"))  
    
    if len(player_02.card_upside_down) > 0:
        #####print(28)
        for the in player_02.card_upside_down:
            if the.score == 3 and player_02.checkOneStock(board,the.type_stock) == True:
                #####print(31)
                return player_02.getOneStock(the.type_stock,board,Luachonbothe(board,the.type_stock,the.type_stock))
            if the.score == 5:
                #####print(34)
                for s in the.stocks.keys():
                    if the.stocks[s] == 7 and player_02.checkOneStock(board,s) == True :
                        #####print(37)
                        return player_02.getOneStock(s,board,Luachonbothe(board,s,s))
            if the.score == 4:
                #####print(40)
                for s in the.stocks.keys():
                    if the.stocks[s] == 7 and player_02.checkOneStock(board,s) == True:
                        #####print(43)
                        return player_02.getOneStock(s,board,Luachonbothe(board,s,s))
            if the.score == 2: 
                #####print(46)
                for s in the.stocks.keys():
                    if the.stocks[s] == 5 and player_02.checkOneStock(board,s) == True:
                        #####print(49)
                        return player_02.getOneStock(s,board,Luachonbothe(board,s,s))
            if the.score == 1: 
                #####print(52)
                for s in the.stocks.keys():
                    if the.stocks[s] == 4 and player_02.checkOneStock(board,s) == True:
                        #####print(55)
                        return player_02.getOneStock(s,board,Luachonbothe(board,s,s))
            if NLlay != None and NLfail != None:
                #####print(58)
                if len(NLlay) > 2 and player_02.checkThreeStocks(board,NLlay[0],NLlay[1],NLlay[2])==True:
                    #####print(60)
                    return player_02.getThreeStocks(NLlay[0],NLlay[1],NLlay[2],board,Luachonbothe(board,NLlay[0],NLlay[1],NLlay[2]))
                if len(NLlay) == 2 and len(NLcon)>0:
                    #####print(63)
                    for thefail in NLfail:
                        if thefail not in NLlay and thefail in NLcon and player_02.checkThreeStocks(board,NLlay[0],NLlay[1],thefail)==True:
                            #####print(66)
                            return player_02.getThreeStocks(NLlay[0],NLlay[1],thefail,board,Luachonbothe(board,NLlay[0],NLlay[1],thefail))
                    for the in NLcon:
                        if the not in NLlay and player_02.checkThreeStocks(board,NLlay[0],NLlay[1],the):
                            #####print(70)
                            return player_02.getThreeStocks(NLlay[0],NLlay[1],the,board,Luachonbothe(board,NLlay[0],NLlay[1],the))
                if len(NLlay) == 1 and len(NLcon) > 1:
                    #####print(73)
                    for the in NLcon:
                        the0trung = []
                        if the != NLlay[0]:
                            #####print(77)
                            the0trung.append(the)
                    if len(the0trung)>1 and player_02.checkThreeStocks(board, NLlay[0],the0trung[0],the0trung[1]):
                        #####print(80)
                        return player_02.getThreeStocks(NLlay[0],the0trung[0],the0trung[1],board,Luachonbothe(board,NLlay[0],the0trung[0],the0trung[1]))
    if theup(board)!= None and player_02.checkUpsiteDown()==True:
        #####print(83)
        return player_02.getUpsideDown(theup(board),board,Luachonbothe(board,"auto_color"))
    if len(player_02.card_upside_down) == 0 and NLlay2 != None and NLcon != None:
        if len(NLlay2) >1 and player_02.checkOneStock(board,NLlay2[0]):
            return player_02.getOneStock(NLlay2[0],board,Luachonbothe(board,NLlay2[0],NLlay2[0]))
        if len(NLcon) > 2 and player_02.checkThreeStocks(board,NLcon[0],NLcon[1],NLcon[2]):
            return player_02.getThreeStocks(NLcon[0],NLcon[1],NLcon[2],board,Luachonbothe(board,NLcon[0],NLcon[1],NLcon[2]))
    return board
def theup(board):   
    if len(board.dict_Card_Stocks_Show["I"]) > 0:
        #####print(102)
        if NLcan(board)!= None and len(NLcan(board)) > 0:
            #####print(104)
            for NL in NLcan(board):
                for the1 in board.dict_Card_Stocks_Show["I"]:
                    if the1.type_stock == NL:
                        #####print(108)
                        return the1
                    
def latthe(board,player_02):
    if len(player_02.card_upside_down) > 0:
        #####print(113)
        for the in player_02.card_upside_down:
            if player_02.checkGetCard(the) == True:
                #####print(116)
                return the
    else: 
        for thelat in List_card(board):
            if player_02.checkGetCard(thelat) == True:
                #####print(121)
                return thelat

def NLcan(board):
    List_NLcan = []
    dict_NLcan = {}
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        if len(player_02.card_upside_down) > 0:
            #####print(129)
            sum_NL = 0
            for the in player_02.card_upside_down:
                sum_NL += the.stocks[nguyenlieu]
            if sum_NL > player_02.stocks[nguyenlieu]:
                #####print(134)
                dict_NLcan[nguyenlieu] = sum_NL
    {k: v for k, v in sorted(dict_NLcan.items(), key=lambda item: item[1],reverse=True)}
    return list(dict_NLcan.keys())
                
def NLkocan(board):
    List_NL0can = []
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        if len(player_02.card_upside_down) > 0:
            #####print(143)
            sum_NL = 0
            for the in player_02.card_upside_down:
                sum_NL += the.stocks[nguyenlieu]
            if sum_NL <= player_02.stocks[nguyenlieu]:
                #####print(148)
                List_NL0can.append(nguyenlieu) 
            return List_NL0can    
              
    
def card_target(board):
    for card in List_card(board):
        if card.score == 3 and sum(card.stocks.values()) == 6:
            #####print(156)
            return card
        if card.score == 5 and sum(card.stocks.values()) == 10:
            #####print(159)
            for color in card.stocks.keys():
                if card.stocks[color] == 3:
                    #####print(162)
                    return card
        if card.score == 4 and sum(card.stocks.values()) == 7:
            #####print(165)
            for color in card.stocks.keys():
                if card.stocks[color] == 7:
                    #####print(168)
                    return card
        if card.score == 2:
            #####print(171)
            for color in card.stocks.keys():
                if card.stocks[color] == 5:
                    #####print(174)
                    return card
        if card.score == 1:
            #####print(177)
            for color in card.stocks.keys():
                if card.stocks[color] == 4 :
                    #####print(180)
                    return card
def card_holding(board):
    DS = []
    if len(player_02.card_open)>0:
        #####print(185)
        DS.extend(player_02.card_open)
        if len(player_02.card_upside_down)>0:
            #####print(188)
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
        if T > 0:
            T = max
            NLMax = nguyenlieu
    return nguyenlieu

def laynguyenlieucon(board):
    nguyenlieucon = []
    dict_NLcon = {}
    if len(board.stocks.keys()) > 0:
        #####print(219)
        for nguyenlieu in board.stocks.keys():
            if nguyenlieu != "auto_color" and board.stocks[nguyenlieu] > 0:
                #####print(222)
                dict_NLcon[nguyenlieu] = board.stocks[nguyenlieu]
        {k: v for k, v in sorted(dict_NLcon.items(), key=lambda item: item[1])}
        return list(dict_NLcon.keys())
  

def nguyenlieucothelay2 (board):
    arr_NLlay2 = []
    if len(board.stocks.keys()) > 0:
        #####print(231)
        for nguyenlieu in board.stocks.keys():
            if nguyenlieu != "auto_color" and player_02.checkOneStock(board,nguyenlieu) == True:
                #####print(234)
                arr_NLlay2.append(nguyenlieu)
        return arr_NLlay2
def stocks_holding(board,player_02):
    dict_NLgiu = {}
    if len(player_02.stocks.keys()) > 0:
        #####print(240)
        for s in player_02.stocks.keys():
            dict_NLgiu[s] = player_02.stocks[s]
        {k: v for k, v in sorted(dict_NLgiu.items(), key=lambda item: item[1])}
        return list(dict_NLgiu.keys())       
            

def Luachonbothe(board,*args):
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
    if stocks_holding(board,player_02) != None:
        danhsachcon = stocks_holding(board,player_02)
        if sum(dict_bd.values()) > 10:
            #####print(261)
            n = sum(dict_bd.values()) - 10
            i = 0
            while n != 0:
                ####print(266)
                if dict_bd[danhsachcon[i]] != 0:
                    ####print(268)
                    dict_bo[danhsachcon[i]] +=1
                    dict_bd[danhsachcon[i]] -=1
                    n -= 1
                else:
                    i += 1
        return dict_bo
