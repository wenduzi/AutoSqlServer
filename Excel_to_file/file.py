# -*- coding: utf-8 -*-
from excel import excel_table_byindex
import os


def operate_file(old_file='file.ini'):
    info = excel_table_byindex()
    for i in range(len(info)):
        instance_name = info[i]['NAME']
        with open(old_file, 'r') as fr:
            with open(instance_name, 'w') as fw:
                for line in fr.readlines():
                    reline = line.replace('mysql', instance_name)
                    fw.write(reline)


def main():
    operate_file()
    for filename in os.listdir(r'/root/PycharmProjects/AutoSqlServer/Excel_to_file'):
        print filename


if __name__ == "__main__":
    main()
