# -*- coding: utf-8 -*-
import xlrd


# open existing excel file
def open_excel(excel_file='excel.xls'):
    try:
        data = xlrd.open_workbook(excel_file)
        return data
    except Exception, e:
        print str(e)


# convert excel to list
def excel_to_list(excel_file='excel.xls', colnameindex=0, by_index=0):
    data = open_excel(excel_file)
    table = data.sheets()[by_index]                  # open sheet
    nrows = table.nrows                              # row number
    colnames = table.row_values(colnameindex)        # first row value

    information = []
    for rownum in range(1, nrows):
        row = table.row_values(rownum)
        if row:
            app = {}
            for i in range(len(colnames)):           # first row be a dict key and other row be a value
                app[colnames[i]] = row[i]
            information.append(app)
    return information


def main():
    tables = excel_to_list()
    print tables


if __name__ == "__main__":
    main()