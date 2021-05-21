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
    