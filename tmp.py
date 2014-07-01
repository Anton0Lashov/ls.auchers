__author__ = '@antonyLash'
# -*- coding: utf-8 -*-
# -*- coding: cp1251 -*-

import logging
import os
import shutil
from math import *
import time
import sys
from suds.client import Client

import xlwt
import xlrd

# формирование словаря №1
def dict_one():
    workbook = xlrd.open_workbook("source/Input.xls", on_demand=True, formatting_info=True)
    worksheet2 = workbook.sheet_by_name('Sheet1')
    num_rows = worksheet2.nrows - 1
    # print u'Кол-во импортированных строк из файла Input.xls:', num_rows
    nm_rw = str(num_rows + 1)
    logging.info(u'Кол-во импортированных строк из файла Input.xls: ' + nm_rw)
    num_cells = worksheet2.ncols - 1
    # print u'Кол-во импортированных солбцов из файла Input.xls:', num_cells
    nm_cls = str(num_cells + 1)
    logging.info(u'Кол-во импортированных столбцов из файла Input.xls: ' + nm_cls)
    dict_main = {0: 0}
    cur_row = 0
    curr_cell = 0
    append = 1
    while cur_row < num_rows:
        cur_row += 1
        row = worksheet2.cell_value(cur_row, 0)
        roww = unicode(row)
        rr = roww.encode("cp1251")
        rrr = str(rr)
        rw = rrr.replace(".0", "")
        dict_main[append] = rw
        append += 1
    # p = str(dict_main[4])
    # pp = p.decode('cp1251')
    # print pp
    return dict_main

dict_one = dict_one()  # вывод значения функции dict_one
dict_two = {} # создание словаря №2. Конвертация русских символов
for i in dict_one:
    formatedDict = str(dict_one[i])
    frm_dict = formatedDict.decode('cp1251')
    dict_two[i] = frm_dict
    i += 1
# инициализация врменного файла Excel
## в данный файл будет производится первичная сортировка позиций. Возможные идентификаторы сортируются в отдельный столбец.
### Затем будет применена проццедура прогона запросов через веб-сервис Club Pro.
wb = xlwt.Workbook()
ws = wb.add_sheet('TempSheet')
curr_row = 0
for y in dict_two:
    count = sum(1 for i in dict_two[y])
    if count <= 4:
        print "кол-во символов соответствует магазину"
        ws.write (curr_row, 3, dict_two[y])
    elif u'ПР' in dict_two[y]:
        print "строка содержит номер корзины"
        bask = dict_two[y].replace(" ", "")
        ws.write (curr_row, 2, bask)
    else:
        print "строка содержит возможные идентификаторы"
        ws.write (curr_row, 1, dict_two[y])
    y += 1
    curr_row += 1
wb.save('tmp/temp_table.xls')
# формирование словаря 3
def dict_three():
    workbook = xlrd.open_workbook("tmp/temp_table.xls", on_demand=True, formatting_info=True)
    worksheet2 = workbook.sheet_by_name('TempSheet')
    num_rows = worksheet2.nrows - 1
    dict_main = {0: 0}
    cur_row = 0
    append = 1
    while cur_row < num_rows:
        cur_row += 1
        row = worksheet2.cell_value(cur_row, 1)
        roww = unicode(row)
        rr = roww.encode("cp1251")
        rrr = str(rr)
        rw = rrr.replace(".0", "")
        dict_main[append] = rw
        append += 1
    # p = str(dict_main[4])
    # pp = p.decode('cp1251')
    # print pp
    return dict_main

dict_three = dict_three()
del dict_three[0]
dict_3 = {} # создание словаря №3 в качестве контейнера для значений для веб-сервиса
workbook = xlrd.open_workbook("tmp/temp_table.xls", on_demand=True, formatting_info=True)
worksheet2 = workbook.sheet_by_name('TempSheet')
num_rows = worksheet2.nrows - 1
wb = xlwt.Workbook()
ws = wb.add_sheet('Sheet')
for i in dict_three:
    formatedDict = str(dict_three[i])
    frm_dict = formatedDict.decode('cp1251')
    dict_3[i] = frm_dict
    card_type_SM_rus = {'blue' : 300, 'silver' : 301, 'gold' : 302} # dictionary for card type Sportmaster Russia
    webService = "http://clubcards.moscow.sportmaster.ru:80/ClubPro/CardPort?wsdl"
    #webService = "http://172.16.0.37:8001/ClubPro/CardPort?wsdl"
    url_default = "%s" %webService
    client = Client(url_default)
    out = client.service.GetCardIdRequest(card_type_SM_rus["blue"], dict_3[i])
    out_two = client.service.GetCardIdRequest(card_type_SM_rus["silver"], dict_3[i])
    out_three = client.service.GetCardIdRequest(card_type_SM_rus["gold"], dict_3[i])
    out_1 = "%s" %out
    #print out_1
    out_1_1 = str(out_1[22:36])
    out_1_2 = out_1_1.replace('"', "")
    #print("Result code:"+out_1_2)
    out_2 = "%s" %out_two
    out_2_1 = str(out_2[22:36])
    out_2_2 = out_2_1.replace('"', "")
    #print("Result code:"+out_2_2)
    out_3 = "%s" %out_three
    out_3_1 = str(out_3[22:36])
    out_3_2 = out_3_1.replace('"', "")
    #print("Result code:"+out_3_2)
    if "None" in out_1_2:
        pass
    else:
        ws.write(i, 1, out_1_2)
        ws.write(i, 0, 0)
    if "None" in out_2_2:
        pass
    else:
        ws.write(i, 1, out_2_2)
        ws.write(i, 0, 0)
    if "None" in out_3_2:
        pass
    else:
        ws.write(i, 1, out_3_2)
        ws.write(i, 0, 0)
    mob_num_req = client.service.GetClientRegByIdentRequest(133, dict_3[i], 1, 0)
    mb_num = str(mob_num_req)
    mob_num = str(mb_num)
    if "Code = 1" not in mob_num:
        pass
    else:
        print "Mob num is %s" %dict_3[i]
        ws.write(i, 1, dict_3[i])
        ws.write(i, 0, 1)
    # обработка для случаев, если указана ШК-карты
    card_barcode_req = client.service.GetClientRegByIdentRequest(133, dict_3[i], 0, 0)
    card_id = str(card_barcode_req)
    cardId = str(card_id)
    if "Code = 1" not in cardId:
        pass
    else:
        print "Card ID is %s" %dict_3[i]
        ws.write(i, 1, dict_3[i])
        ws.write(i, 0, 0)
    basket = worksheet2.cell_value(i, 2)
    ws.write(i, 2, basket)
    shop = worksheet2.cell_value(i, 3)
    ws.write(i, 3, shop)
    i += 1
wb.save('Output.xls')