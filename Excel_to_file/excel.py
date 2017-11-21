# -*- coding: utf-8 -*-
import xlrd


def open_excel(excel_file='excel.xls'):
    try:
        data = xlrd.open_workbook(excel_file)
        return data
    except Exception, e:
        print str(e)


def excel_table_byindex(excel_file='excel.xls', colnameindex=0, by_index=0):
    data = open_excel(excel_file)
    table = data.sheets()[by_index]
    nrows = table.nrows                              # row number
    colnames = table.row_values(colnameindex)        # first line value

    information = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            information.append(app)
    return information


def main():
    tables = excel_table_byindex()
    print tables


if __name__ == "__main__":
    main()