import pandas as pd

import openpyxl
import json
from collections import OrderedDict
import pprint
import time

# エクセルファイルのロード
excel_path = './syllabus.xlsx'


print(pd.__version__)
# 1.2.2

# df.to_excel('sylllabus.xlsx', index=False, header=False)
