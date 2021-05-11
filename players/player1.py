from base import player
import random

player_01 = player.Player("1", 0)


def action(board, arr_player):
    return moiturn(board)

def moiturn(board):
    thecothelay = []
    if len(player_01.card_upside_down) > 0:
        for the in player_01.card_upside_down:
            if player_01.checkGetCard(the) == True:
                thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["III"]:
        if player_01.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["II"]:
        if player_01.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["I"]:
        if player_01.checkGetCard(the) == True:
            thecothelay.append(the)
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_01.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    if len(thecothelay) > 0:
        return player_01.getCard(thecothelay[0],board)
    if sum(player_01.stocks.values()) > 7:
        if sum(player_01.stocks.values()) == 10:
            bo = {}
            for nguyenlieu in player_01.stocks.keys():
                if player_01.stocks[nguyenlieu] >0:
                    bo[nguyenlieu] = 1
                    break
            return player_01.getUpsideDown(board.dict_Card_Stocks_Show["I"][0],board,bo)
        return player_01.getUpsideDown(board.dict_Card_Stocks_Show["I"][0],board,{})
    if len(nguyenlieucothelay2) >0:
        return player_01.getOneStock(nguyenlieucothelay2[0],board,{})
    if len(nguyenlieucon) > 2:
        banguyenlieu = random.sample(range(len(nguyenlieucon)),3)
        return player_01.getThreeStocks(nguyenlieucon[banguyenlieu[0]],nguyenlieucon[banguyenlieu[1]],nguyenlieucon[banguyenlieu[2]],board,{})
    return board