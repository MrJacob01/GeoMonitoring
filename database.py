import openpyxl
import pandas as pd
from openpyxl.reader.excel import load_workbook
import xlwt
import xlrd
from xlutils.copy import copy
from openpyxl import Workbook
def head_list():
    file = pd.read_excel('asd.xlsx')
    return file.columns


def list_info():
    lists = []
    file = pd.read_excel('asd.xlsx')
    for j in range(0, 2):
        list = []
        for i in range(0, 34):
            item = file.iloc[j]
            list.append(item[i])
        lists.append(list)
    return lists

def filter_mine():
    list = []
    file = pd.read_excel('asd.xlsx')
    for j in range(0, 2):
        file = file.iloc[j]
        list.append(str(file[3]))



