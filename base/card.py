class Card:
    index = 1
    def __init__(self, score, dict_buy):
        self.score = score
        self.stocks = dict_buy        
        self.id = Card.index
        Card.index +=1

class Card_Stock(Card):
    def __init__(self, type_stock, score, dict_buy):
        super().__init__(score, dict_buy)
        self.type_stock = type_stock

    
class Card_Noble(Card):
    pass
 
    
