# -*- coding: utf-8 -*-
import pandas as pd
import xlrd
import datetime as dt
import os
import pickle

path = r'H:\quant\gtxt_data\boyangwenying3'
res_dict = {}
for root, dirs, files in os.walk(path):
    for name in files:
        dir_name = os.path.join(root, name)
        open_file = xlrd.open_workbook(dir_name, encoding_override='gbk')
        cell = open_file.sheets()[0].cell(0, 2).value
        if cell != '证券代码':
            continue
        df = pd.read_excel(open_file, engine='xlrd', encoding='utf-8', dtype=str)
        # df = df['证券代码']
        df = df.loc[:, ['证券代码', '证券名称']].dropna()
        date_str = os.path.splitext(name)[0][:8]
        res_dict[date_str] = df

print('get res_dict success.')
with open(r'H:\quant\gtxt_data\res_dict_bywy3.pk','wb') as f:
    pickle.dump(res_dict,f)
print('write data to file success.')