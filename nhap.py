import os
import pathlib
import pandas as pd
import json
# # directory = "Knwldg"
# # parent_dir = "C:/Users/Admin/Desktop/Splendor-master/"
# # path = os.path.join(parent_dir, directory)
# # os.mkdir(path)
# code = "100011200000154144300"

# # print(code[:2],code[-2:],code[2:8],code[8:13],code[13:19])
# try:
#     a = pd.read_csv('Knwldg/'+ code[:2] + "/" + code[-2] + "/" + code[2:8] + "/" + code[8:13] + "/" + code[13:19] + ".csv")
# except:
#     pathlib.Path('Knwldg/'+ code[:2] + "/" + code[-2] + "/" + code[2:8] + "/" + code[8:13]).mkdir(parents=True, exist_ok=True) 
#     a = pd.DataFrame({})
#     a.to_csv('Knwldg/'+ code[:2] + "/" + code[-2] + "/" + code[2:8] + "/" + code[8:13] + "/" + code[13:19] + ".csv")
with open("p4learning.json", "w") as outfile:
    json.dump([], outfile)
with open("p3learning.json", "w") as outfile:
    json.dump([], outfile)
with open("p2learning.json", "w") as outfile:
    json.dump([], outfile)
with open("p1learning.json", "w") as outfile:
    json.dump([], outfile)