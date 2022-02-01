# import pathlib
# pathlib.Path('Knwldg').mkdir(parents=True, exist_ok=True) 
import pandas as pd
def start():
    start = []
    for a in range (1,41):
        card = "I_"+str(a)
        start.append(card)
    for a in range(1,31):
        card = "II_"+str(a)
        start.append(card)
    for a in range(1,21):
        card = "III_" + str(a)
        start.append(card)
    a = pd.DataFrame()
    a["basic"] = start
    a["turn"] = 0
    return a
start().to_csv("1l.csv",index = False)
start().to_csv("2l.csv",index = False)
start().to_csv("3l.csv",index = False)
start().to_csv("4l.csv",index = False)
start().to_csv("Knwldg.csv",index = False)
