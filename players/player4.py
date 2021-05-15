from base import player
import random
import math
player_04 = player.Player("Hieu", 0)


def action(board, arr_player):
    return turn(board, player_04)


def turn(board, player_04):
    thecothelay = []

    if len(player_04.card_upside_down) > 0:
        for the in player_04.card_upside_down:
            if player_04.checkGetCard(the) == True:
                thecothelay.append(the)
    

    for the in board.dict_Card_Stocks_Show["III"]:
        if player_04.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["II"]:
        if player_04.checkGetCard(the) == True:
            thecothelay.append(the)
    for the in board.dict_Card_Stocks_Show["I"]:
        if player_04.checkGetCard(the) == True:
            thecothelay.append(the)
    
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_04.checkOneStock(board, nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    
    #action
    #Lấy thẻ
    if len(thecothelay) > 0:
        list_card_value = []
        for card in thecothelay:
            if card.score > 0:
                card_value = sum(list(card.stocks.values()))/card.score
                list_card_value.append([card, card_value])
        if len(list_card_value) > 0:
            card_get = list_card_value[0][0]
            card_value = list_card_value[0][1]
            for item in list_card_value:
                if item[1] < card_value:
                    card_get = item[0]
                    card_value = item[1]
            return player_04.getCard(card_get, board)
        else:
            for card in thecothelay:
                if card.score == 0:
                    card_value = math.sqrt(sum(list(card.stocks.values())) + 1.78)
                    list_card_value.append([card, card_value])
            card_get = list_card_value[0][0]
            card_value = list_card_value[0][1]
            for item in list_card_value:
                if item[1] < card_value:
                    card_get = item[0]
                    card_value = item[1]
            return player_04.getCard(card_get, board)
    #lấy token
    if sum(player_04.stocks.values()) <= 7:
        dict_token_important = get_important_token(board)
        if len(dict_token_important) > 0:
            for token in list(dict_token_important.keys()):
                if token not in nguyenlieucon:
                    del dict_token_important[token]
            if len(dict_token_important) >= 3:
                return player_04.getThreeStocks(list(dict_token_important.keys())[0],
                                        list(dict_token_important.keys())[1],
                                        list(dict_token_important.keys())[2], board, {})
            elif len(dict_token_important) > 0 and len(nguyenlieucothelay2) > 0:
                type_card = nguyenlieucothelay2[0]
                value = 0
                for typecard in list(dict_token_important.keys()):
                    if dict_token_important[typecard] > value:
                        value = dict_token_important[typecard]
                        type_card = typecard
                return player_04.getOneStock(type_card, board, {})
        else:
            dict_token_choose = get_Three_Most_Token(board)
            for token in list(dict_token_choose.keys()):
                if token not in nguyenlieucon:
                    del dict_token_choose[token]

            if len(dict_token_choose) >= 3:
                return player_04.getThreeStocks(list(dict_token_choose.keys())[0],
                                        list(dict_token_choose.keys())[1],
                                        list(dict_token_choose.keys())[2], board, {})
        

        if len(nguyenlieucothelay2) > 0:
            dict_token_choose = get_Three_Most_Token(board)
            for token in list(dict_token_choose.keys()):
                if token not in nguyenlieucothelay2:
                    del dict_token_choose[token]
            # if len(dict_token_choose)
            if len(dict_token_choose) > 0:
                return player_04.getOneStock(list(dict_token_choose.keys())[0], board, {})    
            

    if sum(player_04.stocks.values()) > 7:
        #nếu có 8 token
        if sum(player_04.stocks.values()) < 9:
            dict_token_important = get_important_token(board)
            if len(dict_token_important) > 0:
                for token in list(dict_token_important.keys()):
                    if token not in nguyenlieucothelay2:
                        del dict_token_important[token]
                if len(dict_token_important) > 0:
                    type_card = nguyenlieucothelay2[0]
                    value = 0
                    for typecard in list(dict_token_important.keys()):
                        if dict_token_important[typecard] > value:
                            value = dict_token_important[typecard]
                            type_card = typecard
                    return player_04.getOneStock(type_card, board,{})
        #nếu có 9 token
        elif sum(player_04.stocks.values()) == 9:
            return player_04.getUpsideDown(get_card_value(board), board, {})
        else:
            bo = {}
            dict_token_important = get_important_token(board)
            list_value = list(dict_token_important.values())
            list_type_token = list(dict_token_important.keys())
            list_token_return = []
            count = 0
            while count < len(dict_token_important):
                count += 1
                min_value = min(list_value)
                list_token_return.append(list_type_token[list_value.index(min_value)])
            
            for nguyenlieu in list_token_return:
                if player_04.stocks[nguyenlieu] > 0:
                    bo[nguyenlieu] = 1
                    break
            return player_04.getUpsideDown(get_card_value(board), board, bo)
    
    return board


def get_Three_Most_Token(board):
    dict_most_token = {}
    dict_most_token['red'] = 0
    dict_most_token['blue'] = 0
    dict_most_token['green'] = 0
    dict_most_token['white'] = 0
    dict_most_token['black'] = 0

    for i in board.dict_Card_Stocks_Show.keys():
        for card in board.dict_Card_Stocks_Show[i]:
            dict_most_token['red'] += card.stocks['red']
            dict_most_token['blue'] += card.stocks['blue']
            dict_most_token['green'] += card.stocks['green']
            dict_most_token['white'] += card.stocks['white']
            dict_most_token['black'] += card.stocks['black']

    list_token = list(dict_most_token.keys())
    list_number_token = list(dict_most_token.values())
    dict_token_choose = {}
    count = 0
    while count < len(list_token):
        count += 1
        # for token in list_token:
        if board.stocks[list_token[list_number_token.index(max(list_number_token))]] > 0:
            dict_token_choose[list_token[list_number_token.index(max(list_number_token))]] = max(list_number_token)
        
        list_token.remove(list_token[list_number_token.index(max(list_number_token))])
        list_number_token.remove(max(list_number_token))

    return dict_token_choose

def get_important_token(board):
    dict_important_token = {}
    dict_important_token['red'] = 0
    dict_important_token['blue'] = 0
    dict_important_token['green'] = 0
    dict_important_token['white'] = 0
    dict_important_token['black'] = 0
    for card in player_04.card_upside_down:
        dict_important_token['red'] += card.stocks['red']
        dict_important_token['blue'] += card.stocks['blue']
        dict_important_token['green'] += card.stocks['green']
        dict_important_token['white'] += card.stocks['white']
        dict_important_token['black'] += card.stocks['black']   
    list_token = list(dict_important_token.keys())
    list_number_token = list(dict_important_token.values())
    dict_token_important = {}
    count = 0
    while count < len(list_token):
        if board.stocks[list_token[list_number_token.index(max(list_number_token))]] > 0:
            dict_token_important[list_token[list_number_token.index(max(list_number_token))]] = max(list_number_token)
        list_token.remove(list_token[list_number_token.index(max(list_number_token))])
        list_number_token.remove(max(list_number_token))

    return dict_important_token
    

def action_Up_The(board):
    if player_04.checkUpsiteDown == False:
        print('Khong lay the duoc')
        return None
    else:
        return player_04.getUpsideDown(get_card_value(board), board, {})


def get_card_value(board):
    dict_card_value = {}
    min = 3
    list_card_process = []
    list_card_get = []
    for type_card in list(board.dict_Card_Stocks_Show.keys()):
        for card in list(board.dict_Card_Stocks_Show[type_card]):
            if card.score == 0:
                list_card_process.append(card)
                sum = 0
                for nguyenlieu in card.stocks.keys():
                    if card.stocks[nguyenlieu]- player_04.stocks[nguyenlieu] > 0:
                        sum += card.stocks[nguyenlieu]- player_04.stocks[nguyenlieu]
                    else:
                        sum += 0
                dict_card_value[card.id] = math.sqrt(sum+1.78)
            else:
                sum = 0
                list_card_process.append(card)
                for nguyenlieu in card.stocks.keys():
                    if card.stocks[nguyenlieu]- player_04.stocks[nguyenlieu] > 0:
                        sum += card.stocks[nguyenlieu]- player_04.stocks[nguyenlieu]
                    else:
                        sum += 0
                dict_card_value[card.id] = sum/card.score
    dict_card_process = {}
    values = list(dict_card_value.values())
    id = list(dict_card_value.values())
    count = 0
    while count < 4:
        count += 1
        list_card_get.append(list_card_process[values.index(max(values))])
        id.remove(id[values.index(max(values))])
        values.remove(max(values))    
    return list_card_get[0]











