
from base import player
import random
import math
player_01 = player.Player("Violet", 0)




def list_the_ngon(board):
    the_ngon =[]
    type = ["III","II"]
    for i in type:
        for card in board.dict_Card_Stocks_Show[i]:
            if card.score == 2 and sum(card.stocks.values()) == 5:
                the_ngon.append(card)
            if card.score == 3 and sum(card.stocks.values()) == 6:
                the_ngon.append(card)
           
    print("1") 
    return the_ngon 

def list_token_for_Card_down(board):
    list_token_for_Card_down = []
    dict_start = {
        "red" : 0,
       "white" : 0,
       "blue" : 0,
       "green" : 0,
       "black" : 0}
    box = []
    if len(player_01.card_upside_down)>0:
        box = list_Card_down()[0]
        a = 0
        for token in list(box.stocks.keys()):
            if(box.stocks[token] - player_01.stocks[token] - player_01.stocks_const[token]) > a:
                if board.stocks[token]>0:
                    a = box.stocks[token]- player_01.stocks[token] - player_01.stocks_const[token]
                    list_token_for_Card_down.append(token)
    print(2)
    return list_token_for_Card_down


def list_Card_down():
    A = []
    if len(player_01.card_upside_down)>0:
        for object in  player_01.card_upside_down:
            Card_down =  player_01.card_upside_down.copy()
            Card_down.remove(object)
            for card in Card_down:
                if card.stocks[object.type_stock] > 0:
                    A.append(object)
    print(3)
    return A


def tra_token(board, *args) :
    dict_bo = {
        "red" : 0,
        "blue" : 0,
        "green" : 0,
        "black" : 0,
        "white" : 0,
        "auto_color" : 0 }
    dict_bd = player_01.stocks.copy()
  
    list = list_token_return(board).copy()
    if sum(dict_bd.values())>10:
        n = sum(dict_bd.values()) - 10
        i = 0
        while n!=0:
            if dict_bd[list[i]] !=0:
                       dict_bo[list[i]] +=1
                       dict_bd[list[i]] -=1
                       n -= 1
            else:
                i += 1
    print(4)
    return dict_bo


def list_token_return(board):
    token_return = []
    for token in player_01.stocks.keys():
        if player_01.stocks[token]>0 and token!= "auto_color":
            if token not in  list_token_for_Card_down(board):
                token_return.append(token)
    item =  list_token_for_Card_down(board).copy()
    item.reverse()
    for token in item:
        if player_01.stocks[token] > 0 and token not in token_return:
            token_return.append(token)
    print(5)
    return token_return

                
def support_card(board):
    support_card = []
    cardx= None
    type = ["II", "I"]
    if len(list_token_for_Card_down(board))>0:
        for token in list_token_for_Card_down(board) :
            for i in type:
                for card in board.dict_Card_Stocks_Show[i]:
                    if card.type_stock == token :
                        support_card.append(card)
        b = 0
        for card in support_card:
            if card.score / sum(card.stocks.values()) > b :
                b = card.score / sum(card.stocks.values())
                cardx = card
        print(6)
        return cardx
    

def token_support_card(board):
    dict = {}
    token_support = []
    if support_card(board) != None:
        dict = support_card(board).stocks.copy()
        for token in dict.keys():
            if dict[token] > 0:
                if board.stocks[token] >0 :
                    token_support.append(token)
    print(7)
    return token_support

def list_card_can_take(board):
    card_can_take = []
    for card in list_Card_down():
        if player_01.checkGetCard(card):
            card_can_take.append(card)
    for card in list_the_ngon(board):
        if player_01.checkGetCard(card):
            card_can_take.append(card)
        if support_card(board)!=None:
            if player_01.checkGetCard(card):
                card_can_take.append(card)
    print(8)           
    return card_can_take

def take_card_to_take_noble(board):
    dict_card = {}
    dict_card['red'] = 0  
    dict_card['blue'] = 0 
    dict_card['green'] = 0 
    dict_card['black'] = 0 
    dict_card['white'] = 0
    dict_card_value = {}
    card_in_hand = list_card_can_take(board)
    target_noble = []
    for card in board.dict_Card_Stocks_UpsiteDown['Noble']:
        dict_card_to_take = {}
        for type_card in card.stocks.keys():
            dict_card_to_take[type_card] = max(card.stocks[type_card] - player_01.stocks_const[type_card], 0)
        if sum(list(dict_card_to_take.values()))>2:
            continue
        else:
            print(15)
            dict_card_value[card] = dict_card_to_take
            target_noble.append(sum(list(dict_card_to_take.values())))
        list_card_noble = list(dict_card_value.keys())
        noble_should_get = []
        while len(target_noble) > 0:
           index_card = target_noble.index(min(target_noble))
           noble_should_get.append(list_card_noble [index_card])
           target_noble.remove(min(target_noble))
           list_card_noble.remove(list_card_noble[index_card])
        if len(noble_should_get) > 0:
            list_card_should_take = []
            for card in  card_in_hand:
                if card.type_stock in list(dict_card_value[noble_should_get[0]].keys()):
                    list_card_should_take.append(card)
            print(16)
            return list_card_should_take


def action(board, arr_player):
    if len(list_card_can_take(board)) > 0:
        print(9)
        return player_01.getCard(list_card_can_take(board)[0],board)
    if len(list_the_ngon(board))>0:
        if player_01.checkUpsiteDown():
             print(10)
             return player_01.getUpsideDown(list_the_ngon(board)[0], board,tra_token)
    if len(player_01.card_upside_down)>0:
        if sum(player_01.stocks.values()) <=8:
            if len(list_token_for_Card_down(board)) > 0:
                print(11)
                if player_01.checkOneStock(board,list_token_for_Card_down(board)[0]):
                     print("12")
                     return player_01.getOneStock(list_token_for_Card_down(board)[0], board, tra_token)
            if len(list_token_for_Card_down(board))>2:
                if player_01.checkThreeStocks(board, list_token_for_Card_down(board)[0], list_token_for_Card_down(board)[1], list_token_for_Card_down(board)[2]):
                    print(13)
                    return player_01.getThreeStocks(list_token_for_Card_down(board)[0], list_token_for_Card_down(board)[1], list_token_for_Card_down(board)[2], board, tra_token)

            if support_card(board) != None:
                    if len(token_support_card(board))> 2:
                           if player_01.checkThreeStocks(board, token_support_card(board)[0], token_support_card(board)[1], token_support_card(board)[2]):
                              print("co len")
                              return player_01.getThreeStocks(token_support_card(board)[0], token_support_card(board)[1], token_support_card(board)[2], board, tra_token)
                    for token in token_support_card(board):
                        if player_01.checkOneStock(board, token):
                            print(14)
                            return player_01.getOneStock(token, board, tra_token)
            else:
               card_in_hand = take_card_to_take_noble(board)
               if card_in_hand != None:
                   for card in card_in_hand:
                       return player_01.getCard(card, board)
                   



    print(19)
    return board



            
