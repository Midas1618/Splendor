from typing import Coroutine
from base import player
import random
import operator

player_01 = player.Player("Hoang", 0)

def action(board, arr_player):
    return moiturn(board,player_01)
    # return board

#List thẻ có thể mua
def list_cards_can_open(board,player_01):

    cards_can_open = []

    for card in player_01.card_upside_down:
        if player_01.checkGetCard(card) == True:
            cards_can_open.append(card)
    
    for card in board.dict_Card_Stocks_Show["I"]:
        if player_01.checkGetCard(card) == True:
            cards_can_open.append(card)
    
    for card in board.dict_Card_Stocks_Show["II"]:
        if player_01.checkGetCard(card) == True:
            cards_can_open.append(card)

    for card in board.dict_Card_Stocks_Show["III"]:
        if player_01.checkGetCard(card) == True:
            cards_can_open.append(card)
    
    return cards_can_open


#Thẻ ưu tiên mua trước
def card_to_buy_first(board,player_01):

    card_first = None

    x = 0

    for card in list_cards_can_open(board,player_01):
        if ( card.score / sum(card.stocks.values()) ) > x:
            card_first = card
    
    return card_first

#dict tổng stock trên tay, không tính vàng
def dict_total_normal_stocks_on_hand(player_01):

    total_normal_stocks_on_hand = {"red": 0, "blue": 0, "green": 0, "white": 0, "black": 0}
    
    for color in total_normal_stocks_on_hand.keys():
        total_normal_stocks_on_hand[color] = player_01.stocks[color] + player_01.stocks_const[color]
    
    return total_normal_stocks_on_hand

#list_rank các màu token đang có trên tay, theo số lượng giảm dần
def list_rank_color_on_hand_descending(player_01):

    list_sorted_values = list(sorted(dict_total_normal_stocks_on_hand(player_01).values(),reverse=True))

    rank_color_on_hand_descending = []

    for value in list_sorted_values:
        for color in dict_total_normal_stocks_on_hand(player_01).keys():
            if dict_total_normal_stocks_on_hand(player_01)[color] == value:
                if player_01.stocks[color] >0:
                    rank_color_on_hand_descending.append(color)
    
    return rank_color_on_hand_descending

#dict các token yêu cầu trong thẻ đang úp
def dict_token_in_upside_down(player_01):

    token_in_upside_down = {"red": 0, "blue": 0, "green": 0, "white": 0, "black": 0}

    for card in player_01.card_upside_down:
        for color in card.stocks.keys():
            token_in_upside_down[color] += card.stocks[color]
    
    return token_in_upside_down

#dict các token còn thiếu cho các thẻ đang úp
def dict_token_required_for_upside_down(player_01):

    token_required_for_upside_down = {"red": 0, "blue": 0, "green": 0, "white": 0, "black": 0}

    for color in token_required_for_upside_down.keys():
        token_required_for_upside_down[color] = dict_token_in_upside_down(player_01)[color] - dict_total_normal_stocks_on_hand(player_01)[color]
    
    return token_required_for_upside_down


#Xếp hạng các màu token muốn lấy, ưu tiên giảm dần, trong trường hợp đang có thẻ úp
def list_rank_color_for_upside_down(player_01):

    list_sorted_values = list(sorted(dict_token_required_for_upside_down(player_01).values(),reverse=True))
    rank_color_for_upside_down = []

    for value in list_sorted_values:
        for color in dict_token_required_for_upside_down(player_01).keys():
            if dict_token_required_for_upside_down(player_01)[color] == value:
                rank_color_for_upside_down.append(color)
    
    return rank_color_for_upside_down





#Xếp hạng các màu token có thể lấy, ưu tiên giảm dần, trong trường hợp đang có thẻ úp
def list_rank_color_can_get(board,player_01):

    rank_color_can_get = []

    for color in list_rank_color_for_upside_down(player_01):
        if board.stocks[color] >0 :
            rank_color_can_get.append(color)
    return rank_color_can_get

#Lưu kết quả màu 1, trong trường hợp đang có thẻ úp
def Color1_has_upside_down(board, player_01):

    Color1 = None
    if len(list_rank_color_can_get(board, player_01)) > 0:
        Color1 = list_rank_color_can_get(board, player_01)[0]
    
    return Color1

#Lưu kết quả màu 2, trong trường hợp đang có thẻ úp
def Color2_has_upside_down(board,player_01):

    Color2 = None
    if len(list_rank_color_can_get(board, player_01)) > 1:
        Color2 = list_rank_color_can_get(board, player_01)[1]
    
    return Color2

#Lưu kết quả màu 3, trong trường hợp đang có thẻ úp
def Color3_has_upside_down(board, player_01):

    Color3 = None
    if len(list_rank_color_can_get(board, player_01)) > 2:
        Color3 = list_rank_color_can_get(board, player_01)[2]
    
    return Color3

#dict token còn thiếu cho thẻ úp, sau khi đã lấy thêm 2 token
def dict_token_required_remaining_for_upside_down(board,player_01):

    token_required_remaining_for_upside_down = dict_token_required_for_upside_down(player_01)

    for color in list_rank_color_for_upside_down(player_01):
        if player_01.checkOneStock(board, color) == True:
            token_required_remaining_for_upside_down[color] -= 2
            return token_required_remaining_for_upside_down
    
#Sau khi lấy 2 token, xếp hạng lại các màu token muốn trả, ưu tiên giảm dần, trong trường hợp đang có thẻ úp

def list_rerank_color_to_return_afterget2(board,player_01):

    rerank_color_to_return_afterget2 = []

    list_sorted_values = list(sorted(dict_token_required_remaining_for_upside_down(board,player_01).values()))

    for value in list_sorted_values:
        for color in dict_token_required_remaining_for_upside_down(board,player_01).keys():
            if dict_token_required_remaining_for_upside_down(board,player_01)[color] == value:
                rerank_color_to_return_afterget2.append(color)
    
    return rerank_color_to_return_afterget2


#list rank màu token có thể lấy trong trường hợp không có thẻ úp
def list_rank_color_can_get_alt(board):

    rank_color_can_get_alt = []

    # for color in board.stocks.keys():
    #     if ( board.stocks[color] > 0 ) & (color != "auto_color"):
    #         rank_color_can_get_alt.append(color)

    # return rank_color_can_get_alt

    total_score_board = 0
    for card in board.dict_Card_Stocks_Show["II"]:
        total_score_board += card.score
    for card in board.dict_Card_Stocks_Show["II"]:
        total_score_board += card.score

    color_valuation = { "red": 0, "blue": 0, "green": 0, "white": 0, "black": 0}
    for color in color_valuation.keys():
        for card in board.dict_Card_Stocks_Show["II"]:
            color_valuation[color] += card.stocks[color]
        for item in board.dict_Card_Stocks_Show["III"]:
            color_valuation[color] += item.stocks[color]
    
    for color in color_valuation.keys():
        if color_valuation[color] > 0:
            color_valuation[color] = total_score_board / color_valuation[color]
        if color_valuation[color] == 0:
            del color_valuation[color]
    
    list_sorted_value = list(sorted(color_valuation.values(),reverse=True))

    for value in list_sorted_value:
        for color in color_valuation.keys():
            if color_valuation[color] == value:
                rank_color_can_get_alt.append(color)
    
    return rank_color_can_get_alt
    
    
    
    
    

#Dict return trong trường hợp úp thẻ mà token trên tay đã = 10
def dict_return_get_upside_down(player_01):

    dict_return = {}

    for color in player_01.stocks.keys():
        if player_01.stocks[color] > 0 & dict_token_in_upside_down(player_01)[color] == 0:
            dict_return[color] = 1
            return dict_return

    list_sorted_values = list(sorted(dict_token_required_for_upside_down(player_01).values()))
    
    rank_color_to_return = []

    for value in list_sorted_values:
        for color in dict_token_required_for_upside_down(player_01).keys():
            if dict_token_required_for_upside_down(player_01)[color] == value:
                rank_color_to_return.append[color]
    
    for color in rank_color_to_return:
        if player_01.stocks[color] > 0:
            dict_return[color] = 1
            return dict_return

    for color in player_01.stocks.keys:
        if player_01.stocks[color] > 0:
            dict_return[color] = 1
            return dict_return

    
    
#Dict return trong trường hợp lấy 2 token và cần trả lại
def dict_return_get_one_type_stock(board,player_01):
    
    dict_return = {}

    if len(player_01.card_upside_down) > 0:
        
        if sum(player_01.stocks.values()) == 9:
        
            for color in list_rerank_color_to_return_afterget2(board,player_01):
                if player_01.stocks[color] > 0:
                    dict_return[color] = 1
                    return dict_return
            
            for color in list_rank_color_on_hand_descending(player_01):
                if player_01.stocks[color] > 0:
                    dict_return[color] = 1
                    return dict_return
            
        
        elif sum(player_01.stocks.values()) == 10:

            for color in list_rerank_color_to_return_afterget2(board,player_01):

                while sum(dict_return.values()) <2:
                
                    if player_01.stocks[color] >= 2:
                        if sum(dict_return.values()) == 0:
                            dict_return[color] = 2
                            return dict_return
                        else:
                            dict_return[color] = 1
                            return dict_return                        
                    
                    if player_01.stocks[color] == 1:
                        dict_return[color] = 1

            if sum(dict_return.values()) == 2:
                return dict_return
            
            for color in list_rank_color_on_hand_descending(player_01):

                while sum(dict_return.values()) <2:

                    if player_01.stocks[color] >=2:
                        if sum(dict_return.values()) == 0:
                            dict_return[color] = 2
                            return dict_return
                        else:
                            dict_return[color] = 1
                            return dict_return

                    if player_01.stocks[color] == 1:
                        dict_return[color] = 1

            return dict_return            
        

    if sum(player_01.stocks.values()) == 9:        
        # for color in player_01.stocks.keys():
        for color in list_rank_color_on_hand_descending(player_01):
            if player_01.stocks[color] > 0:
                dict_return[color] = 1
                return dict_return
    
    elif sum(player_01.stocks.values()) == 10:
        # for color in player_01.stocks.keys():
        for color in list_rank_color_on_hand_descending(player_01):

            while sum(dict_return.values()) <2:

                if player_01.stocks[color] >=2:
                    if sum(dict_return.values()) == 0:
                        dict_return[color] = 2
                        return dict_return
                    else:
                        dict_return[color] = 1
                        return dict_return
                if player_01.stocks[color] == 1:
                    dict_return[color] = 1

    else:
        return dict_return

    
    
#Dict return trường hợp lấy 3 token
def dict_return_get_three_stocks(player_01):
    dict_return = {}

    if sum(player_01.stocks.values()) == 8:

        # for color in player_01.stocks.keys():
        #     if player_01.stocks[color] > 0:
        #         dict_return[color] = 1
        #         return dict_return

        for color in list_rank_color_on_hand_descending(player_01):
            if player_01.stocks[color] > 0:
                dict_return[color] = 1
                return dict_return

    elif sum(player_01.stocks.values()) == 9:

        # for color in player_01.stocks.keys():
        for color in list_rank_color_on_hand_descending(player_01):

            while sum(dict_return.values()) <2:

                if player_01.stocks[color] >=2:
                    if sum(dict_return.values()) == 0:
                        dict_return[color] = 2
                        return dict_return
                    else:
                        dict_return[color] = 1
                        return dict_return

                if player_01.stocks[color] == 1:
                    dict_return[color] = 1
            ##print(363)
            return dict_return
    
    elif sum(player_01.stocks.values()) == 10:

        # for color in player_01.stocks.keys():
        for color in list_rank_color_on_hand_descending(player_01):

            while sum(dict_return.values()) <3:

                if player_01.stocks[color] >=3:

                    if sum(dict_return.values()) == 0:
                        dict_return[color] = 3
                        return dict_return
                    
                    elif sum(dict_return.values()) == 1:
                        dict_return[color] = 2
                        return dict_return

                    elif sum(dict_return.values()) == 2:
                        dict_return[color] = 1
                        return dict_return

                if player_01.stocks[color] == 2:

                    if sum(dict_return.values()) == 0:                    
                        dict_return[color] = 2
                    
                    elif sum(dict_return.values()) == 1:
                        dict_return[color] = 2
                        return dict_return
                    
                    elif sum(dict_return.values()) == 2:
                        dict_return[color] = 1
                        return dict_return
                
                if player_01.stocks[color] == 1:                    
                    dict_return[color] = 1
            ##print(402)
            return dict_return
    
    else:
        return dict_return



#dict_return general
def dict_return_general(board,*args):
    
    
    dict_return = {
        "red":0,
        "blue":0,
        "white":0,
        "green":0,
        "black":0,
        "auto_color": 0
    }
    #Copy Nguyên liệu ban đầu
    dict_start = player_01.stocks.copy()
    #Thêm Nguyên liệu
    for x in args:
        dict_start[x] += 1
    #Kiểm tra nguyên liệu còn
    list_sorted_values = list(sorted(dict_total_normal_stocks_on_hand(player_01).values(),reverse=True))
    list_sorted_color = []
    for value in list_sorted_values:
        for color in dict_total_normal_stocks_on_hand(player_01):
            if dict_total_normal_stocks_on_hand(player_01)[color] == value:
                list_sorted_color.append(color)
    #Thực hiện bỏ thẻ. Đk bỏ thẻ là bỏ lần lượt.
    if sum(dict_start.values()) > 10:
        n = sum(dict_start.values()) - 10
        i = 0
        
        while n != 0:
            if dict_start[list_sorted_color[i]] != 0:
                dict_return[list_sorted_color[i]] +=1
                dict_start[list_sorted_color[i]] -=1
                n -= 1
            else:
                i += 1
    return dict_return

    

    


def moiturn(board,player_01):
    
    if len(list_cards_can_open(board,player_01)) > 0:
        if card_to_buy_first(board,player_01) != None:
            return player_01.getCard(card_to_buy_first(board,player_01),board)

    for card in board.dict_Card_Stocks_Show["III"]:

        if card.score == 5:
            if len(player_01.card_upside_down) <2:

                if sum(player_01.stocks.values()) == 10:
                    ##print(424)
                    return player_01.getUpsideDown(card,board,dict_return_get_upside_down(player_01))
                
                else:
                    ##print(426)
                    return player_01.getUpsideDown(card,board,{})
        
        if ( card.score == 4 ) & ( sum(card.stocks.values())  == 7 ) :
            if len(player_01.card_upside_down) <2:

                if sum(player_01.stocks.values()) == 10:
                    ##print(433)
                    return player_01.getUpsideDown(card,board,dict_return_get_upside_down(player_01))
                
                else:
                    ##print(436)
                    return player_01.getUpsideDown(card,board,{})
        
    for card in board.dict_Card_Stocks_Show["II"]:

        if card.score == 3:

            if len(player_01.card_upside_down) <2:

                if sum(player_01.stocks.values()) == 10:
                    ##print(445)
                    return player_01.getUpsideDown(card,board,dict_return_get_upside_down(player_01))
                
                else:
                    ##print(448)
                    return player_01.getUpsideDown(card,board,{})
        
        if ( card.score == 2 ) & ( sum(card.stocks.values()) == 5) :

            if len(player_01.card_upside_down) <2:

                if sum(player_01.stocks.values()) == 10:
                    #print(455)
                    return player_01.getUpsideDown(card,board,dict_return_get_upside_down(player_01))
                
                else:
                    #print(458)
                    return player_01.getUpsideDown(card,board,{})
    
    if len(player_01.card_upside_down) > 0:

        for color in list_rank_color_for_upside_down(player_01):

            if player_01.checkOneStock(board,color):

                if sum(player_01.stocks.values()) > 8:
                    #print(521)
                    return player_01.getOneStock(color,board,dict_return_general(board,color,color))

                else:
                    return player_01.getOneStock(color,board,{})

        if len(list_rank_color_can_get(board,player_01)) >= 3:
            #print(528)
            return player_01.getThreeStocks(Color1_has_upside_down(board,player_01),Color2_has_upside_down(board,player_01),Color3_has_upside_down(board,player_01),board,dict_return_general(board,Color1_has_upside_down(board,player_01),Color2_has_upside_down(board,player_01),Color3_has_upside_down(board,player_01)))

        # if len(list_rank_color_can_get_alt(board)) >= 3:
        #     return player_01.getThreeStocks(list_rank_color_can_get_alt(board)[0],list_rank_color_can_get_alt(board)[1],list_rank_color_can_get_alt(board)[2],board,dict_return_get_three_stocks(player_01))

    else:
        if sum(player_01.stocks.values()) < 8:

            if len(list_rank_color_can_get_alt(board)) > 0:
                for item in list_rank_color_can_get_alt(board):
                    if player_01.checkOneStock(board,item):
                        #print(485)
                        return player_01.getOneStock(item,board,{})
                
                if len(list_rank_color_can_get_alt(board)) >= 3:
                    #print(537)
                    return player_01.getThreeStocks(list_rank_color_can_get_alt(board)[0],list_rank_color_can_get_alt(board)[1],list_rank_color_can_get_alt(board)[2],board,{})

        elif sum(player_01.stocks.values()) == 8:    

            if len(list_rank_color_can_get_alt(board)) > 0:            
                for color in list_rank_color_can_get_alt(board):
                    if player_01.checkOneStock(board,color):
                        #print(497)
                        return player_01.getOneStock(color,board,{})
                
                if len(list_rank_color_can_get_alt(board)) >= 3:
                    #print(501)
                    return player_01.getThreeStocks(list_rank_color_can_get_alt(board)[0],list_rank_color_can_get_alt(board)[1],list_rank_color_can_get_alt(board)[2],board,dict_return_general(board,list_rank_color_can_get_alt(board)[0],list_rank_color_can_get_alt(board)[1],list_rank_color_can_get_alt(board)[2]))
        else:
            if len(list_rank_color_can_get_alt(board)) > 0:            
                for color in list_rank_color_can_get_alt(board):
                    if player_01.checkOneStock(board,color):
                        #print(507)
                        return player_01.getOneStock(color,board,dict_return_general(board,color,color))
                
                if len(list_rank_color_can_get_alt(board)) >= 3:
                    #print(511)
                    return player_01.getThreeStocks(list_rank_color_can_get_alt(board)[0],list_rank_color_can_get_alt(board)[1],list_rank_color_can_get_alt(board)[2],board,dict_return_general(board,list_rank_color_can_get_alt(board)[0],list_rank_color_can_get_alt(board)[1],list_rank_color_can_get_alt(board)[2]))

    return board
    
    
        



        
        
        

    


    

    




        

    
    
    



    
    

    







# # list những thẻ có thể lấy ngay
# def listthecothemua(board):
#     thecothelay = []
#     if len(player_01.card_upside_down) > 0:
#         for the in player_01.card_upside_down:
#             if player_01.checkGetCard(the) == True:
#                 thecothelay.append(the)
#     for the in board.dict_Card_Stocks_Show["III"]:
#         if player_01.checkGetCard(the) == True:
#             thecothelay.append(the)
#     for the in board.dict_Card_Stocks_Show["II"]:
#         if player_01.checkGetCard(the) == True:
#             thecothelay.append(the)
#     for the in board.dict_Card_Stocks_Show["I"]:
#         if player_01.checkGetCard(the) == True:
#             thecothelay.append(the)
#     return thecothelay

# # list những nguyên liệu có thể lấy 2
# def listnguyenlieulay2(board):
#     nguyenlieucothelay2 = []
#     for nguyenlieu in board.stocks.keys():
#         if nguyenlieu != "auto_color" and player_01.checkOneStock(board,nguyenlieu) == True:
#             nguyenlieucothelay2.append(nguyenlieu)
#     return nguyenlieucothelay2

# # danh sách những nguyên liệu còn trên bàn
# def listnguyenlieucon(board):
#     nguyenlieucon = []
#     for nguyenlieu in board.stocks.keys():
#         if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
#             nguyenlieucon.append(nguyenlieu)
#     return nguyenlieucon

# # trong những thẻ có thể mua ngay turn này, thẻ nào nhiều điểm nhất
# def thelayngay(board):
#     diemcothelay = -1
#     thelayngay = None
#     for the in listthecothemua(board):
#         if the.score > 0 and the.score > diemcothelay:
#             diemcothelay = the.score
#             thelayngay = the
#     return thelayngay

# #hàm định giá điểm
# def tinhdiem(the,player_01):
#     sonlthieunhat = 0
#     for nguyenlieu in the.stocks.keys():
#         if the.stocks[nguyenlieu] - player_01.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu] > sonlthieunhat:
#             sonlthieunhat = the.stocks[nguyenlieu] -  player_01.stocks[nguyenlieu] - player_01.stocks_const[nguyenlieu]
#     diem = the.score/sonlthieunhat
#     return diem

# def danhsachthe(board):
#     danhsachthe = []
#     danhsachthe.extend(player_01.card_upside_down)
#     danhsachthe.extend(board.dict_Card_Stocks_Show["III"])
#     danhsachthe.extend(board.dict_Card_Stocks_Show["II"])
#     danhsachthe.extend(board.dict_Card_Stocks_Show["I"])
#     return danhsachthe

# # định giá điểm từng thẻ
# def dictthecodiem(board):
#     thecodiem = {}
#     nlcon = listnguyenlieucon(board)
#     for the in danhsachthe(board):
#         dictthieu = dictnguyenlieuthieu(the)
#         if sum(the.stocks.values()) > 10:
#             thecodiem[the] = 0
#             continue
#         if len(dictthieu) == 0:
#             turn = 1
#         else:
#             turn = max(list(dictthieu.values())) + 1
#         for nguyenlieu in dictthieu.keys():
#             if nguyenlieu not in nlcon:
#                 turn = turn + 1
#         diem = (the.score + 0.2)/turn
#         thecodiem[the] = diem
#     return thecodiem

# #định giá thẻ trên bàn
# def dictthetrenban(board):
#     thecodiem = {}
#     nlcon = listnguyenlieucon(board)
#     for the in danhsachthe(board):
#         if the not in player_01.card_upside_down:
#             dictthieu = dictnguyenlieuthieu(the)
#             if sum(the.stocks.values()) > 10:
#                 thecodiem[the] = 0
#                 continue
#             if len(dictthieu) == 0:
#                 turn = 1
#             else:
#                 turn = max(list(dictthieu.values())) + 1
#             for nguyenlieu in dictthieu.keys():
#                 if nguyenlieu not in nlcon:
#                     turn = turn + 1
#             diem = (the.score + 0.2)/turn
#             thecodiem[the] = diem
#     return thecodiem

# # chọn ra thẻ có điểm cao nhất
# def thetarget(board):
#     diemcaonhat = 0
#     thetarget = None
#     for the in dictthecodiem(board).keys():
#         if dictthecodiem(board)[the] > diemcaonhat:
#             diemcaonhat = dictthecodiem(board)[the]
#             thetarget = the
#     return thetarget

# # chọn ra thẻ tốt nhất ngoài danh sách cho trước
# def theduphong(board,listthedachon):
#     diemcaonhat = 0
#     theduphong = None
#     for the in dictthecodiem(board).keys():
#         if dictthecodiem(board)[the] > diemcaonhat and the not in listthedachon:
#             diemcaonhat = dictthecodiem(board)[the]
#             theduphong = the
#     return theduphong

# # tìm loại và số lượng nguyên liệu thiếu
# def dictnguyenlieuthieu(the):
#     nguyenlieuthieu = {}
#     for nguyenlieu in the.stocks.keys():
#         if the.stocks[nguyenlieu] > (player_01.stocks[nguyenlieu] + player_01.stocks_const[nguyenlieu]):
#             nguyenlieuthieu[nguyenlieu] = the.stocks[nguyenlieu] - (player_01.stocks[nguyenlieu] + player_01.stocks_const[nguyenlieu])
#     return nguyenlieuthieu    

# # chênh giữa nl cần nhiều nhất và nhiều nhì
# def nenlay2nl(the):
#     if len(dictnguyenlieuthieu(the)) == 1:
#         return True
#     chenhlech = 0
#     for luongnlthieu in dictnguyenlieuthieu(the).values():
#         if max(dictnguyenlieuthieu(the).values()) - luongnlthieu != 0 and (max(dictnguyenlieuthieu(the).values()) - luongnlthieu) > chenhlech:
#             chenhlech = max(dictnguyenlieuthieu(the).values()) - luongnlthieu
#     if chenhlech > 1:
#         return True
#     else:
#         return False

# # tìm nguyên liệu cần nhất trong thẻ
# def nlcannhat(the):
#     sonlcan = 0
#     nlcannhat = None
#     for nguyenlieu in dictnguyenlieuthieu(the).keys():
#         if dictnguyenlieuthieu(the)[nguyenlieu] == max(list(dictnguyenlieuthieu(the).values())):
#             sonlcan = dictnguyenlieuthieu(the)[nguyenlieu]
#             nlcannhat = nguyenlieu
#             return nguyenlieu

# # chấm điểm nguyên liệu có thể lấy
# def listnguyenlieuuutien(board):
#     nguyenlieuvadiem = {}
#     a = {}
#     for nguyenlieu in listnguyenlieucon(board):
#         if nguyenlieu in dictnguyenlieuthieu(thetarget(board)).keys():
#             diem = dictnguyenlieuthieu(thetarget(board))[nguyenlieu]
#         else:
#             diem = board.stocks[nguyenlieu]/10
#         nguyenlieuvadiem[nguyenlieu] = diem
#     a = {k: v for k, v in sorted(nguyenlieuvadiem.items(), key=lambda item: item[1],reverse=True)}
#     return list(a.keys())

# # chấm điểm nguyên liệu trên tay (cao càng tệ)
# def listnguyenlieutrentay(board):
#     dictchuaxephang = {}
#     a = {}
#     for nguyenlieu in thetarget(board).stocks.keys():
#         diem = player_01.stocks[nguyenlieu] - thetarget(board).stocks[nguyenlieu]
#         dictchuaxephang[nguyenlieu] = diem
#     a = {k: v for k, v in sorted(dictchuaxephang.items(), key=lambda item: item[1],reverse=True)}
#     return list(a.keys())

# # tìm thẻ để úp
# def theseup(board):
#     diemcaonhat = 0
#     thetarget = None
#     for the in dictthetrenban(board).keys():
#         if dictthetrenban(board)[the] > diemcaonhat:
#             diemcaonhat = dictthetrenban(board)[the]
#             thetarget = the
#     return thetarget

# def moiturn(board):
#     target = thetarget(board)
#     #print("thẻ target:",target.score,"điểm",target.stocks,target.type_stock)
#     #print("những nguyên liệu còn thiếu:",dictnguyenlieuthieu(target))
#     if thelayngay(board) != None:
#         #print("hốt ngay thẻ",thelayngay(board).stocks)
#         return player_01.getCard(thelayngay(board),board)
#     else:
#         if sum(player_01.stocks.values()) >8:
#             if player_01.checkUpsiteDown() == True:
#                 if sum(player_01.stocks.values()) == 9:
#                     bo = {}
#                 if sum(player_01.stocks.values()) == 10:
#                     bo = {listnguyenlieutrentay(board)[0]:1}
#                 #print(209)
#                 return player_01.getUpsideDown(theseup(board),board,bo)
#             else:
#                 if len(listnguyenlieucon(board)) >2:
#                     if sum(player_01.stocks.values()) == 9:
#                         #print(214)
#                         return player_01.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{listnguyenlieuuutien(board)[2]:1,listnguyenlieuuutien(board)[1]:1})
#                     if sum(player_01.stocks.values()) == 10:
#                         #print(217)
#                         #print("lấy 3 nguyên liệu:",listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],"và trả 3 nguyên liệu:",{listnguyenlieutrentay(board)[0]:1,listnguyenlieutrentay(board)[1]:1,listnguyenlieutrentay(board)[2]:1})
#                         return player_01.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{listnguyenlieutrentay(board)[0]:1,listnguyenlieutrentay(board)[1]:1,listnguyenlieutrentay(board)[2]:1})
#                 else:
#                     #print("skip 220")
#                     return board
#         if sum(player_01.stocks.values()) == 8:
#             if len(listnguyenlieucon(board)) >2:
#                 #print(224)
#                 return player_01.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{listnguyenlieuuutien(board)[2]:1})
#             else:
#                 if player_01.checkUpsiteDown() == True:
#                     #print(228)
#                     return player_01.getUpsideDown(theseup(board),board,{})
#                 else:
#                     #print("skip chỗ 1")
#                     return board
#         else:
#             # số thẻ trên tay < 8
#             if player_01.checkOneStock(board,nlcannhat(target)) == True:
#                 #print(236)
#                 return player_01.getOneStock(nlcannhat(target),board,{})
#             else:
#                 if len(listnguyenlieucon(board)) >2:
#                     #print(240)
#                     return player_01.getThreeStocks(listnguyenlieuuutien(board)[0],listnguyenlieuuutien(board)[1],listnguyenlieuuutien(board)[2],board,{})
#                 else:
#                     if player_01.checkUpsiteDown() == True:
#                         #print(244)
#                         return player_01.getUpsideDown(theseup(board),board,{})
#                     else:
#                         #print("skip chỗ 2")
#                         return board