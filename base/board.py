import pandas as pd
from base import card
import json
import random
from base import error

def getType(dict_type):
    for j in dict_type.keys():
        if dict_type[j] == 1:
            return j

class Board:
    def __init__(self):
        self.name = "Board"
        self.__stocks = {
            "red": 7,
            "blue": 7,
            "green": 7,
            "white": 7,
            "black": 7,
            "auto_color": 5,
        }
        self.__dict_Card_Stocks_Show = {
            "I": [],
            "II": [],
            "III": [],
            "Noble": []
        }
        self.__dict_Card_Stocks_UpsiteDown = {
            "I": [],
            "II": [],
            "III": [],
            "Noble": []
        }
    @property
    def stocks(self):
        return self.__stocks.copy()
    @stocks.setter
    def setStocks(self,value):
        self.__stocks = value
    @property
    def dict_Card_Stocks_Show(self):
        return self.__dict_Card_Stocks_Show.copy()
    @dict_Card_Stocks_Show.setter
    def setDict_Card_Stocks_Show(self,value):
        self.__dict_Card_Stocks_Show = value
    @property
    def dict_Card_Stocks_UpsiteDown(self):
        return self.__dict_Card_Stocks_UpsiteDown.copy()
    @dict_Card_Stocks_UpsiteDown.setter
    def setDict_Card_Stocks_UpsiteDown(self,value):
        self.__dict_Card_Stocks_UpsiteDown= value

# Khởi bàn chơi
    def LoadBase(self):
        '''
        Hàm tạo ra bàn chơi và 
        sắp xếp ngẫu nhiên các thẻ trong bộ úp'''
        with open('Cards_Splendor.json') as datafile:
            data = json.load(datafile)
        Ma = ""
        stt = 1
        for i in data:
            if stt <= 40:
                Ma = "I_" + str(stt)
            elif stt <= 70:
                Ma = "II_" + str(stt - 40)
            elif stt <= 90:
                Ma = "III_" + str(stt - 70)
            else : 
                Ma = "Noble_"+ str(stt - 90)
            stt+=1
            if i["type"] != "Noble":
                c = card.Card_Stock(Ma,
                    getType(i["type_stock"]), i["score"], i["stock"])
                self.__dict_Card_Stocks_UpsiteDown[i["type"]].append(c)
            else:
                c = card.Card_Noble(Ma,i["score"], i["stock"])
                self.__dict_Card_Stocks_UpsiteDown["Noble"].append(c)


    def randomCard(self):
        for i in self.__dict_Card_Stocks_UpsiteDown.keys():
            random.shuffle(self.__dict_Card_Stocks_UpsiteDown[i])
        

# Cài đặt cho các thẻ trong bàn chơi
    def setupCard(self):
        '''Thiết lập thẻ cho bàn chơi'''
        self.randomCard()
        for key in self.__dict_Card_Stocks_Show.keys():
            for i in range(4):
                self.__dict_Card_Stocks_Show[key].append(
                    self.__dict_Card_Stocks_UpsiteDown[key][0])
                self.__dict_Card_Stocks_UpsiteDown[key].remove(
                    self.__dict_Card_Stocks_UpsiteDown[key][0])
        self.__dict_Card_Stocks_Show["Noble"].append(
            self.__dict_Card_Stocks_UpsiteDown["Noble"][0])
        self.__dict_Card_Stocks_UpsiteDown["Noble"].remove(
            self.__dict_Card_Stocks_UpsiteDown["Noble"][0])

# Xóa thẻ trong trồng úp
    def deleteCardInUpsiteDown(self, key, card_stock):
        try:
            self.__dict_Card_Stocks_UpsiteDown[key].remove(card_stock)
        except:
            pass      
        return self
    
    def deleteCardNoble(self, CardNoble):
        try:
            self.__dict_Card_Stocks_Show["Noble"].remove(CardNoble)
        except:
            pass      
        return self

# Thêm thẻ Nguyên liệu
    def appendUpCard(self, key, card_stock):
        try:
            self.__dict_Card_Stocks_Show[key].append(card_stock)
            self.deleteCardInUpsiteDown(key, card_stock)
        except:
            error.RecommendColor("Hết thẻ rồi, Không thêm nguyên liệu được nữa đâu")
        return self

# Xóa thẻ trên bàn chơi
    def deleteUpCard(self, key, card_stock):
        try:
            try:
                a = self.__dict_Card_Stocks_UpsiteDown[key][0]
            except:
                a = None
            if a != None:
                self.__dict_Card_Stocks_Show[key] = [a if i.id == card_stock.id else i for i in self.__dict_Card_Stocks_Show[key] ]
                self.deleteCardInUpsiteDown(key,a)
            else:
                self.__dict_Card_Stocks_Show[key].remove(card_stock)
        except:
            error.RecommendColor("Không thể xóa thẻ trên bàn vì chắc chẳng còn thẻ đâu")
            pass
        return self
    

# Lấy thông tin các thẻ trên bàn
    def getInforCards(self):
        return self.__dict_Card_Stocks_Show

# Trả lại thẻ
    def getStock(self, dict_color):
        for i in dict_color.keys():
            self.__stocks[i] -= dict_color[i]
        return self

    def postStock(self, dict_color):
        for i in dict_color:
            self.__stocks[i] += dict_color[i]
        return self
    
    def hien_the(self):
        for i in self.__dict_Card_Stocks_Show.keys():
            print(i,end=": ")
            for j in self.__dict_Card_Stocks_Show[i]:
                print(j.id, end=" ")
            print()