

from base import player
import random
player_02 = player.Player("QueenOfGame", 0)
    

#Scan thẻ target trên bàn
def list_target_cards(board):
    target_cards = []
    type = ["III", "II", "I"]
    for i in type:
        for card in board.dict_Card_Stocks_Show[i]:
            if card.score == 5 and sum(card.stocks.values()) == 10:
                target_cards.append(card)
            if card.score == 4 and sum(card.stocks.values()) == 7:
                target_cards.append(card)
            if card.score == 3 and sum(card.stocks.values()) == 6:
                target_cards.append(card)
            if card.score == 2 and sum(card.stocks.values()) == 2:
                target_cards.append(card)
            if card.score == 1 and sum(card.stocks.values()) == 4:
                target_cards.append(card)
    target_cards_rank = []
    score = [3, 5, 4, 3, 2, 1]

    for i in score:
        for card in target_cards:
            if card.score == i:
                if card.score == 5:
                    if check_any_card_5score_onhand() == False:
                        target_cards_rank.append(card)
                    else:
                        continue
                if card.score == 4:
                    if check_any_card_4score_onhand() == False:
                        target_cards_rank.append(card)
                    else:
                        continue
                if card.score == 3:
                    if check_any_card_3score_onhand() == False:
                        target_cards_rank.append(card)
                    else:
                        continue
                target_cards_rank.append(card)
    target_cards_rank_upgrade = []
    if len(player_02.card_upside_down) > 0:
        for item in player_02.card_upside_down:
            for card in target_cards_rank:
                if card.stocks[item.type_stock] > 0:
                    target_cards_rank_upgrade.append(card)
                if item.stocks[card.type_stock] > 0:
                    target_cards_rank_upgrade.append(card)
    else:
        target_cards_rank_upgrade = target_cards_rank.copy()
    return target_cards_rank_upgrade





#Sắp xếp thứ tự ưu tiên các màu token muốn lấy cho thẻ target trên bàn
def list_color_on_board(board):
    dict_start = {"red" : 0, "white": 0, "blue": 0, "green": 0,"black": 0}
    
    type = ["III", "II"]
    for i in type:
        for card in board.dict_Card_Stocks_Show[i]:
            if card in list_target_cards(board):
                for color in dict_start.keys():
                    dict_start[color] += card.stocks[color]
    list_color = []
    sort_list = sorted(list(dict_start.values()), reverse=True)
    for value in sort_list:
        for color in list(dict_start.keys()):
            if dict_start[color] == value:
                if color not in list_color:
                    list_color.append(color)
    list_color_onboard = []
    for color in list_color:
        if board.stocks[color] > 0:
            list_color_onboard.append(color)
    # ###print(dict_start)
    # ###print(sort_list)
    # ##print(list_color_onboard)
    return list_color_onboard


#Sắp xếp thứ tự ưu tiên các thẻ đang úp
def list_holding_cards():
    A = []
    if len(player_02.card_upside_down) > 0:
        #Xét nếu có thẻ mà có màu giúp support mở thẻ khác --> ưu tiên thẻ đó trước
        for item in player_02.card_upside_down:
            holding_cards = player_02.card_upside_down.copy()  
            holding_cards.remove(item)
            for card in holding_cards:
                if card.stocks[item.type_stock] > 0:
                    A.append(item)
        # if len(A) > 0:
            # ##print(77)    
            # ##print(A[0].type_stock)
        score = [3, 5, 4, 2, 1]
        for i in score:
            for item in player_02.card_upside_down:
                if item.score == i:
                    A.append(item)
    return A

#Sắp xếp màu nguyên liệu ưu tiên cho thẻ đang úp
def list_color_for_holdings(board):
    list_color_holding = []
    dict_start = {"red" : 0, "white": 0, "blue": 0, "green": 0,"black": 0}
    item = None
    #Màu nguyên liệu ưu tiên cho thẻ úp ưu tiên nhất    
    if len(player_02.card_upside_down) > 0:
        # ##print(98)
        # ##print(list_holding_cards()[0].type_stock)
        item = list_holding_cards()[0]
        a = 0
        for color in list(item.stocks.keys()):
            if ( item.stocks[color] - player_02.stocks[color] - player_02.stocks_const[color] ) > a:
                if board.stocks[color] > 0: 
                    a = item.stocks[color] - player_02.stocks[color] - player_02.stocks_const[color]
                    if len(list_color_holding) > 0:                    
                        list_color_holding.insert(0,color)
                    else:
                        list_color_holding.append(color)
            if item.stocks[color] > 0:
                if board.stocks[color] > 0:
                    if color not in list_color_holding:
                        list_color_holding.append(color)
        # ##print(list_color_holding)
        #Màu nguyên liệu ưu tiên cho thẻ các thẻ úp khác
        if len(player_02.card_upside_down) > 1:
            # ##print(117)
            # ##print(list_holding_cards()[1].type_stock)
            list_cards = list_holding_cards().copy()
            list_cards.pop(0)
            for card in list_cards:
                for color in card.stocks.keys():
                    dict_start[color] += card.stocks[color] 
            # ##print(dict_start)
            for color in dict_start.keys():
                dict_start[color] -= ( player_02.stocks[color] + player_02.stocks_const[color] )
            # ##print(dict_start)
            list_values = sorted(list(dict_start.values()),reverse=True)
            # ##print(list_values)
            for value in list_values:
                for color in dict_start.keys():
                    if dict_start[color] == value:
                        if value > 0:
                            if board.stocks[color] > 0:
                                if color not in list_color_holding:
                                    list_color_holding.append(color)
    # ##print(list_color_holding)
    return list_color_holding

#Tìm ra màu token thứ 3 nếu trong thẻ đang úp chỉ còn 2 loại token cần lấy
def color_3(board):
    color3 = None
    if len(list_color_for_holdings(board)) == 2:
        for color in board.stocks.keys():
            if board.stocks[color] > 0 and color not in list_color_for_holdings(board):
                if color != "auto_color":
                    color3 = color
    return color3

#Tìm ra màu token thứ 3 nếu trong list màu target chỉ có 2
def color_3_on_board(board):
    color3 = None
    if len(list_color_on_board(board)) == 2:
        for color in board.stocks.keys():
            if board.stocks[color] > 0 and color not in list_color_on_board(board):
                if color != "auto_color":
                    color3 = color
    return color3

#Thứ tự các màu token muốn lấy, trong trường hợp k có thẻ úp và k có thẻ target 
def list_color_no_target(board):
    color_no_target = []
    dict_start = {"red" : 0, "white": 0, "blue": 0, "green": 0,"black": 0}
    type = ["III", "II", "I"]
    for i in type:
        for card in board.dict_Card_Stocks_Show[i]:
            for color in card.stocks.keys():
                dict_start[color] += card.stocks[color]
    list_value = sorted(list(dict_start.values()),reverse=True)
    for value in list_value:
        for color in dict_start.keys():
            if dict_start[color] == value:
                if board.stocks[color] > 0:
                    if color not in color_no_target:
                        if color not in list_color_for_holdings(board):
                            color_no_target.append(color)
    return color_no_target

#token_important
def list_token_can_get(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon

#get_important_token của Hiếu
def get_important_token(board):
    token_can_get = list_token_can_get(board)
    dict_important_token = {}
    dict_important_token['red'] = 0
    dict_important_token['blue'] = 0
    dict_important_token['green'] = 0
    dict_important_token['white'] = 0
    dict_important_token['black'] = 0
    for card in player_02.card_upside_down:
        dict_important_token['red'] += card.stocks['red'] - player_02.stocks_const['red'] - player_02.stocks['red']
        dict_important_token['blue'] += card.stocks['blue'] - player_02.stocks_const['blue'] - player_02.stocks['blue']
        dict_important_token['green'] += card.stocks['green'] - player_02.stocks_const['green'] - player_02.stocks['green']
        dict_important_token['white'] += card.stocks['white'] - player_02.stocks_const['white'] - player_02.stocks['white']
        dict_important_token['black'] += card.stocks['black'] - player_02.stocks_const['black'] - player_02.stocks['black']
    list_token = list(dict_important_token.keys())
    list_number_token = list(dict_important_token.values())
    dict_token_important = {}
    count = 0
    while count < len(list_token):
        if list_token[list_number_token.index(max(list_number_token))] in token_can_get:
            dict_token_important[list_token[list_number_token.index(max(list_number_token))]] = max(list_number_token)
        list_token.remove(list_token[list_number_token.index(max(list_number_token))])
        list_number_token.remove(max(list_number_token))
    {k: v for k, v in sorted(dict_token_important.items(), key=lambda item: item[1],reverse=True)}
    return list(dict_token_important.keys())

#List màu token đang cầm, ưu tiên bỏ trước, trong trường hợp đang có thẻ úp
def list_color_return_when_holding(board):
    color_return = []
    for color in player_02.stocks.keys():
        if player_02.stocks[color] > 0 and color != "auto_color":
            if color not in list_color_for_holdings(board):
                color_return.append(color)
    list = list_color_for_holdings(board).copy()
    list.reverse()
    for color in list:
        if player_02.stocks[color] > 0 and color not in color_return:
            color_return.append(color)
    return color_return

    
    

#Dict return khi có thẻ úp
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
    danhsachcon = list_color_return_when_holding(board).copy()
    
    if sum(dict_bd.values()) > 10:
        ###print(261)
        n = sum(dict_bd.values()) - 10
        i = 0
        while n != 0:
            ###print(266)
            if dict_bd[danhsachcon[i]] != 0:
                ###print(268)
                dict_bo[danhsachcon[i]] +=1
                dict_bd[danhsachcon[i]] -=1
                n -= 1
            else:
                i += 1
    return dict_bo

#Dict return_when_no_target
def dict_return(board,*args):
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
    color_list = list_color_no_target(board).copy()
    color_list.reverse()
    if sum(dict_bd.values()) > 10:
        ###print(261)
        n = sum(dict_bd.values()) - 10
        i = 0
        while n != 0:
            ###print(266)
            if dict_bd[color_list[i]] != 0:
                ###print(268)
                dict_bo[color_list[i]] +=1
                dict_bd[color_list[i]] -=1
                n -= 1
            else:
                i += 1
    return dict_bo

#Các thẻ trong bộ có thể mua
def list_cards_target_can_buy(board):
    cards_target_can_buy = []
    for card in list_holding_cards():
        if player_02.checkGetCard(card):
            cards_target_can_buy.append(card)
    for card in list_target_cards(board):
        if player_02.checkGetCard(card):
            cards_target_can_buy.append(card)
    if target_support_cards(board) != None:
        if player_02.checkGetCard(card):
            cards_target_can_buy.append(card)
    return cards_target_can_buy

#Các thẻ bất kì trên bàn có thể mua
def list_cards_on_board_can_buy(board):
    cards_on_board_can_buy = []
    type = ["III", "II", "I"]
    for i in type:
        for card in board.dict_Card_Stocks_Show[i]:
            if player_02.checkGetCard(card):
                cards_on_board_can_buy.append(card)
    return cards_on_board_can_buy

#Kiểm tra xem trong thẻ úp hoặc thẻ trên tay đã có thẻ 5 điểm chưa
def check_any_card_5score_onhand():
    for card in player_02.card_upside_down:
        if card.score == 5:
            return True
    for card in player_02.card_open:
        if card.score == 5:
            return True
    return False

#Kiểm tra xem trong thẻ úp hoặc thẻ trên tay đã có thẻ 4 điểm chưa
def check_any_card_4score_onhand():
    for card in player_02.card_upside_down:
        if card.score == 4:
            return True
    for card in player_02.card_open:
        if card.score == 4:
            return True
    return False

#Kiểm tra xem trong thẻ úp hoặc thẻ trên tay đã có thẻ 3 điểm chưa
def check_any_card_3score_onhand():
    for card in player_02.card_upside_down:
        if card.score == 3:
            return True
    for card in player_02.card_open:
        if card.score == 3:
            return True
    return False

#Hàm úp thẻ chị Trang
def theup(board):
    NL = []
    for nguyenlieu in board.dict_Card_Stocks_Show["III"][0].stocks.keys():
        max = 0
        for the in player_02.card_upside_down:
            if the.stocks[nguyenlieu] > max:
                the.stocks[nguyenlieu] = max
        if max > player_02.stocks[nguyenlieu]:
            NL.append(nguyenlieu)
    for n in NL:
        for the1 in board.dict_Card_Stocks_Show["III"]:
            if the1.type_stock == n:
                return the1


#Tìm ra thẻ support cho thẻ đang úp
def target_support_cards(board):
    target_support_cards = []
    cardx = None
    type = ["II", "I"]
    if len(list_color_for_holdings(board)) > 0:
        for color in list_color_for_holdings(board):
            for i in type:
                for card in board.dict_Card_Stocks_Show[i]:
                    if card.type_stock == color:
                        target_support_cards.append(card)
    valuation = 0
    for card in target_support_cards:
        if card.score / sum(card.stocks.values()) > valuation:
            valuation = card.score / sum(card.stocks.values())
            cardx = card
    return cardx

#Màu token cần lấy cho thẻ suppport
def color_card_support(board):
    dict = {}
    color_support = []
    if target_support_cards(board) != None:
        dict = target_support_cards(board).stocks.copy()
        list_values = sorted(list(dict.values()),reverse=True)
        for value in list_values:
            for color in dict.keys():
                if dict[color] == value:
                    if value > 0:
                        if board.stocks[color] > 0:
                            color_support.append(color)
    return color_support

#color3_support
def color_3_support(board):
    color3_support = None
    for color in board.stocks.keys():
        if board.stocks[color] > 0:
            if color not in color_card_support(board):
                color3_support = color
    return color3_support


#Code hành động chính
def action(board, arr_player):

    if len(list_cards_target_can_buy(board)) > 0:
        return player_02.getCard(list_cards_target_can_buy(board)[0],board)
    
    if len(list_target_cards(board)) > 0:
        if player_02.checkUpsiteDown():                            
            ##print(431)
            ##print(list_target_cards(board)[0].type_stock)
            return player_02.getUpsideDown(list_target_cards(board)[0],board, Luachonbothe(board,"auto_color"))

    if len(player_02.card_upside_down) > 0:
        if sum(player_02.stocks.values()) <= 8:            
            if len(list_color_for_holdings(board)) > 0:
                if player_02.checkOneStock(board,list_color_for_holdings(board)[0]):
                    ##print(439)
                    ##print(list_color_for_holdings(board))
                    return player_02.getOneStock(list_color_for_holdings(board)[0],board,Luachonbothe(board,list_color_for_holdings(board)[0],list_color_for_holdings(board)[0]))
            
            if len(list_color_for_holdings(board)) > 2:
                if player_02.checkThreeStocks(board,list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],list_color_for_holdings(board)[2]):
                    ##print(445)
                    ##print(list_color_for_holdings(board))
                    return player_02.getThreeStocks(list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],list_color_for_holdings(board)[2],
                                                    board,
                                                    Luachonbothe(board,list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],list_color_for_holdings(board)[2]))
            if len(list_color_for_holdings(board)) == 2 :               
                if player_02.checkOneStock(board,list_color_for_holdings(board)[1]):
                    ##print(452)
                    ##print(list_color_for_holdings(board)[1])
                    return player_02.getOneStock(list_color_for_holdings(board)[1],board,Luachonbothe(board,list_color_for_holdings(board)[1],list_color_for_holdings(board)[1]))
                if color_3(board) != None:
                    ##print(455)
                    ##print(list_color_for_holdings(board))
                    ##print(color_3(board))
                    ##print(board.stocks)
                    return player_02.getThreeStocks(list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3(board),
                                                    board,
                                                    Luachonbothe(board,
                                                    list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3(board)))
                                            
            if len(list_color_for_holdings(board)) == 1 :
                if len(list_color_no_target(board)) >= 2:
                    if player_02.checkThreeStocks(board,list_color_for_holdings(board)[0],list_color_no_target(board)[0],list_color_no_target(board)[1]):
                        ##print(467)
                        ##print(list_color_for_holdings(board)[0])
                        ##print(list_color_no_target(board))                        
                        return player_02.getThreeStocks(list_color_for_holdings(board)[0],list_color_no_target(board)[0],list_color_no_target(board)[1],
                                                    board,
                                                    Luachonbothe(board,list_color_for_holdings(board)[0],list_color_no_target(board)[0],list_color_no_target(board)[1]))
                if target_support_cards(board) != None:
                    if len(color_card_support(board)) > 2:
                        ##print(475)
                        ##print(color_card_support(board)[0],color_card_support(board)[1],color_card_support(board)[2])
                        if player_02.checkThreeStocks(board,color_card_support(board)[0],color_card_support(board)[1],color_card_support(board)[2]):
                            return player_02.getThreeStocks(color_card_support(board)[0],color_card_support(board)[1],color_card_support(board)[2],board,
                                                        Luachonbothe(board,color_card_support(board)[0],color_card_support(board)[1],color_card_support(board)[2]))                                            
                    for color in color_card_support(board):
                        if player_02.checkOneStock(board,color):
                            ##print(482)
                            ##print(color)
                            return player_02.getOneStock(color,board,Luachonbothe(board,color,color))
                    if len(color_card_support(board)) == 2:
                        if color_3_support(board) != None:
                            ##print(487)
                            if player_02.checkThreeStocks(board,color_card_support(board)[0],color_card_support(board)[1],color_3_support(board)):
                                return player_02.getThreeStocks(color_card_support(board)[0],color_card_support(board)[1],color_3_support(board),board,
                                                                Luachonbothe(board,color_card_support(board)[0],color_card_support(board)[1],color_3_support(board)))
                        for color in color_card_support(board):
                            if player_02.checkOneStock(board,color):
                                ##print(493)
                                ##print(color)
                                return player_02.getOneStock(color,board,Luachonbothe(board,color,color))                
                    if player_02.checkUpsiteDown():
                        ##print(497)
                        ##print(target_support_cards(board).type_stock)
                        return player_02.getUpsideDown(target_support_cards(board),board,{})
                if theup(board) != None:
                    if player_02.checkUpsiteDown():
                        ##print(502)
                        ##print(theup(board).type_stock)                    
                        return player_02.getUpsideDown(theup(board),board,Luachonbothe(board,"auto_color"))
                if target_support_cards(board) != None:
                    if player_02.checkGetCard(target_support_cards(board)):
                        ##print(507)
                        ##print(target_support_cards(board)).type_stock
                        return player_02.getCard(target_support_cards(board),board)
                if theup(board) != None:                
                    if player_02.checkGetCard(theup(board)):
                        ##print(512)
                        ##print(theup(board).type_stock)
                        return player_02.getCard(theup(board),board)
                if len(list_color_no_target(board)) >= 3:
                    if player_02.checkThreeStocks(board,list_color_no_target(board)[0],list_color_no_target(board)[1],list_color_no_target(board)[2]):
                        ##print(517)
                        ##print(list_color_no_target(board)[0],list_color_no_target(board)[1],list_color_no_target(board)[2])
                        return player_02.getThreeStocks(list_color_no_target(board)[0],list_color_no_target(board)[1],list_color_no_target(board)[2],
                                                        board,
                                                        Luachonbothe(board,list_color_no_target(board)[0],list_color_no_target(board)[1],list_color_no_target(board)[2]))
                if len(list_color_no_target(board)) > 0:
                    for color in list_color_no_target(board):
                        if player_02.checkOneStock(board,color):
                            ##print(525)
                            ##print(color)
                            return player_02.getOneStock(color,board,{})            

        if sum(player_02.stocks.values()) == 9:
            for color in list_color_for_holdings(board):
                if player_02.checkOneStock(board,color):
                    ##print(532)
                    ##print(color)
                    return player_02.getOneStock(color,board,Luachonbothe(board,color,color))
            if player_02.checkUpsiteDown():
                if len(list_target_cards(board)) > 0:
                    ##print(537)
                    return player_02.getUpsideDown(list_target_cards(board)[0],board, Luachonbothe(board,"auto_color"))
                if target_support_cards(board) != None:
                    ##print(540)
                    return player_02.getUpsideDown(target_support_cards(board),board,{})
                if theup(board) != None:
                    ##print(543)
                    return player_02.getUpsideDown(theup(board),board,Luachonbothe(board,"auto_color"))                                 
            if len(list_color_for_holdings(board)) == 2:
                if color_3_on_board(board) != None:
                    ##print(547)
                    ##print(list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board))
                    return player_02.getThreeStocks(list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board),
                                                board,
                                                Luachonbothe(board,list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board)))        
            if target_support_cards(board) != None:
                if player_02.checkGetCard(target_support_cards(board)):
                    ##print(554)
                    ##print(target_support_cards(board).type_stock)
                    return player_02.getCard(target_support_cards(board),board)
            if theup(board) != None:
                if player_02.checkGetCard(theup(board)):
                    ##print(559)
                    ##print(theup(board).type_stock)
                    return player_02.getCard(theup(board),board)
        if sum(player_02.stocks.values()) == 10:
            if target_support_cards(board) != None:
                if player_02.checkUpsiteDown():
                    ##print(566)
                    ##print(target_support_cards(board).type_stock)
                    return player_02.getUpsideDown(target_support_cards(board),board,Luachonbothe(board,"auto_color"))
            if theup(board) != None:
                if player_02.checkUpsiteDown():
                    ##print(568)
                    ##print(theup(board).type_stock)
                    return player_02.getUpsideDown(theup(board),board,Luachonbothe(board,"auto_color"))            
            if target_support_cards(board) != None:
                if player_02.checkGetCard(target_support_cards(board)):
                    ##print(573)
                    ##print(target_support_cards(board).type_stock)
                    return player_02.getCard(target_support_cards(board),board)
            if theup(board) != None:
                if player_02.checkGetCard(theup(board)):
                    ##print(578)
                    ##print(theup(board).type_stock)
                    return player_02.getCard(theup(board),board)
            if len(list_color_for_holdings(board)) > 0:
                for color in list_color_for_holdings(board):
                    if player_02.checkOneStock(board,color):
                        ##print(477)
                        ##print(color)
                        return player_02.getOneStock(color,board,Luachonbothe(board,color,color))
            if len(list_color_for_holdings(board)) == 2:
                if color_3_on_board(board) != None:
                    if player_02.checkThreeStocks(board,list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board)):
                        ##print(589)
                        ##print(list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board))                    
                        return player_02.getThreeStocks(list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board),
                                                    board,
                                                    Luachonbothe(board,list_color_for_holdings(board)[0],list_color_for_holdings(board)[1],color_3_on_board(board)))                      
        
        if len(list_cards_on_board_can_buy(board)) > 0:
            for card in list_cards_on_board_can_buy(board):
                if card.score > 0:
                    if player_02.checkGetCard(list_cards_on_board_can_buy(board)[0]):
                        ##print(589)
                        ##print(card.type_stock)
                        return player_02.getCard(card,board)
            for card in list_cards_on_board_can_buy(board):
                if player_02.checkGetCard(card):
                    ##print(602)
                    ##print(card.type_stock)
                    return player_02.getCard(card,board)
        if len(list_color_on_board(board)) > 0:
            for color in list_color_on_board(board):
                if player_02.checkOneStock(board, color):
                    ##print(609)
                    ##print(color)
                    return player_02.getOneStock(color,board,Luachonbothe(board,color,color))
            if len(list_color_on_board(board)) > 2:
                if player_02.checkThreeStocks(board,list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2]):
                    ##print(615)
                    ##print(list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2])
                    return player_02.getThreeStocks(list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2],
                                                    board,
                                                    Luachonbothe(board,
                                                    list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2]))

    if len(player_02.card_upside_down) == 0:

        if len(list_color_on_board(board)) > 0:
            for color in list_color_on_board(board):
                if player_02.checkOneStock(board, color):
                    ##print(241)
                    return player_02.getOneStock(color,board,dict_return(board,color,color))
            if len(list_color_on_board(board)) > 2:
                ##print(243)
                if player_02.checkThreeStocks(board,list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2]):
                    return player_02.getThreeStocks(list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2],
                                                    board,
                                                    dict_return(board,
                                                    list_color_on_board(board)[0],list_color_on_board(board)[1],list_color_on_board(board)[2]))
            if len(list_color_on_board(board)) == 2:
                if color_3(board) != None:
                    ##print(251)
                    return player_02.getThreeStocks(list_color_on_board(board)[0],list_color_on_board(board)[1],color_3_on_board(board),
                                                    board,
                                                    dict_return(board,
                                                    list_color_on_board(board)[0],list_color_on_board(board)[1],color_3_on_board(board)))      

        if sum(player_02.stocks.values()) <= 8:
            for color in list_color_no_target(board):
                if player_02.checkOneStock(board,color):
                    ##print(317)
                    return player_02.getOneStock(color,board,{})
            if len(list_color_no_target(board)) >= 3:
                ##print(320)
                return player_02.getThreeStocks(list_color_no_target(board)[0],list_color_no_target(board)[1],list_color_no_target(board)[2],
                                                board,
                                                dict_return(board,list_color_no_target(board)[0],list_color_no_target(board)[1],list_color_no_target(board)[2]))
        
        if sum(player_02.stocks.values()) == 9:
            for color in list_color_no_target(board):
                if player_02.checkOneStock(board,color):
                    ##print(328)
                    return player_02.getOneStock(color,board,dict_return(board,color,color))
    
    if theup(board) != None:
        if player_02.checkGetCard(theup(board)):
            return player_02.getCard(theup(board),board)
    
    if len(list_cards_on_board_can_buy(board)) > 0:
        for card in list_cards_on_board_can_buy(board):
            if card.score > 0:
                return player_02.getCard(card,board)
        return player_02.getCard(card,board)
    # ##print(board.stocks)
    return board    


        

        
    





                
                    



        

                
                    










