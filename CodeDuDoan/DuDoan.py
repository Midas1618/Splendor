from CodeDuDoan import Transform
import pandas as pd
import numpy as np

df_detail = pd.read_excel("Data.xlsx",engine='openpyxl')

df_detail = df_detail.fillna(0)

df_caculater = pd.DataFrame({})

def stockCard(stock,stock_const,board_card):
  total_value = 1
  for i in board_card:
    score = df_detail["score"].iloc[i+1]
    board_card_stock = np.array(df_detail[["Stock1","Stock2","Stock3","Stock4","Stock5"]].iloc[i+1])
    b = np.subtract(board_card_stock,np.add(stock_const,stock))
    c = np.sum(board_card_stock) - np.sum(np.where(b>0,b,0))
    total_value += (score+1)/(np.where(c>0,c,0)+1)
  return total_value

def stockNoble(stock_const,board_noble):
  total_value = 1
  for i in board_noble:
    board_noble_stock = np.array(df_detail[df_detail["ID"] == i][["Stock1",	"Stock2",	"Stock3",	"Stock4",	"Stock5"]])
    b = np.subtract(board_noble_stock,stock_const)    
    c = np.sum(board_noble_stock) - np.sum(np.where(b>0,b,0))
    total_value += 3/(np.where(c>0,c,0)+1)
  return total_value

def tinhDiemConst(*arg):
  sum = 0
  for i in arg:
    sum += i
  return sum

def stockpro(stock_player,stock_const,stock_board):
  return max(np.subtract(stock_const,stock_board))


def SetUpData():
  df_caculater["Turn"] = df["Turn"]
  for player in range(1,5):
    df_caculater[str(player)+"_const"] = df[[str(player) +" Stocks" + str(i) for i in range(1,7)]].sum(axis = 1)
    df_caculater[str(player)+"_board_const"] = df[["Board Stocks" + str(i) for i in range(1,7)]].sum(axis = 1)
    df_caculater[str(player)+"_score"] = df[str(player)+" Score"]
    df_caculater[str(player)+"_I"] =  np.array(df.apply(lambda row: stockCard(
                                                      [row[str(player) +" Stocks" + str(i)] for i in range(1,6)],
                                                      [row[str(player) +" Stocks Const" + str(i)] for i in range(1,6)],
                                                      [row["Board I" + str(i)] for i in range(1,5)]),axis=1))
    df_caculater[str(player)+"_II"] =  np.array(df.apply(lambda row: stockCard(
                                                        [row[str(player) +" Stocks" + str(i)] for i in range(1,6)],
                                                        [row[str(player) +" Stocks Const" + str(i)] for i in range(1,6)],
                                                        [row["Board I" + str(i)] for i in range(1,5)]),axis=1))
    df_caculater[str(player)+"_III"] =  np.array(df.apply(lambda row: stockCard(
                                                        [row[str(player) +" Stocks" + str(i)] for i in range(1,6)],
                                                        [row[str(player) +" Stocks Const" + str(i)] for i in range(1,6)],
                                                        [row["Board I" + str(i)] for i in range(1,5)]),axis=1))
    df_caculater[str(player)+"_const_nl_sum"] =  np.array(df[[str(player) +" Stocks Const" + str(i) for i in range(1,6)]].apply(lambda row: tinhDiemConst(row[str(player) +" Stocks Const1" ],
                                                                                                                 row[str(player) +" Stocks Const2" ],
                                                                                                                 row[str(player) +" Stocks Const3" ],
                                                                                                                 row[str(player) +" Stocks Const4"],
                                                                                                                row[str(player) +" Stocks Const5"]),axis=1))
    df_caculater[str(player)+"_best_const"] =  np.array(df.apply(lambda row: stockpro([row[str(player) +" Stocks Const" + str(i)] for i in range(1,6)],
                                                      [row[str(player) +" Stocks" + str(i)] for i in range(1,6)],
                                                      [row["Board Stocks" + str(i)] for i in range(1,6)]),axis=1))
    df_caculater[str(player)+"_noble"] =  np.array(df.apply(lambda row: stockNoble([row[str(player) +" Stocks Const" + str(i)] for i in range(1,6)],
                                                      [row["Board Noble" + str(i)] for i in range(1,6)]),axis=1))
    




def DuDoan(DataRaw):
  global df
  df = Transform.FinalData(DataRaw)
  SetUpData()
  df_moi = pd.DataFrame({})
  # print(df_caculater)
  for i in range(1,5):
    player = str(i)
    df_moi[str(player)] = np.array(df_caculater.apply(lambda row: caculater(row[player+"_const_nl_sum"],
                                                                            row[player+"_best_const"],
                                                                            row[player+"_noble"],
                                                                            row[player+"_const"],
                                                                            row[player+"_board_const"],
                                                                            row[player+"_score"],
                                                                            row["Turn"],
                                                                            row[player+"_I"],
                                                                            row[player+"_II"],
                                                                            row[player+"_III"],),axis=1))
  # print(df_moi)
  return df_moi.idxmax(axis=1).loc[0]

def caculater(const_nl,best_const,noble,stocks,board_const,score,turn,loai1,loai2,loai3):
  return const_nl + score

  
  
