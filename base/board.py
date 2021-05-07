import pandas as pd
from base import card
import json
import random


def getType(dict_type):
    for j in dict_type.keys():
        if dict_type[j] == 1:
            return j


class Board:
    def __init__(self):
        self.name = "Board"
        self.stocks = {
            "red": 7,
            "blue": 7,
            "green": 7,
            "white": 7,
            "black": 7,
            "auto_color": 5,
        }
        self.dict_Card_Stocks_Show = {
            "I": [],
            "II": [],
            "III": [],
            "Noble": []
        }
        self.dict_Card_Stocks_UpsiteDown = {
            "I": [],
            "II": [],
            "III": [],
            "Noble": []
        }

# Khởi bàn chơi

    def LoadBase(self):
        '''
        Hàm tạo ra bàn chơi và 
        sắp xếp ngẫu nhiên các thẻ trong bộ úp'''
        with open('Cards_Splendor.json') as datafile:
            data = json.load(datafile)
        for i in data:
            if i["type"] != "Noble":
                c = card.Card_Stock(
                    getType(i["type_stock"]), i["score"], i["stock"])
                self.dict_Card_Stocks_UpsiteDown[i["type"]].append(c)
            else:
                c = card.Card_Noble(i["score"], i["stock"])
                self.dict_Card_Stocks_UpsiteDown["Noble"].append(c)
        for i in self.dict_Card_Stocks_UpsiteDown.keys():
            random.shuffle(self.dict_Card_Stocks_UpsiteDown[i])

# Cài đặt cho các thẻ trong bàn chơi
    def setupCard(self):
        '''Thiết lập thẻ cho bàn chơi'''
        for key in self.dict_Card_Stocks_Show.keys():
            for i in range(4):
                self.dict_Card_Stocks_Show[key].append(
                    self.dict_Card_Stocks_UpsiteDown[key][i])
                self.dict_Card_Stocks_UpsiteDown[key].remove(
                    self.dict_Card_Stocks_UpsiteDown[key][0])
        self.dict_Card_Stocks_Show["Noble"].append(
            self.dict_Card_Stocks_UpsiteDown["Noble"][0])
        self.dict_Card_Stocks_UpsiteDown["Noble"].remove(
            self.dict_Card_Stocks_UpsiteDown["Noble"][0])

# Xóa thẻ trong trồng úp
    def deleteCardInUpsiteDown(self, key, card_stock):
        self.dict_Card_Stocks_UpsiteDown[key].remove(card_stock)
        return self

# Thêm thẻ Nguyên liệu
    def appendUpCard(self, key, card_stock):
        self.dict_Card_Stocks_Show[key].append(card_stock)
        self.deleteCardInUpsiteDown(key, card_stock)
        return self

# Xóa thẻ trên bàn chơi
    def deleteUpCard(self, key, card_stock):
        self.dict_Card_Stocks_Show[key] = [self.dict_Card_Stocks_UpsiteDown[key][0] if i.id == card_stock.id else i for i in self.dict_Card_Stocks_Show[key] ]
        self.deleteCardInUpsiteDown(key,self.dict_Card_Stocks_UpsiteDown[key][0])
        return self
    

# Lấy thông tin các thẻ trên bàn
    def getInforCards(self):
        return self.dict_Card_Stocks_Show

# Trả lại thẻ
    def getStock(self, dict_color):
        for i in dict_color.keys():
            self.stocks[i] -= dict_color[i]
        return self

    def postStock(self, dict_color):
        for i in dict_color:
            self.stocks[i] += dict_color[i]
        return self
    
    def hien_the(self):
        for i in self.dict_Card_Stocks_Show.keys():
            print(i,end=": ")
            for j in self.dict_Card_Stocks_Show[i]:
                print(j.id, end=" ")
            print()