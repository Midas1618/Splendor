from base import player
import random
import math
player_01 = player.Player("KING", 0)


def action(board, arr_player):
    # return player_01.getOneTwoStock("red","blue",board,{})
    return turn(board, player_01)

def turn(board, player_01):
    thecothelay = listthecothemua(board)    
    nguyenlieucothelay2 = listnguyenlieulay2(board)
    nguyenlieucon = listnguyenlieucon(board)    
    #action

    #Lấy thẻ
    if len(thecothelay) > 0:
        list_card_value = []
        for card in thecothelay:
            #lấy thẻ có điểm
            if card.score > 1:
                card_value = sum(list(card.stocks.values()))/card.score
                list_card_value.append([card, card_value])
        if len(list_card_value) > 0:
            card_get = list_card_value[0][0]
            card_value = list_card_value[0][1]
            for item in list_card_value:
                if item[1] < card_value:
                    card_get = item[0]
                    card_value = item[1]
            return player_01.getCard(card_get, board)
        else:
            #lấy thẻ để lấy noble
            thecothelay = get_card_to_get_noble(board)
            if thecothelay != None:
                for card in thecothelay:
                    if card.score == 0:
                        card_value = math.sqrt(sum(list(card.stocks.values())) + 1.78)
                        list_card_value.append([card, card_value])
                    elif card.score > 0:
                        card_value = sum(list(card.stocks.values()))/card.score
                        list_card_value.append([card, card_value])
                # if len(list_card_value) > 0:
                card_get = list_card_value[0][0]
                card_value = list_card_value[0][1]
                for item in list_card_value:
                    if item[1] < card_value:
                        card_get = item[0]
                        card_value = item[1]
                
                return player_01.getCard(card_get, board)
            else:
                #lấy thẻ rẻ nhất còn lại
                thecothelay = listthecothemua(board)
                for card in thecothelay:
                    if card.score == 0:
                        card_value = math.sqrt(sum(list(card.stocks.values())) + 1.78)
                        list_card_value.append([card, card_value])
                    else:
                        card_value = sum(list(card.stocks.values()))/card.score
                        list_card_value.append([card, card_value])
                card_get = list_card_value[0][0]
                card_value = list_card_value[0][1]
                for item in list_card_value:
                    if item[1] < card_value:
                        card_get = item[0]
                        card_value = item[1]
                return player_01.getCard(card_get, board)
      
    # không lấy được thẻ thì lấy token
    if sum(list(player_01.stocks.values())) <= 7:
        dict_token_important = get_important_token(board)
        # if len(dict_token_important) > 0:
            # for token in list(dict_token_important.keys()):
            #     if token not in nguyenlieucon:
            #         del dict_token_important[token]
        if len(dict_token_important) >= 3:
            return player_01.getThreeStocks(list(dict_token_important.keys())[0],
                                    list(dict_token_important.keys())[1],
                                    list(dict_token_important.keys())[2], board, {})
        elif len(dict_token_important) > 0 and len(nguyenlieucothelay2) > 0:

            for token in list(dict_token_important.keys()):
                if token not in nguyenlieucothelay2:
                    del dict_token_important[token]
            type_card = list(dict_token_important.keys())[0]
            value = list(dict_token_important.values())[0]
            for typecard in list(dict_token_important.keys()):
                # if dict_token_important[typecard] > value:
                #     value = dict_token_important[typecard]
                #     type_card = typecard
                if player_01.checkOneStock(board, typecard) == True:
                    # print('sai1')
                    return player_01.getOneStock(type_card, board, {})
        else:
            dict_token_choose = get_Three_Most_Token(board)
            for token in list(dict_token_choose.keys()):
                if token not in nguyenlieucon:
                    del dict_token_choose[token]

            if len(dict_token_choose) >= 3:
                return player_01.getThreeStocks(list(dict_token_choose.keys())[0],
                                        list(dict_token_choose.keys())[1],
                                        list(dict_token_choose.keys())[2], board, {})
            else:
                if len(nguyenlieucothelay2) > 0:
                    dict_token_choose = get_Three_Most_Token(board)
                    for token in list(dict_token_choose.keys()):
                        if token not in nguyenlieucothelay2:
                            del dict_token_choose[token]
                    # if len(dict_token_choose)
                    if len(dict_token_choose) > 0:
                        print('sai2')
                        return player_01.getOneStock(list(dict_token_choose.keys())[0], board, {})    
                    else:
                        if player_01.checkUpsiteDown() == True:
                            return player_01.getUpsideDown(get_card_value(board), board, {})

    if sum(player_01.stocks.values()) > 7:
        #nếu có 8 token
        if sum(player_01.stocks.values()) < 9:
            dict_token_important = get_important_token(board)
            if len(dict_token_important) > 0:
                for token in list(dict_token_important.keys()):
                    if token not in nguyenlieucothelay2:
                        del dict_token_important[token]
            if len(dict_token_important) > 0:
                type_card = list(dict_token_important.keys())[0]
                value = list(dict_token_important.values())[0]
                for typecard in list(dict_token_important.keys()):
                    if player_01.checkOneStock(board, type_card) == True:
                        return player_01.getOneStock(type_card, board,{})
            #nếu ko lấy được 2token cùng loại thì sẽ auto úp thẻ
            if player_01.checkUpsiteDown() == True: 
                return player_01.getUpsideDown(get_card_value(board), board, {})
        #nếu có 9 token
        elif sum(player_01.stocks.values()) == 9:
            if player_01.checkUpsiteDown() == True: 
                return player_01.getUpsideDown(get_card_value(board), board, {})
        else:
            bo = {}
            dict_token_not_important = get_token_return(board)
            list_value = list(dict_token_not_important.values())
            list_type_token = list(dict_token_not_important.keys())
            list_token_return = []
            count = 0
            while count < len(dict_token_not_important):
                count += 1
                min_value = min(list_value)
                list_token_return.append(list_type_token[list_value.index(min_value)])
            
            for nguyenlieu in list_token_return:
                if player_01.stocks[nguyenlieu] > 0:
                    bo[nguyenlieu] = 1
                    break
            if player_01.checkUpsiteDown() == True: 
                return player_01.getUpsideDown(get_card_value(board), board, bo)
    return board

def get_Three_Most_Token(board):
    token_can_get = list_token_can_get(board)
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
        if list_token[list_number_token.index(max(list_number_token))] in token_can_get:
            dict_token_choose[list_token[list_number_token.index(max(list_number_token))]] = max(list_number_token)
        
        list_token.remove(list_token[list_number_token.index(max(list_number_token))])
        list_number_token.remove(max(list_number_token))
    return dict_token_choose

def get_token_return(board):
    token_can_return = player_01.stocks
    dict_important_token = {}
    dict_important_token['red'] = 0
    dict_important_token['blue'] = 0
    dict_important_token['green'] = 0
    dict_important_token['white'] = 0
    dict_important_token['black'] = 0
    for card in player_01.card_upside_down:
        dict_important_token['red'] += card.stocks['red'] - player_01.stocks_const['red'] - player_01.stocks['red']
        dict_important_token['blue'] += card.stocks['blue'] - player_01.stocks_const['blue'] - player_01.stocks['blue']
        dict_important_token['green'] += card.stocks['green'] - player_01.stocks_const['green'] - player_01.stocks['green']
        dict_important_token['white'] += card.stocks['white'] - player_01.stocks_const['white'] - player_01.stocks['white']
        dict_important_token['black'] += card.stocks['black'] - player_01.stocks_const['black'] - player_01.stocks['black']
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

def get_important_token(board):
    token_can_get = list_token_can_get(board)
    dict_important_token = {}
    dict_important_token['red'] = 0
    dict_important_token['blue'] = 0
    dict_important_token['green'] = 0
    dict_important_token['white'] = 0
    dict_important_token['black'] = 0
    for card in player_01.card_upside_down:
        dict_important_token['red'] += card.stocks['red'] - player_01.stocks_const['red'] - player_01.stocks['red']
        dict_important_token['blue'] += card.stocks['blue'] - player_01.stocks_const['blue'] - player_01.stocks['blue']
        dict_important_token['green'] += card.stocks['green'] - player_01.stocks_const['green'] - player_01.stocks['green']
        dict_important_token['white'] += card.stocks['white'] - player_01.stocks_const['white'] - player_01.stocks['white']
        dict_important_token['black'] += card.stocks['black'] - player_01.stocks_const['black'] - player_01.stocks['black']
    list_token = list(dict_important_token.keys())
    list_number_token = list(dict_important_token.values())
    dict_token_important = {}
    count = 0
    while count < len(list_token):
        if list_token[list_number_token.index(max(list_number_token))] in token_can_get:
            dict_token_important[list_token[list_number_token.index(max(list_number_token))]] = max(list_number_token)
        list_token.remove(list_token[list_number_token.index(max(list_number_token))])
        list_number_token.remove(max(list_number_token))
    return dict_token_important
    
def get_card_to_get_noble(board):
    dict_important_card = {}
    dict_important_card['red'] = 0
    dict_important_card['blue'] = 0
    dict_important_card['green'] = 0
    dict_important_card['white'] = 0
    dict_important_card['black'] = 0
    dict_card_value = {}
    thecothelay = listthecothemua(board)
    target_noble = []
    #tính xem với các thẻ noble thì cần mua thêm bao nhiêu thẻ các loại để lấy được thẻ noble
    for card in board.dict_Card_Stocks_UpsiteDown['Noble']:
        dict_card_to_get = {}
        for type_card in card.stocks.keys():
            dict_card_to_get[type_card] = max(card.stocks[type_card] - player_01.stocks_const[type_card], 0)
        if sum(list(dict_card_to_get.values())) > 2:
            continue
        else:
            dict_card_value[card] = dict_card_to_get
            target_noble.append(sum(list(dict_card_to_get.values())))
    #chỉ hướng đến các thẻ noble còn thiếu dưới 3 thẻ
    list_card_noble = list(dict_card_value.keys())
    noble_should_get = []
    while len(target_noble) > 0:
        index_card = target_noble.index(min(target_noble))
        noble_should_get.append(list_card_noble[index_card])
        target_noble.remove(min(target_noble))
        list_card_noble.remove(list_card_noble[index_card])
    if len(noble_should_get) > 0:
        list_card_should_get = []
        for the in thecothelay:
            if the.type_stock in list(dict_card_value[noble_should_get[0]].keys()):
                list_card_should_get.append(the)

        return list_card_should_get

def get_card_value(board):
    dict_card_value = {}
    list_card_process = []
    list_card_get = []
    list_type_card = ['III', 'II', 'I']
    for type_card in list_type_card:
        for card in list(board.dict_Card_Stocks_Show[type_card]):
            if card.score == 0:
                list_card_process.append(card)
                sum = 1
                for token in list(card.stocks.keys()):
                    if card.stocks[token] - player_01.stocks[token] - player_01.stocks_const[token]  > 0:
                        sum += card.stocks[token] - player_01.stocks[token] - player_01.stocks_const[token]
                    else:
                        sum += 0
                dict_card_value[card.id] = math.sqrt(sum+3)
            else:
                sum = 1
                list_card_process.append(card)
                for token in card.stocks.keys():
                    if card.stocks[token] - player_01.stocks[token] - player_01.stocks_const[token] > 0:
                        sum += card.stocks[token]- player_01.stocks[token] - player_01.stocks_const[token]
                    else:
                        sum += 0
                dict_card_value[card] = sum/card.score
    dict_card_process = {}
    values = list(dict_card_value.values())
    count = 0
    list_card = list_card_process
    while count < len(list_card_process):
        count += 1
        list_card_get.append(list_card_process[values.index(min(values))])
        list_card.remove(list_card[values.index(min(values))])
        values.remove(max(values))    
    return list_card_get[0]

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

def listnguyenlieulay2(board):
    nguyenlieucothelay2 = []
    for nguyenlieu in board.stocks.keys():
        if nguyenlieu != "auto_color" and player_01.checkOneStock(board,nguyenlieu) == True:
            nguyenlieucothelay2.append(nguyenlieu)
    return nguyenlieucothelay2

def listnguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon

def target_noble_card(board, player_01):
    list_noble_card = board.dict_Card_Stocks_Show['Noble']
    dict_card_value = {}
    for card in list_noble_card:
        dict_thieu = {}
        for type_card in card.stocks.keys():
            if player_01.stocks_const[type_card] > card.stocks.keys():
                dict_thieu[type_card] = 0
            else:
                dict_thieu[type_card] = card.stocks.keys() - player_01.stocks_const[type_card]
        dict_card_value[card] = sum(list(dict_thieu.values()))

def virtual_player(board, player_01):
    player_virtual = player_01
    thecothelay = listthecothemua(board)    
    nguyenlieucothelay2 = listnguyenlieulay2(board)
    nguyenlieucon = listnguyenlieucon(board)     

#hàm list_token_can_get ngon
def list_token_can_get(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color":
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon