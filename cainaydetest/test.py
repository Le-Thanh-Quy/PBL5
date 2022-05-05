import pandas as pd
import DEF
import numpy as np
import json
from json import JSONEncoder


df = pd.read_excel('CSDL.xlsx')

# arr = [0.123, 0.2456, 0.3107]
# ar2 = [f'{round((1 - x), 4) * 100}%' for x in arr]
# print(ar2)

for i in range(len(df.index)):
    for j in range(1, len(df.columns)):
        base = df.loc[i].iat[j]
        base = json.loads(base)
        base = np.asarray(base["value"])
        print(base)
# print(df.iat[2, 3])
# print(type(df.iat[2, 3]))
# print(DEF.getMaHoa("DataBase/Valentines/Valentines.jpg"))
# abc = df.iat[2, 3]

# Deserialization
# decodedArrays = json.loads(abc)

# finalNumpyArray = np.asarray(decodedArrays["value"])
# print(type(finalNumpyArray))