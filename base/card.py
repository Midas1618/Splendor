class Card:
    index = 1
    def __init__(self, score, dict_buy):
        self.__score = score
        self.__stocks = dict_buy        
        Card.index +=1
        self.id = Card.index
        
    @property
    def score(self):
        return self.__score
    @score.setter
    def setScore(self,value):
        self.__score = value
    #Stock 
    @property
    def stocks(self):
        return self.__stocks
    @stocks.setter
    def setStocks(self,value):
        self.__stocks = value

class Card_Stock(Card):
    def __init__(self, type_stock, score, dict_buy):
        super().__init__(score, dict_buy)
        self.__type_stock = type_stock.replace("type_","")
    @property
    def type_stock(self):
        return self.__type_stock
    @type_stock.setter
    def setType_stock(self,value):
        self.__type_stock = value

    
class Card_Noble(Card):
    pass
 
    
