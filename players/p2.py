from base.board import Board
from base import player
import pandas as pd
import random
import operator
import json
player_02 = player.Player("player_02", 0)
import pathlib
import numpy as np
# pathlib.Path('/my/directory').mkdir(parents=True, exist_ok=True) 


#code creation
def codes(board,player_02):
    codes = []
    for Noble in board.dict_Card_Stocks_Show["Noble"]:
        code = str(Noble.id)[6:]
        for nl in player_02.stocks.keys():
            code += str(player_02.stocks[nl])
        for nl in player_02.stocks_const.keys():
            code += str(player_02.stocks_const[nl])
        for nl in board.stocks.keys():
            code += str(board.stocks[nl])
        a = str(player_02.score)
        if len(a) < 2:
            a = "0" + a 
        code += a 
        codes.append(code)
    return codes
 
 
#pools of cards
def pools(board,player_02):
    cards = []
    for card in board.dict_Card_Stocks_Show["I"]:
        cards.append(card.id)
    for card in board.dict_Card_Stocks_Show["II"]:
        cards.append(card.id)
    for card in board.dict_Card_Stocks_Show["III"]:
        cards.append(card.id)
    for card in player_02.card_upside_down:
        cards.append(card.id)
    return cards
 
 
#decision
def decision(board,data,pools,loai):
    current_mind = data
    current_pools = pools
    use = current_mind[current_mind['basic'].isin(pools)]
    list_de_chon = list(use["basic"])
    list_rate = list(use["mind"])
    for the in loai:
        vi_tri = list_de_chon.index(the)
        list_rate.pop(vi_tri)
        list_de_chon.pop(vi_tri)
    if len(list_de_chon) == 0:
        return None
    chosen = random.choices(list_de_chon,list_rate)[0]
    #  chosen
    # print(pools)
    for card in board.dict_Card_Stocks_Show["I"]:
        if card.id == chosen:
            return card
    for card in board.dict_Card_Stocks_Show["II"]:
        if card.id == chosen:
            return card
    for card in board.dict_Card_Stocks_Show["III"]:
        if card.id == chosen:
            return card
    for card in player_02.card_upside_down:
        if card.id == chosen:
            return card
 
def act(target,board,player_02,data,pools_c):
    missing = {}
    for nl in target.stocks.keys():
        thieu = target.stocks[nl] - player_02.stocks[nl] - player_02.stocks_const[nl]
        if thieu > 0:
            missing[nl] = thieu
    if sum(missing.values()) > 10:
        return None,player_02.stocks
    else:
        if player_02.checkGetCard(target) == True:
            return "up",target
        can_va_co = []
        for nl in missing.keys():
            if board.stocks[nl] > 0:
                can_va_co.append(nl)
        if len(can_va_co) == 0:
            if board.stocks['auto_color'] == 0:
                return None,2
            else:
                if player_02.checkUpsiteDown() == True:
                    if target not in player_02.card_upside_down:
                        return "down",target
                    else:
                        state = False
                        while state == False:
                            target_2 = decision(board,data,pools_c,[])
                            state = target_2 not in player_02.card_upside_down
                        return "down",target_2
                else:
                    return None, 3
        else:
            nl_lay = {}
            dinh_lay = []
            state = None
            for nl in can_va_co:
                dinh_lay.append(nl)
            for nl in target.stocks.keys():
                if nl not in can_va_co and board.stocks[nl] > 0:
                    dinh_lay.append(nl)
            co_the_lay = min(3,10 - sum(player_02.stocks.values()),len(dinh_lay))
            cbi_lay = []
            for so_luong in range(co_the_lay):
                cbi_lay.append(dinh_lay[so_luong])
                nl_lay[dinh_lay[so_luong]] =1
            if len(cbi_lay) == 3:
                # ac =  player_02.getThreeStocks(nl_lay,board,{})
                return "3", cbi_lay
            if len(cbi_lay) == 2:
                # ac =  player_02.getOneTwoStock(cbi_lay[0],cbi_lay[1],board,{})
                return "2", cbi_lay
            if len(cbi_lay) == 1:
                # ac =  player_02.getOneTwoStock(cbi_lay[0],'Null',board,{})
                return "1",cbi_lay
    return None,None
 
def action(board, arr_player):
    # print(1)
    ds_codes = codes(board,player_02)
    mind = pd.DataFrame(np.zeros(90))
    data = pd.read_csv('Knwldg.csv')
    for code in ds_codes:
        try:
            a = data[code]
        except:
            a = pd.DataFrame(np.ones(90))
            data[code] = a
        mind += a
    data["mind"] = mind
    pools_c = pools(board,player_02)
    ac = None
    # time = 0
    loai =[]
    while ac == None and len(loai) < 12:
        target = decision(board,data,pools_c,loai)
        if target == None:
            return board
        loai.append(target.id)
        ac,b = act(target,board,player_02,data,pools_c)
        # time += 1
    # print(target.id)
    learning = pd.read_csv("2l.csv")
    turn = list(learning["turn"])[0]
    turn += 1
    vi_tri = list(learning["basic"]).index(target.id)
    saving = np.zeros(90)
    saving[vi_tri] = turn
    # print(saving)
    for code in ds_codes:
        # print(code)
        learning[code] = saving
    learning["turn"] = turn
    learning.to_csv("2l.csv",index = False)
    if ac == "up":
        return player_02.getCard(b,board)
    if ac == "down":
        return player_02.getUpsideDown(b,board,{})
    if ac == "3":
        return player_02.getThreeStocks(b[0],b[1],b[2],board,{})
    if ac == "2":
        return player_02.getOneTwoStock(b[0],b[1],board,{})
    if ac == "1":
        return player_02.getOneTwoStock(b[0],"Null",board,{})
    return board
 
 
 
 
 
 

