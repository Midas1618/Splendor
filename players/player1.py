from base import player

player_01 = player.Player("V", 0)


def action(board, arr_player, t):
    if t:
    # if XetDieuKien(arr_player) == True and player_01.checkOneStock(board, "blue"):
    # return player_01.getUpsideDown(ChooseMaxScoreCard(board, "III"), board,True,"III",{})
      return player_01.getThreeStocks("blue","red","green", board, {})
    else:
      return player_01.getThreeStocks("blue","red","green", board, {"white":1,"red":1})

def XetDieuKien(arr_player):
  for i in arr_player:
    if i.stocks["blue"] != 0:
      return False
  return True
def chooseStock():
  return {"red": 1, "blue":1}

def ChooseMaxScoreCard(board, key):
  max = 0
  card = None
  for i in board.dict_Card_Stocks_Show[key]:
    if i.score > max:
      max = i.score
      card = i
  return card