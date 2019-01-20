# -*- coding: utf-8 -*-
import os

# 遍历文件夹下所有文件
path = r'H:\quant\gtxt_data\boyangwenying3'
    for root, dirs, files in os.walk(path):
        for name in files:
            old_dir_name = os.path.join(root, name)
            print(old_dir_name)