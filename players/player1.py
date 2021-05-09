from base import player

player_01 = player.Player("V", 0)


def action(board, arr_player):
    a = getCardCanUp()
    if a != None:
        return player_01.getCard(a, board)
    else:
        return player_01.getUpsideDown(board.dict_Card_Stocks_UpsiteDown["III"][1], board,{})
def getCardCanUp():
    for i in player_01.card_upside_down:
        if player_01.checkGetCard(i):
            return i


