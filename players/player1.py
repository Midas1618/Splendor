from base import player
import random
import operator

player_01 = player.Player("NA", 0)

def action(board, arr_player):
    return moiturn(board, arr_player)
    
# list những thẻ có thể lấy ngay
def listthecothemua(board):
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
    return thecothelay

    diemmax = 0
    thenenmua = None
    for the in listthecothemua(board):
        if the.type_stock == nlcannhat(thetarget(board)):
            diem = 20-(sum(the.stocks.values()))
        else:
            diem = 10- (sum(the.stocks.values()))
        if diem > diemmax:
            diemmax = diem
            thenenmua = the
    return thenenmua

# list những nguyên liệu có thể lấy 2
def listnguyenlieulay2(board):
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_01.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    return nguyenlieucothelay2

# danh sách những nguyên liệu còn trên bàn
def listnguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon

#hàm định giá điểm
def tinhdiem(the,player_01):
    sonlthieunhat = 0
    for nguyenlieu in the.stocks.keys():
        if the.stocks[nguyenlieu] - player_01.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu] > sonlthieunhat:
            sonlthieunhat = the.stocks[nguyenlieu] -  player_01.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu]
    diem = the.score/sonlthieunhat
    return diem

def danhsachthe(board):
    danhsachthe = []
    danhsachthe.extend(player_01.card_upside_down)
    danhsachthe.extend(board.dict_Card_Stocks_Show["III"])
    danhsachthe.extend(board.dict_Card_Stocks_Show["II"])
    danhsachthe.extend(board.dict_Card_Stocks_Show["I"])
    return danhsachthe

# tìm loại và số lượng nguyên liệu thiếu
def dictnguyenlieuthieu(the):
    nguyenlieuthieu = {}
    for nguyenlieu in the.stocks.keys():
        if the.stocks[nguyenlieu] > (player_01.stocks[nguyenlieu] + player_01.stocks_const[nguyenlieu]):
            nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_01.stocks[nguyenlieu] + player_01.stocks_const[nguyenlieu])
    return nguyenlieuthieu    

# tìm nguyên liệu cần nhất trong thẻ
def nlcannhat(the):
    sonlcan = 0
    nlcannhat = None
    for nguyenlieu in dictnguyenlieuthieu(the).keys():
        if dictnguyenlieuthieu(the)[nguyenlieu] == max(list(dictnguyenlieuthieu(the).values())):
            sonlcan = dictnguyenlieuthieu(the)[nguyenlieu]
            nlcannhat = nguyenlieu
    return nguyenlieu

# tìm nguyên liệu cần nhất của mỗi player
def nlcannhat(board,player):
    dictnlvadiem = {}
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        dictnlvadiem[nguyenlieu] = player.stocks[nguyenlieu]
    for the in player.card_upside_down:
        for nguyenlieu in dictnlvadiem.keys():
            dictnlvadiem[nguyenlieu] = dictnlvadiem[nguyenlieu] + the.stocks[nguyenlieu]
    slmax = 0
    nlcannhat = None
    for nguyenlieu in dictnlvadiem.keys():
        if dictnlvadiem[nguyenlieu] > slmax:
            slmax = dictnlvadiem[nguyenlieu]
            nlcannhat = nguyenlieu
    return nguyenlieu

# tìm các nguyên liệu để nhặt
def nhat3cainay(board, arr_player):
    dictnlvadiem = {
        "red": 0,
        "blue": 0,
        "green": 0,
        "white": 0,
        "black": 0
    }
    target = [nlcannhat(board,player) for player in arr_player]
    if sum(player_01.stocks.values()) < 8:
        for nguyenlieu in listnguyenlieucon(board):
            if nguyenlieu in target and player_01.stocks[nguyenlieu] < 2:
                dictnlvadiem[nguyenlieu] = 1000
            else:
                for the in board.dict_Card_Stocks_Show["I"]:
                    dictnlvadiem[nguyenlieu] = dictnlvadiem[nguyenlieu] + the.stocks[nguyenlieu]
    a = {k: v for k, v in sorted(dictnlvadiem.items(), key=lambda item: item[1],reverse=True)}
    b = list(a.keys())
    c = [b[0],b[1],b[2]]
    return c

# tìm thẻ quý tộc dễ lấy nhất
def Nobletarget(board):
    diemmin = 1000
    target = None
    for Noble in board.dict_Card_Stocks_Show["Noble"]:
        diem = 0
        for nguyenlieu in Noble.stocks.keys():
            diem = diem + Noble.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu]
        if diem < diemmin:
            diemmin = diem
            target = Noble
    return target

# tìm danh sách type_stock cần
def listtypestock(board):
    danhsach = []
    for stype in Nobletarget(board).stocks.keys():
        if Nobletarget(board).stocks[stype] > player_01.stocks_const[stype]:
            danhsach.append(stype)
    return danhsach

# chấm điểm các thẻ
def chamdiemthe(board,the):
    if the.type_stock in listtypestock(board):
        dokholay = 1
    else:
        dokholay = 10 
    for nguyenlieu in the.stocks.keys():
        dokholay = dokholay + max((the.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu] - player_01.stocks[nguyenlieu]),0)
    diem = the.score/max(dokholay,3)
    return diem

# thẻ target
def thetarget(board):
    diemmax = 0
    themax = None
    for the in danhsachthe(board):
        if chamdiemthe(board,the) > diemmax:
            diemmax = chamdiemthe(board,the)
            themax = the
    return the

# thẻ sẽ úp
def theseup(board,arr_player):
    diemmax = 0
    themax = None
    for the in danhsachthe(board):
        if chamdiemthe(board,the) > diemmax and the not in player_01.card_upside_down:
            diemmax = chamdiemthe(board,the)
            themax = the
    return the

# chấm điểm nguyên liệu
def listnguyenlieuuutien(board, arr_player):
    dictnl = {}
    nhamvao = [nlcannhat(board,player) for player in arr_player]
    for nguyenlieu in listnguyenlieucon(board):
        if nguyenlieu in nhamvao and player_01.stocks[nguyenlieu] <2:
            diem = 1000
        else:
            diem = thetarget(board).stocks[nguyenlieu] - player_01.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu]
        dictnl[nguyenlieu] = diem
    a = {k: v for k, v in sorted(dictnl.items(), key=lambda item: item[1],reverse=True)}
    b = list(a.keys())
    return b

# thẻ điểm cao nhất trong các thẻ có thể mua
def thesemua(board,arr_player):
    diemmax = -10000000
    thesemua = None
    for the in listthecothemua(board):
        if chamdiemthe(board,the) > diemmax:
            diemmax = chamdiemthe(board,the)
            thesemua = the
    return thesemua

def moiturn(board,arr_player):
    if sum(player_01.stocks.values()) <8:
        if len(listnguyenlieucon(board)) >2:
            return player_01.getThreeStocks(listnguyenlieuuutien(board,arr_player)[0],listnguyenlieuuutien(board,arr_player)[1],listnguyenlieuuutien(board,arr_player)[2],board,{})
        else:
            if player_01.checkUpsiteDown() == True:
                return player_01.getUpsideDown(theseup(board,arr_player),board,{})
            else:
                return board
    else:
        if len(listthecothemua(board)) > 0:
            ####print(1)
            return player_01.getCard(thesemua(board,arr_player),board)
        else:
            if player_01.checkUpsiteDown() == True:
                return player_01.getUpsideDown(theseup(board,arr_player),board,{})
            else:
                return board
            