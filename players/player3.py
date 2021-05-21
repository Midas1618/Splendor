# from base import player

# player_03 = player.Player("Thao12345", 0)

# def action(board, arr_player):
#     if laythe(board,"III") != None:
#         return player_03.getCard(laythe(board,"III"), board)
#     if laythe(board,"II") != None:
#         return player_03.getCard(laythe(board,"II"), board)
#     if laythe(board,"I") != None:
#         return player_03.getCard(laythe(board,"I"), board)
#     else:
#         print(player_03.stocks.values())
#         if sum(player_03.stocks.values()) >8:
#             if player_03.checkUpsiteDown() == True:
#                 if sum(player_03.stocks.values()) == 9:
#                     return player_03.getUpsideDown(theseup(board),board,{})
#                 if sum(player_03.stocks.values()) == 10:
#                     return player_03.getUpsideDown(theseup(board),board,Luachonbothe("auto_color"))
#             else:
#                 print(player_03.stocks.values())
#                 if len(dsnguyenlieuconlaitrenbanlaitrenban(board)) >2:
#                     if sum(player_03.stocks.values()) == 9:
#                         return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,Luachonbothe(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2]))
#                     if sum(player_03.stocks.values()) == 10:
#                         return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,Luachonbothe(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2]))
#         if sum(player_03.stocks.values()) == 8:
#             if len(dsnguyenlieuconlaitrenbanlaitrenban(board)) >2:
#                 return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,Luachonbothe(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2]))
#             else:
#                 if player_03.checkUpsiteDown() == True:
#                     return player_03.getUpsideDown(theseup(board),board,{})
#         else:
#             if sum(player_03.stocks.values()) < 8:
#                 if player_03.checkOneStock(board,nguyenlieucannhat(theuutien(board))) == True:
#                     return player_03.getOneStock(nguyenlieucannhat(theuutien(board)),board,{})
#                 else:
#                     if len(dsnguyenlieuconlaitrenbanlaitrenban(board)) >2:
#                         return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,{})
#                     else:
#                         if player_03.checkUpsiteDown() == True:
#                             return player_03.getUpsideDown(theseup(board),board,{})
#         return board           



# def Luachonbothe(*args):
#     dict_bo = {
#         "red":0,
#         "blue":0,
#         "white":0,
#         "green":0,
#         "black":0,
#         "auto_color": 0
#     }
#     #Copy Nguyên liệu ban đầu
#     dict_bd = player_03.stocks.copy()
#     #Thêm Nguyên liệu
#     for x in args:
#         dict_bd[x] += 1
#     #Kiểm tra nguyên liệu còn
#     danhsachcon = checknguyenlieucon(player_03)
#     # #Thực hiện bỏ thẻ. Đk bỏ thẻ là bỏ lần lượt.
#     if sum(dict_bd.values()) > 10:
#         n = sum(dict_bd.values()) - 10
#         i = 0
#         while n != 0:
#             if dict_bd[danhsachcon[i]] != 0:
#                 dict_bo[danhsachcon[i]] +=1
#                 dict_bd[danhsachcon[i]] -=1
#                 n -= 1
#             else:
#                 i += 1
#     return dict_bo

# # Loại bỏ thẻ thừa
# def checknguyenlieucon(board):
#     nguyenlieucon = []
#     for nguyenlieu in board.stocks.keys():
#         if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
#             nguyenlieucon.append(nguyenlieu)
#     return nguyenlieucon

# # danh sách ưu tiên lấy thẻ
# def dstheuutienlay(board):
#     thecothelay = []
#     if len(player_03.card_upside_down) > 0:
#         for the in player_03.card_upside_down:
#             if player_03.checkGetCard(the) == True:
#                 thecothelay.append(the)
#     for the in board.dict_Card_Stocks_Show["III"]:
#         if player_03.checkGetCard(the) == True:
#             thecothelay.append(the)
#     for the in board.dict_Card_Stocks_Show["II"]:
#         if player_03.checkGetCard(the) == True:
#             thecothelay.append(the)
#     for the in board.dict_Card_Stocks_Show["I"]:
#         if player_03.checkGetCard(the) == True:
#             thecothelay.append(the)
#     return thecothelay


# # danh sách những nguyên liệu còn trên bàn
# def dsnguyenlieuconlaitrenbanlaitrenban(board):
#     nguyenlieuconlaitrenban = []
#     for nguyenlieu in board.stocks.keys():
#         if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
#             nguyenlieuconlaitrenban.append(nguyenlieu)
#     return nguyenlieuconlaitrenban


# def ListCard(board):
#     ListCard = []
#     ListCard.extend(board.dict_Card_Stocks_Show["III"])
#     ListCard.extend(board.dict_Card_Stocks_Show["II"])
#     ListCard.extend(board.dict_Card_Stocks_Show["I"])
#     return ListCard

# # tìmsố lượng nguyên liệu thiếu mỗi lotrên bàn
# def dictnguyenlieuthieu(the):
#     nguyenlieuthieu = {}
#     for nguyenlieu in the.stocks.keys():
#         if the.stocks[nguyenlieu] > (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu]):
#             nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu])
#     return nguyenlieuthieu   

# #định giá điểm của các thẻ trên bàn
# def danhgiadiemtrenthe(board):
#     diemdanhgiamoithe = {}
#     nguyenlieuconlai = dsnguyenlieuconlaitrenbanlaitrenban(board)
#     for the in ListCard(board):
#         if the not in player_03.card_upside_down:
#             if sum(the.stocks.values()) > 10:
#                 diemdanhgiamoithe[the] = 0
#             if len(dictnguyenlieuthieu(the)) == 0:
#                 songuyenlieu = sum(the.stocks.values()) *10
#             else:
#                 songuyenlieu = sum(the.stocks.values())
#             for nguyenlieu in dictnguyenlieuthieu(the).keys():
#                 if nguyenlieu not in nguyenlieuconlai:
#                     songuyenlieu =  sum(the.stocks.values()) /10
#             diem = songuyenlieu / (the.score +1)
#             diemdanhgiamoithe[the] = diem
#     return diemdanhgiamoithe

# # lựa chọn thẻ ưu tiên
# def theuutien(board):
#     diemcaonhat = 0
#     theuutien = None
#     for the in board.dict_Card_Stocks_Show["III"]:
#         if the.score ==5:
#             theuutien = the
#             return theuutien
#     for the in danhgiadiemtrenthe(board).keys():
#         if danhgiadiemtrenthe(board)[the] > diemcaonhat:
#             diemcaonhat = danhgiadiemtrenthe(board)[the]
#             theuutien = the
#     return theuutien


# # tìm loại và số lượng nguyên liệu còn thiếu để lấy thẻ
# def dictnguyenlieuthieu(the):
#     nguyenlieuthieu = {}
#     for nguyenlieu in the.stocks.keys():
#         if the.stocks[nguyenlieu] > (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu]):
#             nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu])
#     return nguyenlieuthieu    




# def nguyenlieucannhat(board):
#     nguyenlieucannhat = None
#     soluongcan = 0
#     for nguyenlieu in board.stocks.keys():
#         if board.stocks[nguyenlieu] > soluongcan:
#             soluongcan = board.stocks[nguyenlieu]
#             nguyenlieucannhat = nguyenlieu
#     return nguyenlieucannhat


# # xếp hạng ưu tiên lấy nguyên liệu
# def nguyenlieuutien(board):
#     nguyenlieuvadiem = {}
#     a = {}
#     for nguyenlieu in dsnguyenlieuconlaitrenbanlaitrenban(board):
#         if nguyenlieu in dictnguyenlieuthieu(theuutien(board)).keys():
#             diem = dictnguyenlieuthieu(theuutien(board))[nguyenlieu]
#         else:
#             diem = board.stocks[nguyenlieu]/10
#         nguyenlieuvadiem[nguyenlieu] = diem
#     a = {k: v for k, v in sorted(nguyenlieuvadiem.items(), key=lambda item: item[1],reverse=True)}
#     return list(a.keys())

# # tìm thẻ để úp
# def theseup(board):
#     diemcaonhat = 0
#     theuutien = None
#     for the in danhgiadiemtrenthe(board).keys():
#         if danhgiadiemtrenthe(board)[the] > diemcaonhat:
#             diemcaonhat = danhgiadiemtrenthe(board)[the]
#             theuutien = the
#     return theuutien

# # trả nguyên liệu thừa
# def nguyenlieuminhco(board):
#     dictchuaxephang = {}
#     a = {}
#     for nguyenlieu in theuutien(board).stocks.keys():
#         diem = player_03.stocks[nguyenlieu] - theuutien(board).stocks[nguyenlieu]
#         dictchuaxephang[nguyenlieu] = diem
#     a = {k: v for k, v in sorted(dictchuaxephang.items(), key=lambda item: item[1],reverse=True)}
#     return list(a.keys())

        


# # Lấy thẻ
# def laythe (board,loai):
#     for the in board.dict_Card_Stocks_Show[loai]:
#         if player_03.checkGetCard(the) == True:
#             return the
#         else:
#             return None





from base import player

player_03 = player.Player("Thao", 0)

def action(board, arr_player):
    if thelayngay(board) != None and thelayngay(board):
        return player_03.getCard(thelayngay(board),board)
    if laythe(board,"III") != None:
        return player_03.getCard(laythe(board,"III"), board)
    if laythe(board,"II") != None:
        return player_03.getCard(laythe(board,"II"), board)
    if laythe(board,"I") != None:
        return player_03.getCard(laythe(board,"I"), board)
    
    else:
        if sum(player_03.stocks.values()) >8:
            if player_03.checkUpsiteDown() == True:
                if sum(player_03.stocks.values()) == 9:
                    return player_03.getUpsideDown(theseup(board),board,{})
                if sum(player_03.stocks.values()) == 10:
                    return player_03.getUpsideDown(theseup(board),board,Luachonbothe("auto_color"))
            else:
                # print(player_03.stocks.values())
                if len(dsnguyenlieuconlaitrenbanlaitrenban(board)) >2:
                    if sum(player_03.stocks.values()) == 9:
                        return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,Luachonbothe(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2]))
                    if sum(player_03.stocks.values()) == 10:
                        return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,Luachonbothe(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2]))
        if sum(player_03.stocks.values()) == 8:
            if len(dsnguyenlieuconlaitrenbanlaitrenban(board)) >2:
                return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,Luachonbothe(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2]))
            else:
                if player_03.checkUpsiteDown() == True:
                    return player_03.getUpsideDown(theseup(board),board,{})
        else:
            if sum(player_03.stocks.values()) < 8:
                if player_03.checkOneStock(board,nguyenlieucannhat(theuutien(board))) == True:
                    return player_03.getOneStock(nguyenlieucannhat(theuutien(board)),board,{})
                else:
                    if len(dsnguyenlieuconlaitrenbanlaitrenban(board)) >2:
                        return player_03.getThreeStocks(nguyenlieuutien(board)[0],nguyenlieuutien(board)[1],nguyenlieuutien(board)[2],board,{})
                    else:
                        if player_03.checkUpsiteDown() == True:
                            return player_03.getUpsideDown(theseup(board),board,{})
        return board           



def Luachonbothe(*args):
    dict_bo = {
        "red":0,
        "blue":0,
        "white":0,
        "green":0,
        "black":0,
        "auto_color": 0
    }
    #Copy Nguyên liệu ban đầu
    dict_bd = player_03.stocks.copy()
    #Thêm Nguyên liệu
    for x in args:
        dict_bd[x] += 1
    #Kiểm tra nguyên liệu còn
    danhsachcon = checknguyenlieucon(player_03)
    # #Thực hiện bỏ thẻ. Đk bỏ thẻ là bỏ lần lượt.
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

# Loại bỏ thẻ thừa
def checknguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon


# danh sách ưu tiên lấy thẻ
def dstheuutienlay(board):
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
    return thecothelay


# danh sách những nguyên liệu còn trên bàn
def dsnguyenlieuconlaitrenbanlaitrenban(board):
    nguyenlieuconlaitrenban = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieuconlaitrenban.append(nguyenlieu)
    return nguyenlieuconlaitrenban


def ListCard(board):
    ListCard = []
    ListCard.extend(board.dict_Card_Stocks_Show["III"])
    ListCard.extend(board.dict_Card_Stocks_Show["II"])
    ListCard.extend(board.dict_Card_Stocks_Show["I"])
    return ListCard

# tìmsố lượng nguyên liệu thiếu mỗi lotrên bàn
def dictnguyenlieuthieu(the):
    nguyenlieuthieu = {}
    for nguyenlieu in the.stocks.keys():
        if the.stocks[nguyenlieu] > (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu]):
            nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu])
    return nguyenlieuthieu   

#định giá điểm của các thẻ trên bàn
def danhgiadiemtrenthe(board):
    diemdanhgiamoithe = {}
    nguyenlieuconlai = dsnguyenlieuconlaitrenbanlaitrenban(board)
    for the in ListCard(board):
        if the not in player_03.card_upside_down:
            if sum(the.stocks.values()) > 10:
                diemdanhgiamoithe[the] = 0
            if len(dictnguyenlieuthieu(the)) == 0:
                songuyenlieu = sum(the.stocks.values()) *10
            else:
                songuyenlieu = sum(the.stocks.values())
            for nguyenlieu in dictnguyenlieuthieu(the).keys():
                if nguyenlieu not in nguyenlieuconlai:
                    songuyenlieu =  sum(the.stocks.values()) /10
            diem = songuyenlieu / (the.score +1)
            diemdanhgiamoithe[the] = diem
    return diemdanhgiamoithe

# lựa chọn thẻ ưu tiên
def theuutien(board):
    diemcaonhat = 0
    theuutien = None
    for the in board.dict_Card_Stocks_Show["III"]:
        if the.score ==5:
            theuutien = the
            return theuutien
    for the in danhgiadiemtrenthe(board).keys():
        if danhgiadiemtrenthe(board)[the] > diemcaonhat:
            diemcaonhat = danhgiadiemtrenthe(board)[the]
            theuutien = the
    return theuutien


# tìm loại và số lượng nguyên liệu còn thiếu để lấy thẻ
def dictnguyenlieuthieu(the):
    nguyenlieuthieu = {}
    for nguyenlieu in the.stocks.keys():
        if the.stocks[nguyenlieu] > (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu]):
            nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_03.stocks[nguyenlieu] + player_03.stocks_const[nguyenlieu])
    return nguyenlieuthieu    

# trong những thẻ có thể mua ngay turn này, thẻ nào nhiều điểm nhất
def thelayngay(board):
    diemcothelay = -1
    thelayngay = None
    for the in dstheuutienlay(board):
        if the.score > 0 and the.score > diemcothelay:
            diemcothelay = the.score
            thelayngay = the
    return thelayngay


def nguyenlieucannhat(board):
    nguyenlieucannhat = None
    soluongcan = 0
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > soluongcan:
            soluongcan = board.stocks[nguyenlieu]
            nguyenlieucannhat = nguyenlieu
    return nguyenlieucannhat


# xếp hạng ưu tiên lấy nguyên liệu
def nguyenlieuutien(board):
    nguyenlieuvadiem = {}
    a = {}
    for nguyenlieu in dsnguyenlieuconlaitrenbanlaitrenban(board):
        if nguyenlieu in dictnguyenlieuthieu(theuutien(board)).keys():
            diem = dictnguyenlieuthieu(theuutien(board))[nguyenlieu]
        else:
            diem = board.stocks[nguyenlieu]/10
        nguyenlieuvadiem[nguyenlieu] = diem
    a = {k: v for k, v in sorted(nguyenlieuvadiem.items(), key=lambda item: item[1],reverse=True)}
    return list(a.keys())

# nguyên liệu không quan trọng
def get_token_return(board):
    token_can_return = player_03.stocks
    dict_important_token = {}
    dict_important_token['red'] = 0
    dict_important_token['blue'] = 0
    dict_important_token['green'] = 0
    dict_important_token['white'] = 0
    dict_important_token['black'] = 0
    for card in player_03.card_upside_down:
        dict_important_token['red'] += card.stocks['red'] - player_03.stocks_const['red'] - player_03.stocks['red']
        dict_important_token['blue'] += card.stocks['blue'] - player_03.stocks_const['blue'] - player_03.stocks['blue']
        dict_important_token['green'] += card.stocks['green'] - player_03.stocks_const['green'] - player_03.stocks['green']
        dict_important_token['white'] += card.stocks['white'] - player_03.stocks_const['white'] - player_03.stocks['white']
        dict_important_token['black'] += card.stocks['black'] - player_03.stocks_const['black'] - player_03.stocks['black']
    list_token = list(dict_important_token.keys())
    list_number_token = list(dict_important_token.values())
    dict_token_not_important = {}
    count = 0
    while count < len(list_token):
        if list_token[list_number_token.index(max(list_number_token))] in token_can_return:
            dict_token_not_important[list_token[list_number_token.index(min(list_number_token))]] = min(list_number_token)
        list_token.remove(list_token[list_number_token.index(min(list_number_token))])
        list_number_token.remove(min(list_number_token))
    return dict_token_not_important

# tìm thẻ để úp
def theseup(board):
    diemcaonhat = 0
    theuutien = None
    for the in danhgiadiemtrenthe(board).keys():
        if danhgiadiemtrenthe(board)[the] > diemcaonhat:
            diemcaonhat = danhgiadiemtrenthe(board)[the]
            theuutien = the
    return theuutien

# trả nguyên liệu thừa
def nguyenlieuminhco(board):
    dictchuaxephang = {}
    a = {}
    for nguyenlieu in theuutien(board).stocks.keys():
        diem = player_03.stocks[nguyenlieu] - theuutien(board).stocks[nguyenlieu]
        dictchuaxephang[nguyenlieu] = diem
    a = {k: v for k, v in sorted(dictchuaxephang.items(), key=lambda item: item[1],reverse=True)}
    return list(a.keys())

    

# Lấy thẻ
def laythe (board,loai):
    for the in board.dict_Card_Stocks_Show[loai]:
        if player_03.checkGetCard(the) == True:
            return the
        else:
            return None