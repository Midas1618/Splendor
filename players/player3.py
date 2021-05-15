from base import player
import random
player_03 = player.Player("Thao", 0)

def action(board,arr_player):
    if laythe(board,"I") != None:
        return player_03.getCard(laythe(board,"I"), board)
    if laythe(board,"II") != None:
        return player_03.getCard(laythe(board,"II"), board)
    if laythe(board,"III") != None:
        return player_03.getCard(laythe(board,"III"), board)
    stock1 = GetChoose1Stocks(board)
    if stock1 != None:
        return player_03.getOneStock(stock1,board,Luachonbothe(stock1,stock1))
    stock3 = GetChoose3Stocks(board)
    if stock3 != None:
        return player_03.getThreeStocks(stock3[0],stock3[1],stock3[2],board,Luachonbothe(stock3[0],stock3[1],stock3[2]))
    if Upthe(board) != None:
        return player_03.getUpsideDown(Upthe(board),board, Luachonbothe("auto_color"))
    return board

# Loại bỏ thẻ thừa
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
    #Copy Nguyên liệu ban đầu
    dict_bd = player_03.stocks.copy()
    #Thêm Nguyên liệu
    for x in args:
        dict_bd[x] += 1
    #Kiểm tra nguyên liệu còn
    danhsachcon = checknguyenlieucon(player_03)
    #Thực hiện bỏ thẻ. Đk bỏ thẻ là bỏ lần lượt.
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
    
#kiểm tra xem có thể lấy nguyên liệu không (nếu có thì lấy 1 nguyên liệu, không thì lấy 3 nguyên liệu)
def GetChoose1Stocks (board):
    nguyenlieucothelay1 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_03.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay1.append(nguyenlieu)
    if  len(nguyenlieucothelay1)>0:
        return nguyenlieucothelay1[0]
    else:
        return None
def GetChoose3Stocks (board):
    nguyenlieucothelay3 =[]  
    for nguyenlieu in board.stocks.keys():       
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucothelay3.append(nguyenlieu)
    if len(nguyenlieucothelay3) > 2 and player_03.checkThreeStocks(board,nguyenlieucothelay3[0], nguyenlieucothelay3[1],nguyenlieucothelay3[2]) == True:
        return nguyenlieucothelay3
    else:
        return None
# úp thẻ
def Upthe (board):
    if sum(player_03.stocks.values()) > 7:
        return board.dict_Card_Stocks_Show["II"][0]
    else:
        return None
    # if sum(player_03.stocks.values()) > 7:
    #     if sum(player_03.stocks.values()) == 10:
    #         bo = {}
    #         for nguyenlieu in player_03.stocks.keys():
    #             if player_03.stocks[nguyenlieu] >0:
    #                 bo[nguyenlieu] = 1
    #                 break
    #         return player_03.getUpsideDown(board.dict_Card_Stocks_Show["II"][0],board,bo)
    #     return player_03.getUpsideDown(board.dict_Card_Stocks_Show["II"][0],board,{})

# Lấy thẻ
def laythe (board,loai):
    for the in board.dict_Card_Stocks_Show[loai]:
        if player_03.checkGetCard(the) == True:
            return the




# Xếp hạng các thẻ
# def LuaChonTheUuTien (board):
#     diem = 0
#     theuutien = None
#     for the in board.dict_Card_Stocks_Show["II"]:
#         if the.type_stock == "White" or the.type_stock == "Black" or the.type_stock == "Red" and sum(board.stocks.keys()) < 11:
#             if the.score > diem:
#                 diem = the.score
#                 theuutien = the
#                 return theuutien      
#         else:
#             for the in board.dict_Card_Stocks_Show["I"]:
#                 if the.type_stock == "White" or the.type_stock == "Black" or the.type_stock == "Red" and sum(board.stocks.keys()) < 11:
#                     if the.score > diem:
#                         diem = the.score
#                         theuutien = the
#                         return theuutien  
            
#     if sum(player_03.card_open) == 3:
#             for the in board.dict_Card_Stocks_Show["III"]:
#                 if the.type_stock == "White" or the.type_stock == "Black" or the.type_stock == "Red" and sum(board.stocks.keys()) < 11:
#                     if the.score > diem:
#                         diem = the.score
#                         theuutien = the     
#                         return theuutien
#                 else:
#                     for the in board.dict_Card_Stocks_Show["II"]:
#                         if the.type_stock == "White" or the.type_stock == "Black" or the.type_stock == "Red" and sum(board.stocks.keys()) < 11:
#                             if the.score > diem:
#                                 diem = the.score
#                                 theuutien = the
#                                 return theuutien 
#                         else:
#                             for the in board.dict_Card_Stocks_Show["I"]:
#                                 if the.type_stock == "White" or the.type_stock == "Black" or the.type_stock == "Red" and sum(board.stocks.keys()) < 11:
#                                     if the.score > diem:
#                                         diem = the.score
#                                         theuutien = the
#                                         return theuutien  

#xếp hạng nguyên liệu
# def nguyenlieucannhat(board):
#     nguyenlieucannhat = None
#     soluongcan = 0
#     for nguyenlieu in board.stocks.keys():
#         if board.stocks[nguyenlieu] > soluongcan:
#             soluongcan = board.stocks[nguyenlieu]
#             nguyenlieucannhat = nguyenlieu
#     return nguyenlieucannhat


# def nguyenlieucon(board):
#     nguyenlieucon = []
#     for nguyenlieu in board.stocks.keys():
#         if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color" and nguyenlieu != nguyenlieucannhat(board):
#             nguyenlieucon.append(nguyenlieu)
#     return nguyenlieucon


# def nguyenlieucannhi(board):
#     luongnguyenlieu = 10
#     nguyenlieuthu2 = None
#     for nguyenlieu in nguyenlieucon(board):
#         if board.stocks[nguyenlieu] > 0:
#             return nguyenlieu
#             luongnguyenlieu = -1
#             break
#         else:
#             if board.stocks[nguyenlieu] < luongnguyenlieu:
#                 luongnguyenlieu = board.stocks[nguyenlieu]
#                 nguyenlieuthu2 = nguyenlieu
#     if luongnguyenlieu != -1:
#         return nguyenlieuthu2


# def nguyenlieucanba(board):
#     luongnguyenlieu = 10
#     nguyenlieuthu3 = None
#     for nguyenlieu in nguyenlieucon(board):
#         if nguyenlieu != nguyenlieucannhi(board):
#             if board.stocks[nguyenlieu] > 0:
#                 return nguyenlieu
#                 luongnguyenlieu = -1
#                 break
#             else:
#                 if board.stocks[nguyenlieu] < luongnguyenlieu:
#                     luongnguyenlieu = board.stocks[nguyenlieu]
#                     nguyenlieuthu3 = nguyenlieu
#     if luongnguyenlieu != -1:
#         return nguyenlieuthu3



# # Lấy thẻ
# def Laythe (board,loai):
#     for the in board.dict_Card_Stocks_Show[loai]:
#         if player_03.checkGetCard(the) == True:
#             return the
    


        

