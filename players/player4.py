from base import player

player_04 = player.Player("TH", 0)

def action(board, arr_player):
  return moiturn(board)
def nguyenlieucannhat(board):
    nguyenlieucannhat = None
    soluongcan = 0
    for nguyenlieu in player_04.card_upside_down[0].stocks.keys():
        if player_04.card_upside_down[0].stocks[nguyenlieu] > soluongcan:
            soluongcan = player_04.card_upside_down[0].stocks[nguyenlieu]
            nguyenlieucannhat = nguyenlieu
    return nguyenlieucannhat


def nguyenlieucon(board):
    nguyenlieucon = []
    for nguyenlieu in board.stocks.keys():
        if board.stocks[nguyenlieu] > 0 and nguyenlieu != "auto_color" and nguyenlieu != nguyenlieucannhat(board):
            nguyenlieucon.append(nguyenlieu)
    return nguyenlieucon


def nguyenlieucannhi(board):
    luongnguyenlieu = 10
    nguyenlieuthu2 = None
    for nguyenlieu in nguyenlieucon(board):
        if player_04.card_upside_down[0].stocks[nguyenlieu] > 0:
            return nguyenlieu
            luongnguyenlieu = -1
            break
        else:
            if board.stocks[nguyenlieu] < luongnguyenlieu:
                luongnguyenlieu = board.stocks[nguyenlieu]
                nguyenlieuthu2 = nguyenlieu
    if luongnguyenlieu != -1:
        return nguyenlieuthu2


def nguyenlieucanba(board):
    luongnguyenlieu = 10
    nguyenlieuthu3 = None
    for nguyenlieu in nguyenlieucon(board):
        if nguyenlieu != nguyenlieucannhi(board):
            if player_04.card_upside_down[0].stocks[nguyenlieu] > 0:
                return nguyenlieu
                luongnguyenlieu = -1
                break
            else:
                if board.stocks[nguyenlieu] < luongnguyenlieu:
                    luongnguyenlieu = board.stocks[nguyenlieu]
                    nguyenlieuthu3 = nguyenlieu
    if luongnguyenlieu != -1:
        return nguyenlieuthu3
# turn1
# nếu k có thẻ nào trên tay:


def moiturn(board):
    if len(player_04.card_upside_down) == 0:
        thesenhat = None
        for a in board.dict_Card_Stocks_Show["III"]:
            if sum(a.stocks.values()) == 7:
                thesenhat = a
        for a in board.dict_Card_Stocks_Show["III"]:
            if sum(a.stocks.values()) == 10:
                thesenhat = a
        if thesenhat != None:
            return player_04.getUpsideDown(thesenhat, board, {})
        else:
            IIlonnhat = -1
            for a in board.dict_Card_Stocks_Show["II"]:
                if a.score > IIlonnhat:
                    IIlonnhat = a.score
                    thesenhat = a
            print(thesenhat)
            return player_04.getUpsideDown(thesenhat, board, {})
    else:
        # mua thẻ
        if player_04.checkGetCard(player_04.card_upside_down[0]) == True:
            return player_04.getCard(player_04.card_upside_down[0], board)
        # nhặt nguyên liệu
        # nhặt 2 nguyên liệu
        else:
            if player_04.checkOneStock(board, nguyenlieucannhat(board)) == True:
                return player_04.getOneStock(nguyenlieucannhat(board), board, {})
            else:
                # úp thẻ nếu có từ 9 nguyên liệu trở lên
                # tìm nguyên liệu dư
                if sum(player_04.stocks.values()) > 8:
                    for nguyenlieu in player_04.stocks.keys():
                        if player_04.card_upside_down[0].stocks[nguyenlieu] == 0:
                            bo1 = {nguyenlieu: 1}
                            break
                    theseup = None
                    for the in board.dict_Card_Stocks_Show["III"]:
                        if sum(the.stocks.values()) == 7:
                            theseup = the
                    for the in board.dict_Card_Stocks_Show["III"]:
                        if sum(the.stocks.values()) == 10:
                            theseup == the
                    if theseup != None:
                        return player_04.getUpsideDown(theseup, board, bo1)
                    else:
                        IIlon = 0
                        for the in board.dict_Card_Stocks_Show["II"]:
                            if the.score > IIlon:
                                IIlon = the.score
                                theseup = the
                        return player_04.getUpsideDown(theseup, board, bo1)
            # nhặt 3 nguyên liệu
                else:
                    if player_04.checkThreeStocks(board, nguyenlieucannhat(board), nguyenlieucannhi(board), nguyenlieucanba(board)) == True:
                        bo = {}
                        if sum(player_04.stocks.values()) == 8:
                            bo = {nguyenlieucanba(board): 1}
                        return player_04.getThreeStocks(nguyenlieucannhat(board), nguyenlieucannhi(board), nguyenlieucanba(board), board, bo)
