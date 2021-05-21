from base import board
from base import error

class Player:
    # Khởi tạo một người chơi
    def __init__(self, name, score):
        self.message = ""
        self.__name = name
        self.__score = score
        self.__stocks = {
            "red": 0,
            "blue": 0,
            "green": 0,
            "white": 0,
            "black": 0,
            "auto_color": 0,
        }
        self.__stocks_const = {
            "red": 0,
            "blue": 0,
            "green": 0,
            "white": 0,
            "black": 0,
        }
        self.__card_open = []
        self.__card_upside_down = []
        self.__card_noble = []
#Name
    @property
    def name(self):
        return self.__name
    def setName(self,value):
        self.__name = value
#Score   
    @property
    def score(self):
        return self.__score
    @score.setter
    def setScore(self,value):
        self.__score = value
#Stock 
    @property
    def stocks(self):
        return self.__stocks.copy()
    @stocks.setter
    def setStocks(self,value):
        self.__stocks = value
#Stocks Const   
    @property
    def stocks_const(self):
        return self.__stocks_const.copy()
    @stocks_const.setter
    def setStocks_const(self,value):
        self.__stocks_const = value
#card_open    
    @property
    def card_open(self):
        return self.__card_open
    @card_open.setter
    def setCard_open(self,value):
        self.__card_open = value
#card_upside_down
    @property
    def card_upside_down(self):
        return self.__card_upside_down
    @card_upside_down.setter
    def setCard_open(self,value):
        self.__card_upside_down = value
#card_noble
    @property
    def card_noble(self):
        return self.__card_noble
    @card_noble.setter
    def setCard_noble(self,value):
        self.__card_noble = value


# Lấy 3 nguyên liệu

    def getThreeStocks(self, color_1, color_2, color_3, board, dict_return):
        '''
          Đây là hàm lấy thẻ cần 3 tham số truyền vào là ba màu sắc cần lấy.\n
          Màu sắc có kiểu dữ liệu là string.vd: "red", "blue","white"
        '''
        if self.checkThreeStocks(board, color_1, color_2, color_3):
            self.__stocks[color_1] += 1
            self.__stocks[color_2] += 1
            self.__stocks[color_3] += 1
            self.message = self.__name +" Get three stock: " + color_1 + "," + color_2 + "," +color_3+"."
            self.returnStock(dict_return, board)
            error.successColor(self.__name +" Lấy 3 nguyên liệu thành công")
            return board.getStock({color_1: 1, color_2: 1, color_3: 1})
        else:
            return None
# Lấy 1 nguyên liệu

    def getOneStock(self, color_1, board, dict_return):
        '''
          Đây là hàm lấy thẻ cần 1 tham số truyền vào là một màu sắc cần lấy.\n
          Màu sắc có kiểu dữ liệu là string.vd: "red"
        '''
        if self.checkOneStock(board, color_1):
            self.__stocks[color_1] += 2
            self.message = self.__name +" Get One stock: " + color_1
            self.returnStock(dict_return, board)
            error.successColor(self.__name + "Lấy 1 nguyên liệu thành công")
            return board.getStock({color_1: 2})
        else:
            return None
# Úp thẻ

    def getUpsideDown(self, Card, board, dict_return):
        '''
          Đây là hàm lấy thẻ úp
          Card là thẻ\n
          board là bàn chơi \n
        '''
        if self.checkUpsiteDown():
            auto_color = 0
            if board.stocks["auto_color"] >= 1:
                auto_color = 1
                self.__stocks["auto_color"] += 1
            # -------
            a = self.getPositionCard(board, Card)
            show = a["show"]
            key = a["key"]
            if show == True:
                self.__card_upside_down.append(Card)
                board.deleteUpCard(key, Card)
                self.message = self.__name +" Get UpsiteDown id =" + str(Card.id)
            else:
                self.__card_upside_down.append(
                    board.dict_Card_Stocks_UpsiteDown[key][1])
                board.deleteCardInUpsiteDown(
                    key, board.dict_Card_Stocks_UpsiteDown[key][1])
                self.message = self.__name +" Get UpsiteDown in Upsite Board type: " +key+" id = " + str(Card.id)
            self.returnStock(dict_return, board)
            error.successColor(self.__name + " Úp thẻ " + str(Card.id) + " thành công")
            return board.getStock({"auto_color": auto_color})
# Trả thẻ thừa

    def returnStock(self, dict_return, board):
        '''Trả thẻ nếu thừa\n
        amount là số lượng thẻ trả \n
        dict_return danh sách chọn các thẻ trả'''
        if sum(self.__stocks.values()) > 10:
            if sum(dict_return.values()) == sum(self.__stocks.values()) - 10 and self.CheckReturn(dict_return):
                self.message += " Return stock: "
                for i in dict_return.keys():
                    self.__stocks[i] = self.__stocks[i] - dict_return[i]
                    if dict_return[i] != 0:
                        self.message += i + ":" + str(dict_return[i])
                return board.postStock(dict_return)
            else:
                error.errorColor(self.__name + " Số lượng thẻ bỏ chưa đúng hoặc số thẻ trả bị âm, Cần sửa lại ngay")
                return None
# Kiểm tra thỏa mãn điều kiện trả thẻ hay chưa

    def CheckReturn(self, dict_return):
        for i in dict_return.keys():
            if self.__stocks[i] - dict_return[i] < 0:
                return False
        return True
# Kiểm tra xem có lật được thẻ hay không

    def checkGetCard(self, Card):
        try:
            auto_color = self.__stocks["auto_color"]
            for i in Card.stocks.keys():
                if self.__stocks[i] + self.__stocks_const[i] < Card.stocks[i]:
                    if self.__stocks[i] + self.__stocks_const[i] + auto_color >= Card.stocks[i]:
                        auto_color = self.__stocks[i] + self.__stocks_const[i] + auto_color - Card.stocks[i]
                    else:
                        return False
            return True
        except AttributeError:
            error.errorColor("GetCard Có tham số nào đó truyền vào bị rỗng nên không thực hiện được hàm")
        return False


# Lật thẻ

    def getCard(self, Card, board):
        '''
          Đây là hàm lật thẻ
          Card là thẻ\n
          board là bàn chơi \n
        '''
        if self.checkGetCard(Card) == False:
            return None
        else:
            stock_return = {"red": 0,
                            "blue": 0,
                            "green": 0,
                            "white": 0,
                            "black": 0,
                            "auto_color": 0, }
            self.__card_open.append(Card)
            self.message = self.__name + " Get Card = " + str(Card.id)
            self.__score += Card.score
            for i in Card.stocks.keys():
                stocks_late = self.__stocks[i]
                if stocks_late + self.__stocks_const[i] < Card.stocks[i]:
                    auto_color = self.__stocks["auto_color"]
                    self.__stocks["auto_color"] = self.__stocks["auto_color"] - (Card.stocks[i] - self.__stocks[i] -
                         self.__stocks_const[i])
                    self.__stocks[i] = self.__stocks[i] + (auto_color-self.__stocks["auto_color"]) + self.__stocks_const[i] - Card.stocks[i]
                    stock_return["auto_color"] = auto_color - self.__stocks["auto_color"]
                    stock_return[i] = stocks_late
                else:
                    if self.__stocks_const[i] >= Card.stocks[i]:
                        stock_return[i] = 0
                    else:
                        self.__stocks[i] = stocks_late + self.__stocks_const[i] - Card.stocks[i]
                        stock_return[i] = stocks_late - self.__stocks[i]
            self.__stocks_const[Card.type_stock] += 1
            # ------------
            a = self.getPositionCard(board, Card)
            mine = a["mine"]
            if mine == False:
                board = board.deleteUpCard(a["key"], Card)
            else:
                self.__card_upside_down.remove(Card)
            board = self.getNoble(board)
            error.successColor(self.__name + " Lật thẻ " + str(Card.id) + "thành công")
            return board.postStock(stock_return)

    def getPositionCard(self, board, card):
        for i in self.__card_upside_down:
            if i.id == card.id:
                return {
                    "mine": True,
                }
        for i in board.dict_Card_Stocks_Show.keys():
            for j in board.dict_Card_Stocks_Show[i]:
                if j.id == card.id:
                    return{
                        "key": i,
                        "mine": False,
                        "show": True,
                    }
        for i in board.dict_Card_Stocks_UpsiteDown.keys():
            for j in board.dict_Card_Stocks_UpsiteDown[i]:
                if j.id == card.id:
                    return{
                        "key": i,
                        "show": False,
                    }
        error.errorColor("Thẻ có lẽ đã được lật, nên không tìm thấy trong bài úp, trên bàn chơi.")

# Lấy thẻ Quý tộc nếu có thể
    def getNoble(self, board):
        b = []
        for card_Noble in board.dict_Card_Stocks_Show["Noble"]:
            check = True
            for i in card_Noble.stocks.keys():
                if self.__stocks_const[i] < card_Noble.stocks[i]:
                    check = False
            b.append(check)
        for i in range(len(b)):
            if b[i] == True:
                card_Noble = board.dict_Card_Stocks_Show["Noble"][i]
                self.__score += card_Noble.score
                self.__card_noble.append(card_Noble)
                self.message += "Nhan the quy toc id = " + str(card_Noble.id)
                error.RecommendColor(self.__name + "Nhận được " + str(card_Noble.score) + "điểm từ thẻ quý tộc" + str(card_Noble.id))
        for i in self.__card_noble:
            try:
                board.deleteCardNoble(i)
            except:
                continue
        return board
# Kiểm tra xem có úp được thẻ nữa hay không
    def checkUpsiteDown(self):
        try:
            if len(self.__card_upside_down) < 3:
                return True
            else:
                return False
        except AttributeError:
            error.errorColor("Check UpSite Có tham số nào đó truyền vào bị rỗng nên không thực hiện được hàm")
            return False


# Kiểm tra xem có lấy được 3 nguyên liệu hay không

    def checkThreeStocks(self, board, color_1, color_2, color_3):
        try:
            if color_1 == color_2 or color_1 == color_3 or color_2 == color_3:
                return False
            if board.stocks[color_1] == 0:
                return False
            elif board.stocks[color_2] == 0:
                return False
            elif board.stocks[color_3] == 0:
                return False
            return True
        except AttributeError:
            error.errorColor("Check Three Stocks Có tham số nào đó truyền vào bị rỗng nên không thực hiện được hàm")
            return False

# Kiểm tra xem có lấy được 1 nguyên liệu hay không
    def checkOneStock(self, board, color_1):
        try:
            
            if board.stocks[color_1] <= 3:
                return False
            return True
        except AttributeError:
            error.errorColor("Check One Stocks  Có tham số nào đó truyền vào bị rỗng nên không thực hiện được hàm")
            return False
