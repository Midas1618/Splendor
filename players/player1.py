from base import player

player_01 = player.Player("Vang", 0)


def action(board, arr_player):
  return player_01.getUpsideDown(board.dict_Card_Stocks_Show["I"][0], board,True,"I",{})
  # return player_01.getThreeStocks("red","blue","green", board, chooseStock())

def chooseStock():
  return {"red": 1, "blue":1}