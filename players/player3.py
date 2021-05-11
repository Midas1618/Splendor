from base import player
import random
player_03 = player.Player("NA", 0)

def action(board, arr_player):
    return moiturn(board)

def moiturn(board):
    thecothelay = []
    if len(player_03.card_upside_down) > 0:
        for the in player_03.card_upside_down:
            if player_03.checkGetCard(the) == True:
                thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["III"]:
        if player_03.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["II"]:
        if player_03.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["I"]:
        if player_03.checkGetCard(the) == True:
            thecothelay.append(the)
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_03.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    if len(thecothelay) > 0:
        return player_03.getCard(thecothelay[0],board)
    if sum(player_03.stocks.values()) > 7:
        if sum(player_03.stocks.values()) == 10:
            bo = {}
            for nguyenlieu in player_03.stocks.keys():
                if player_03.stocks[nguyenlieu] >0:
                    bo[nguyenlieu] = 1
                    break
            return player_03.getUpsideDown(board.dict_Card_Stocks_Show["I"][0],board,bo)
        return player_03.getUpsideDown(board.dict_Card_Stocks_Show["I"][0],board,{})
    if len(nguyenlieucothelay2) >0:
        return player_03.getOneStock(nguyenlieucothelay2[0],board,{})
    if len(nguyenlieucon) > 2:
        banguyenlieu = random.sample(range(len(nguyenlieucon)),3)
        return player_03.getThreeStocks(nguyenlieucon[banguyenlieu[0]],nguyenlieucon[banguyenlieu[1]],nguyenlieucon[banguyenlieu[2]],board,{})
    return board