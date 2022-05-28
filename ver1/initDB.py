import pandas as pd
import os
import DEF
import json
from json import JSONEncoder
import numpy

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

path = "DataBase"
subPath = os.listdir(path)
susscess = True # mỗi người 4 tấm ảnh, nếu không đủ là false

encodes = []

for i in subPath:
    sPath = f'{path}/{i}'
    sEncodes = []
    # print(sPath)
    itemsInSubPath = os.listdir(sPath)
    for j in itemsInSubPath:
        sSPath = f'{sPath}/{j}'
        # print(sSPath)
        encodedNumpyData = json.dumps({"value": DEF.getMaHoa(sSPath)}, cls=NumpyArrayEncoder)
        sEncodes.append(encodedNumpyData)
    
    if(len(sEncodes) < 4):
        susscess = False
        break
    sEncodes.append(False)
    encodes.append(sEncodes)
    
# print(encodes)

df = pd.DataFrame(encodes,
                  columns = ['ec1', 'ec2', 'ec3', 'ec4', 'allowed'],
                  index = subPath)

df.to_excel('CSDL.xlsx', sheet_name='Trang_tính1')