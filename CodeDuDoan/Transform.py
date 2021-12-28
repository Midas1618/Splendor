import json
import pandas as pd

def get_stock(field,arr_dict):
  dict_data = {}
  for i in field:
    dict_data[i]=[]
  for i in arr_dict:
    data = i
    key_field = list(dict_data.keys())
    count = 0
    for k in list(data.values()):
      try:
        dict_data[key_field[count]].append(k)
      except:
        dict_data[key_field[count]].append(-1)
      count += 1
  return dict_data

def get_card(field,arr):
  dict_data = {}
  for i in field:
    dict_data[i]=[]
  for i in arr:
    t = i
    count = 0
    for j in field:
      try:
        dict_data[j].append(t[count])
      except:
        dict_data[j].append(-1)
      count +=1
  return dict_data

def TranFormDataFirst(DataRaw):
  data = DataRaw
  Table = {}
  for columns in data.columns:
      if columns.find("Board I") != -1:
        t = get_card([columns + str(i+1) for i in range(4)],data[columns])
      elif columns.find("Board Noble") != -1:
        t = get_card([columns + str(i+1) for i in range(5)],data[columns])
      elif columns.find("Stocks") != -1:
        if columns.find("Const") != -1:
          t = get_stock([columns + str(i+1) for i in range(5)],data[columns])
        else:
          t = get_stock([columns + str(i+1) for i in range(6)],data[columns])
      elif columns.find("Open") != -1:
          t = get_card([columns+" " + str(i+1) for i in range(15)],data[columns])
      elif columns.find("Upsite Down") != -1:
          t = get_card([columns+" " + str(i+1) for i in range(3)],data[columns])
      elif columns.find("Noble") != -1:
        if columns.find("Board") == -1:
          t = get_card([columns+" " + str(i+1) for i in range(3)],data[columns])
      else:
        t = {columns: data[columns]}
      Table.update(t)
  return pd.DataFrame(Table)

def TranFormDataSecond(s):
  try:
    if s == '':
      return 0
    list_s = s.split("_")
    lenI = s.count("I")
    if lenI == 1:
      return int(list_s[1])
    if lenI == 2:
      return int(list_s[1]) + 40
    if lenI == 3:
      return int(list_s[1])+ 70
    if list_s[0] == 'Noble':
      return int(list_s[1]) + 90
  except:
    if s == -1:
      return 0
  return s

def FinalData(DataRaw):
  df = TranFormDataFirst(DataRaw)
  for column in df.columns.values:
    arr = []
    for row in df[column].values:
      try:
        arr.append(TranFormDataSecond(row))
      except:
        break
    # print(len(arr))
      try:
        df[column] = arr
      except:
        continue
  return df



  
