from base.board import Board
from base import player
import pandas as pd
import random
import operator
import json
import pathlib
player_02 = player.Player("2", 0)
 
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
            a = "a" + a 
        code += a 
        codes.append(code)
    return codes
 
#basic df
def basic():
    basic = {}
    for a in range (1,41):
        card = "I_"+str(a)
        basic[card] = 1
    for a in range(1,31):
        card = "II_"+str(a)
        basic[card] = 1
    for a in range(1,21):
        card = "III_" + str(a)
        basic[card] = 1
    basic = pd.DataFrame([basic])
    return basic
 
#start df
def start():
    start = {}
    for a in range (1,41):
        card = "I_"+str(a)
        start[card] = 0
    for a in range(1,31):
        card = "II_"+str(a)
        start[card] = 0
    for a in range(1,21):
        card = "III_" + str(a)
        start[card] = 0
    start = pd.DataFrame([start])
    return start
 
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
 
#create mind
def mind(board,player_02):
    ds_codes = codes(board,player_02)
    mind = start()
    for code in ds_codes:
        try:
            a = pd.read_csv('Knwldg/'+ code[:2] + "/" + code[-2:] + "/" + code[2:8] + "/" + code[8:13] + "/" + code[13:19] + ".csv")
        except:
            pathlib.Path('Knwldg/'+ code[:2] + "/" + code[-2:] + "/" + code[2:8] + "/" + code[8:13]).mkdir(parents=True, exist_ok=True) 
            a = basic()
            a.to_csv('Knwldg/'+ code[:2] + "/" + code[-2:] + "/" + code[2:8] + "/" + code[8:13] + "/" + code[13:19] + ".csv")        
        for card in mind:
            mind[card] += a[card]
    return mind
 
#decision
def decision(board,mind,pools):
    rates = []
    current_mind = mind
    current_pools = pools
    for card in current_pools:
        rates.append(int(current_mind[card]))
    chosen = random.choices(current_pools,weights=rates)[0]
    # while chosen in loai:
    #     chosen = random.choices(current_pools,weights=rates)[0]
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
 
def act(target,board,player_02,mind_c,pools_c):
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
                            target_2 = decision(board,mind_c,pools_c)
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
    # print(player_02.score)
    ds_codes = codes(board,player_02)
    # print(codes(board,player_02))
    # print(basic())
    # print(pools(board,player_02))
    # print(mind(board,player_02))
    # print(decision(board,player_02))
    mind_c = mind(board,player_02)
    pools_c = pools(board,player_02)
    # target = decision(board,mind_c,pools_c)
    # loai = []
    ac = None
    time = 0
    while ac == None and time < 16:
        target = decision(board,mind_c,pools_c)
        ac,b = act(target,board,player_02,mind_c,pools_c)
        time += 1
        # print("player 1 ngh?? l???n ",time)
    try:
        f = open("p2learning.json")
        dahoc = json.load(f)
    except:
        dahoc = []
    saving = {}
    for code in ds_codes:
        saving[code] = target.id
    # print(saving)
    dahoc.append(saving)
    # print(dahoc)
    with open("p2learning.json","w") as outfile:
        json.dump(dahoc,outfile)
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
 


