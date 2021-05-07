from base import board


class Player:
    # Khởi tạo một người chơi
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.stocks = {
            "red": 0,
            "blue": 0,
            "green": 0,
            "white": 0,
            "black": 0,
            "auto_color": 0,
        }
        self.stocks_const = {
            "red": 0,
            "blue": 0,
            "green": 0,
            "white": 0,
            "black": 0,
        }
        self.card_open = []
        self.card_upside_down = []

# Lấy 3 nguyên liệu
    def getThreeStocks(self, color_1, color_2, color_3, board, dict_return):
        '''
          Đây là hàm lấy thẻ cần 3 tham số truyền vào là ba màu sắc cần lấy.\n
          Màu sắc có kiểu dữ liệu là string.vd: "red", "blue","white"
        '''
        if self.checkThreeStocks(board,color_1, color_2, color_3):
            self.stocks[color_1] += 1
            self.stocks[color_2] += 1
            self.stocks[color_3] += 1
            self.returnStock(dict_return,board)
            return board.getStock({color_1: 1, color_2: 1, color_3: 1})
        else:
            return None

# Lấy 1 nguyên liệu
    def getOneStock(self, color_1, board, dict_return):
        '''
          Đây là hàm lấy thẻ cần 1 tham số truyền vào là một màu sắc cần lấy.\n
          Màu sắc có kiểu dữ liệu là string.vd: "red"
        '''
        if self.checkOneStock(board,color_1):
            self.stocks[color_1] += 2
            self.returnStock(dict_return,board)
            return board.getStock({color_1: 2})
        else:
            return None

# Úp thẻ
    def getUpsideDown(self, Card, board, show, key, dict_return):
        '''
          Đây là hàm lấy thẻ úp
          Card là thẻ\n
          board là bàn chơi \n 
          show là chọn trồng bài đã mở hay thẻ úp. True thì sẽ lấy thẻ trên bàn, False thì sẽ lấy trong chồng bài úp \n
          key là loại thẻ cần lấy
        '''
        if self.checkUpsiteDown():
            auto_color = 0
            if board.stocks["auto_color"] >= 1:
                auto_color = 1
                self.stocks["auto_color"] += 1
            self.returnStock(dict_return,board)
            if show == True:
                self.card_upside_down.append(Card)
                board.deleteUpCard(key, Card)
                return board.getStock({"auto_color": auto_color})
            else:
                self.card_upside_down.append(board.dict_Card_Stocks_UpsiteDown[key][0])
                board.deleteCardInUpsiteDown(key,board.dict_Card_Stocks_UpsiteDown[key][0])
                return board.getStock({"auto_color": auto_color})
            
        return board

# Trả thẻ thừa
    def returnStock(self, dict_return, board):
        '''Trả thẻ nếu thừa\n 
        amount là số lượng thẻ trả \n
        dict_return danh sách chọn các thẻ trả'''
        if sum(self.stocks.values()) > 10:
            if sum(dict_return.values()) == sum(self.stocks.values()) - 10:
                for i in dict_return.keys():
                    self.stocks[i] = self.stocks[i] - dict_return[i]
            else:
                print("Số lượng thẻ bỏ chưa đúng, Cần sửa lại ngay")
            return board.postStock(dict_return)

# Kiểm tra xem có lật được thẻ hay không
    def checkGetCard(self, Card):
        auto_color = self.stocks["auto_color"]
        for i in Card.stock:
            if self.stocks[i] < Card.stocks[i]:
                if self.stocks[i] + auto_color > Card.stocks[i]:
                    auto_color = self.stocks[i] + auto_color - Card.stocks[i]
                else:
                    return False
        return True

# Lật thẻ
    def getCard(self, Card, board):
        '''
          Đây là hàm lấy thẻ cần 1 tham số truyền vào là Card_Stock
        '''
        if checkGetCard(Card, self) == False:
            return None
        else:
            stock_return = {"red": 0,
                            "blue": 0,
                            "green": 0,
                            "white": 0,
                            "black": 0,
                            "auto_color": 0, }
            self.card_open.append(Card)
            self.score += Card.score
            for i in Card.stocks.keys():
                stocks_late = self.stocks[i]
                if stocks_late + self.stocks_const[i] < Card.stocks[i]:
                    auto_color = self.stocks["auto_color"]
                    self.stocks["auto_color"] = self.stocks["auto_color"] - \
                        (Card.stocks[i] -
                         self.stocks[i] - self.stocks_const[i])
                    self.stocks[i] = self.stocks[i] + auto_color + \
                        self.stocks_const[i] - Card.stocks[i]
                    stock_return["auto_color"] = auto_color - \
                        self.stocks["auto_color"]
                else:
                    self.stocks[i] = stocks_late + \
                        self.stocks_const[i] - Card.stocks[i]
                stock_return[i] = stocks_late
            self.stocks_const[Card.type_stock] += 1
            return board

# Kiểm tra xem có úp được thẻ nữa hay không
    def checkUpsiteDown(self):
        if len(self.card_upside_down) < 3:
            return True
        else:
            return False

    def checkThreeStocks(self, board, color_1, color_2, color_3):
        if board.stocks[color_1] == 0:
            return False
        elif board.stocks[color_2] == 0:
            return False
        elif board.stocks[color_3] == 0:
            return False
        return True

# Kiểm tra xem có lấy được 3 nguyên liệu hay không
    
# Kiểm tra xem có lấy được 1 nguyên liệu hay không
    def checkOneStock(self, board, color_1):
        if board.stocks[color_1] <= 3:
            return False
        return True
        