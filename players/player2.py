from base import player
import random
player_02 = player.Player("Trang", 0)

def action(board, arr_player):
    return moiturn(board)

def moiturn(board):

# Úp thẻ:
    if ChooseCard(board,3,6) != None and len(player_02.card_upside_down) < 2:
        for card_3 in ChooseCard(board,3,6):
            for t in player_02.stocks.keys():
                if card_3.type_stock == t:
                    return player_02.getUpsideDown(card_3,board,Luachonbothe("auto_color"))
    elif ChooseCard(board,5,10) != None and len(player_02.card_upside_down) <2:  
        for card_5 in ChooseCard(board,5,10):
                for s in card_5.stocks.keys():
                    for t in player_02.stocks.keys():
                        if card_5.stocks[s] == 3 and s == t:
                            return player_02.getUpsideDown(card_5, board, Luachonbothe("auto_color"))
    elif ChooseCard(board,4,7) != None and len(player_02.card_upside_down) <2:  
        for thedalay in player_02.card_upside_down:
            for card_4 in ChooseCard(board,4,7):
                for s in card_4.stocks.keys():
                    if thedalay.score == 5 and thedalay.stocks[s] == 7:
                        return player_02.getUpsideDown(card_4,board, Luachonbothe("auto_color"))
    elif ChooseCard_stock(board,4) != None and len(player_02.card_upside_down) < 2:
        for card_4stocks in ChooseCard_stock(board,4):
            if card_4stocks == 1:
                return player_02.getUpsideDown(card_4stocks, board,Luachonbothe("auto_color"))
    elif ChooseCard_score(board,2) != None and len(player_02.card_upside_down) <2:
        for card_0 in ChooseCard_score(board,2):
            if sum(card_0.stocks.values()) <7:
                for s in player_02.stocks.keys():
                    for s1 in card_0.stocks.keys():
                        if s1 == s:
                            return player_02.getUpsideDown(card_0,board,Luachonbothe("auto_color"))  
#Lấy 2 thẻ:
    arr_NLcon = laynguyenlieucon(board)
    arr_2NL = nguyenlieucothelay2 (board)
    if ChooseCard(board,3,6) != None:
        for card_3 in ChooseCard(board,3,6):
            if len(arr_2NL) > 0:
                for stock2 in arr_2NL:
                    if stock2 == card_3.type_stock:
                        return player_02.getOneStock(stock2,board,Luachonbothe(stock2,stock2))
                
            elif len(arr_NLcon) > 3 and player_02.checkThreeStocks(board, arr_NLcon[0],arr_NLcon[1],arr_NLcon[2])==True:
                return player_02.getThreeStocks(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2],board, Luachonbothe(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2]))

    elif ChooseCard(board,2,5) != None:
        for card_2 in ChooseCard(board,2,5):
            if len(arr_2NL) > 0:
                for stock2 in arr_2NL:
                    for stock in card_2.stocks.keys():
                        if stock2 == stock:
                            return player_02.getOneStock(stock2,board,Luachonbothe(stock2,stock2))

            elif player_02.checkThreeStocks(board, arr_NLcon[0],arr_NLcon[1],arr_NLcon[2])==True:
                return player_02.getThreeStocks(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2],board, Luachonbothe(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2]))
    elif ChooseCard(board,5,10) != None:
        if len(arr_2NL) > 0:
            for card_5 in ChooseCard(board,5,10):
                for s in card_5.stocks.keys():
                    for stock2 in arr_2NL: 
                        if card_5.stocks[s] == 3 and s == stock2:
                            return player_02.getOneStock(stock2,board,Luachonbothe(stock2,stock2))
                
        elif player_02.checkThreeStocks(board, arr_NLcon[0],arr_NLcon[1],arr_NLcon[2])==True:
            return player_02.getThreeStocks(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2],board, Luachonbothe(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2]))
    elif ChooseCard(board,4,7) != None:
        if len(arr_2NL) > 0:
            for card_4 in ChooseCard(board,4,7):
                for s in card_4.stocks.keys():
                    for stock2 in arr_2NL: 
                        if card_4.stocks[s] == 7 and s == stock2:
                            return player_02.getOneStock(stock2,board,Luachonbothe(stock2,stock2))
                       
        elif player_02.checkThreeStocks(board, arr_NLcon[0],arr_NLcon[1],arr_NLcon[2])==True:
            return player_02.getThreeStocks(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2],board, Luachonbothe(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2]))
    elif player_02.checkThreeStocks(board, arr_NLcon[0],arr_NLcon[1],arr_NLcon[2])==True:   
        return player_02.getThreeStocks(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2],board, Luachonbothe(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2]))


#lấy 3 stocks:
    stock_card = []
    for theup in player_02.card_upside_down:
        for s in theup.stocks.keys():
            if s not in stock_card:
                stock_card.append(s)
    if len(stock_card) > 2 and player_02.checkThreeStocks(board, stock_card[0],stock_card[1],stock_card[2]) == True:
        return player_02.getThreeStocks(stock_card[0],stock_card[1],stock_card[2],board,Luachonbothe(stock_card[0],stock_card[1],stock_card[2]))
    elif len(arr_NLcon) > 3 and player_02.checkThreeStocks(board,arr_NLcon[0],arr_NLcon[1],arr_NLcon[2])==True:
        return player_02.getThreeStocks(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2],board,Luachonbothe(arr_NLcon[0],arr_NLcon[1],arr_NLcon[2]))

#lật thẻ:
    for thedangup in player_02.card_upside_down:
        if player_02.checkGetCard(thedangup)==True:
            return player_02.getCard(thedangup,board)
    for thebatki in board.dict_Card_Stocks_Show["III"]:
        if player_02.checkGetCard(thebatki)==True:
            return player_02.getCard(thebatki,board)
    for the in board.dict_Card_Stocks_Show["II"]:
        if player_02.checkGetCard(the)==True:
            return player_02.getCard(the,board)
    for theI in board.dict_Card_Stocks_Show["I"]:
        if sum(player_02.stocks.values()) == 10 and player_02.checkGetCard(theI)==True:
            return player_02.getCard(theI,board)                          
    return board

def laynguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon

def nguyenlieucothelay2 (board):
    arr_NLlay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_02.checkOneStock(board,nguyenlieu) == True:
            arr_NLlay2.append(nguyenlieu)
    return arr_NLlay2

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
    danhsachcon = laynguyenlieucon(player_02)
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