from base import player
import random
import operator

player_05 = player.Player("NA", 0)

def action(board, arr_player):
    return moiturn(board)
# list những thẻ có thể lấy ngay
def listthecothemua(board):
    thecothelay = []
    if len(player_05.card_upside_down) > 0:
        for the in player_05.card_upside_down:
            if player_05.checkGetCard(the) == True:
                thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["III"]:
        if player_05.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["II"]:
        if player_05.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["I"]:
        if player_05.checkGetCard(the) == True:
            thecothelay.append(the)
    return thecothelay

# list những nguyên liệu có thể lấy 2
def listnguyenlieulay2(board):
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_05.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    return nguyenlieucothelay2

# danh sách những nguyên liệu còn trên bàn
def listnguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon

# trong những thẻ có thể mua ngay turn này, thẻ nào nhiều điểm nhất
def thelayngay(board):
    diemcothelay = -1
    thelayngay = None
    for the in listthecothemua(board):
        if the.score > 0 and the.score > diemcothelay:
            diemcothelay = the.score
            thelayngay = the
    return thelayngay

#hàm định giá điểm
def tinhdiem(the,player_05):
    sonlthieunhat = 0
    for nguyenlieu in the.stocks.keys():
        if the.stocks[nguyenlieu] - player_05.stocks[nguyenlieu] - player_05.stocks_const[nguyenlieu] > sonlthieunhat:
            sonlthieunhat = the.stocks[nguyenlieu] -  player_05.stocks[nguyenlieu] - player_05.stocks_const[nguyenlieu]
    diem = the.score/sonlthieunhat
    return diem

def danhsachthe(board):
    danhsachthe = []
    danhsachthe.extend(player_05.card_upside_down)
    danhsachthe.extend(board.dict_Card_Stocks_Show["III"])
    danhsachthe.extend(board.dict_Card_Stocks_Show["II"])
    danhsachthe.extend(board.dict_Card_Stocks_Show["I"])
    return danhsachthe

# định giá điểm từng thẻ
def dictthecodiem(board):
    thecodiem = {}
    nlcon = listnguyenlieucon(board)
    for the in danhsachthe(board):
        dictthieu = dictnguyenlieuthieu(the)
        if sum(the.stocks.values()) > 10:
            thecodiem[the] = 0
            continue
        if len(dictthieu) == 0:
            turn = 1
        else:
            turn = max(list(dictthieu.values())) + 1
        for nguyenlieu in dictthieu.keys():
            if nguyenlieu not in nlcon:
                turn = turn + 1
        diem = (the.score + 0.2)/turn
        thecodiem[the] = diem
    return thecodiem

#định giá thẻ trên bàn
def dictthetrenban(board):
    thecodiem = {}
    nlcon = listnguyenlieucon(board)
    for the in danhsachthe(board):
        if the not in player_05.card_upside_down:
            dictthieu = dictnguyenlieuthieu(the)
            if sum(the.stocks.values()) > 10:
                thecodiem[the] = 0
                continue
            if len(dictthieu) == 0:
                turn = 1
            else:
                turn = max(list(dictthieu.values())) + 1
            for nguyenlieu in dictthieu.keys():
                if nguyenlieu not in nlcon:
                    turn = turn + 1
            diem = (the.score + 0.2)/turn
            thecodiem[the] = diem
    return thecodiem

# chọn ra thẻ có điểm cao nhất
def thetarget(board):
    diemcaonhat = 0
    thetarget = None
    for the in dictthecodiem(board).keys():
        if dictthecodiem(board)[the] > diemcaonhat:
            diemcaonhat = dictthecodiem(board)[the]
            thetarget = the
    return thetarget

# chọn ra thẻ tốt nhất ngoài danh sách cho trước
def theduphong(board,listthedachon):
    diemcaonhat = 0
    theduphong = None
    for the in dictthecodiem(board).keys():
        if dictthecodiem(board)[the] > diemcaonhat and the not in listthedachon:
            diemcaonhat = dictthecodiem(board)[the]
            theduphong = the
    return theduphong

# tìm loại và số lượng nguyên liệu thiếu
def dictnguyenlieuthieu(the):
    nguyenlieuthieu = {}
    for nguyenlieu in the.stocks.keys():
        if the.stocks[nguyenlieu] > (player_05.stocks[nguyenlieu] + player_05.stocks_const[nguyenlieu]):
            nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_05.stocks[nguyenlieu] + player_05.stocks_const[nguyenlieu])
    return nguyenlieuthieu    

# chênh giữa nl cần nhiều nhất và nhiều nhì
def nenlay2nl(the):
    if len(dictnguyenlieuthieu(the)) == 1:
        return True
    chenhlech = 0
    for luongnlthieu in dictnguyenlieuthieu(the).values():
        if max(dictnguyenlieuthieu(the).values()) - luongnlthieu != 0 and (max(dictnguyenlieuthieu(the).values()) - luongnlthieu) > chenhlech:
            chenhlech = max(dictnguyenlieuthieu(the).values()) - luongnlthieu
    if chenhlech > 1:
        return True
    else:
        return False

# tìm nguyên liệu cần nhất trong thẻ
def nlcannhat(the):
    sonlcan = 0
    nlcannhat = None
    for nguyenlieu in dictnguyenlieuthieu(the).keys():
        if dictnguyenlieuthieu(the)[nguyenlieu] == max(list(dictnguyenlieuthieu(the).values())):
            sonlcan = dictnguyenlieuthieu(the)[nguyenlieu]
            nlcannhat = nguyenlieu
            return nguyenlieu

# chấm điểm nguyên liệu có thể lấy
def listnguyenlieuuutien(board):
    nguyenlieuvadiem = {}
    a = {}
    for nguyenlieu in listnguyenlieucon(board):
        if nguyenlieu in dictnguyenlieuthieu(thetarget(board)).keys():
            diem = dictnguyenlieuthieu(thetarget(board))[nguyenlieu]
        else:
            diem = board.stocks[nguyenlieu]/10
        nguyenlieuvadiem[nguyenlieu] = diem
    a = {k: v for k, v in sorted(nguyenlieuvadiem.items(), key=lambda item: item[1],reverse=True)}
    return list(a.keys())

# chấm điểm nguyên liệu trên tay (cao càng tệ)
def listnguyenlieutrentay(board):
    dictchuaxephang = {}
    a = {}
    for nguyenlieu in thetarget(board).stocks.keys():
        diem = player_05.stocks[nguyenlieu] - thetarget(board).stocks[nguyenlieu]
        dictchuaxephang[nguyenlieu] = diem
    a = {k: v for k, v in sorted(dictchuaxephang.items(), key=lambda item: item[1],reverse=True)}
    return list(a.keys())

# tìm thẻ để úp
def theseup(board):
    diemcaonhat = 0
    thetarget = None
    for the in dictthetrenban(board).keys():
        if dictthetrenban(board)[the] > diemcaonhat:
            diemcaonhat = dictthetrenban(board)[the]
            thetarget = the
    return thetarget

def moiturn(board):
    target = thetarget(board)
    print("thẻ target:",target.score,"điểm",target.stocks,target.type_stock)
    print("những nguyên liệu còn thiếu:",dictnguyenlieuthieu(target))
    if thelayngay(board) != None:
        print("hốt ngay thẻ",thelayngay(board).stocks)
        return player_05.getCard(thelayngay(board),board)
    else:
        if sum(player_05.stocks.values()) >8:
            if player_05.checkUpsiteDown() == True:
                if sum(player_05.stocks.values()) == 9:
                    bo = {}
                if sum(player_05.stocks.values()) == 10:
                    bo = {listnguyenlieutrentay(board)[0]:1}
                print(209)
                return player_05.getUpsideDown(theseup(board),board,bo)
            else:
                if len(listnguyenlieucon(board)) >2:
                    if sum(player_05.stocks.values()) == 9:
                        print(214)
                        return player_05.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{listnguyenlieuuutien(board)[2]:1,listnguyenlieuuutien(board)[1]:1})
                    if sum(player_05.stocks.values()) == 10:
                        print(217)
                        print("lấy 3 nguyên liệu:",listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],"và trả 3 nguyên liệu:",{listnguyenlieutrentay(board)[0]:1,listnguyenlieutrentay(board)[1]:1,listnguyenlieutrentay(board)[2]:1})
                        return player_05.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{listnguyenlieutrentay(board)[0]:1,listnguyenlieutrentay(board)[1]:1,listnguyenlieutrentay(board)[2]:1})
                else:
                    print("skip 220")
                    return board
        if sum(player_05.stocks.values()) == 8:
            if len(listnguyenlieucon(board)) >2:
                print(224)
                return player_05.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{listnguyenlieuuutien(board)[2]:1})
            else:
                if player_05.checkUpsiteDown() == True:
                    print(228)
                    return player_05.getUpsideDown(theseup(board),board,{})
                else:
                    print("skip chỗ 1")
                    return board
        else:
            # số thẻ trên tay < 8
            if player_05.checkOneStock(board,nlcannhat(target)) == True:
                print(236)
                return player_05.getOneStock(nlcannhat(target),board,{})
            else:
                if len(listnguyenlieucon(board)) >2:
                    print(240)
                    return player_05.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{})
                else:
                    if player_05.checkUpsiteDown() == True:
                        print(244)
                        return player_05.getUpsideDown(theseup(board),board,{})
                    else:
                        print("skip chỗ 2")
                        return board