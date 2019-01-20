# -*- coding: utf-8 -*-

import os
import datetime as dt

def file_rename():
    path = r'H:\quant\gtxt_data\boyangwenying3'
    i = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            i = i + 1
            old_dir_name = os.path.join(root, name)
            print(old_dir_name)
            print(os.path.getmtime(old_dir_name))
            get_file_mtime = dt.datetime.fromtimestamp(os.path.getmtime(old_dir_name)).strftime('%Y%m%d%H%M%S')
            print(get_file_mtime)
            filetype = os.path.splitext(name)[1]
            new_dir_name = os.path.join(root, get_file_mtime + 'bywy3' + str(i) + filetype)
            print(new_dir_name)
            os.rename(old_dir_name, new_dir_name)
            print('%s-->>%s' % (old_dir_name, new_dir_name))
            print('-' * 40)


if __name__ == '__main__':
    file_rename()
    print('rename done.')