__author__ = '@antonyLash'
# -*- coding: utf-8 -*-
# -*- coding: cp1251 -*-
import logging
import os
import shutil
from math import *
import time
import sys

import xlwt
import xlrd
from suds.client import Client
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtGui import QIcon
from PyQt4.QtGui import QPixmap

from csv_generatorGUI_v_1 import Ui_MainWindow
from DialogBox_checkStatus import Ui_dialogBoxStatusCheck

class Main(QtGui.QMainWindow):

    # MainWindow implementation
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        if not os.path.exists('tmp'):
            os.makedirs('tmp')
        # default param block
        self.ui.progressBar.reset()
        self.ui.sm_ua.setEnabled(False)
        self.ui.sm_china.setEnabled(False)
        self.ui.sm_kz.setEnabled(False)
        self.ui.os_china.setEnabled(False)
        self.ui.os_kz.setEnabled(False)
        self.ui.os_rus.setEnabled(False)
        self.ui.os_ua.setEnabled(False)
        self.ui.sm_rus.setChecked(True)
        self.ui.pushButton.setEnabled(False)
        self.ui.saveAsBtn.setEnabled(False)
        self.ui.outputPath.setEnabled(False)

        ### implementation block
        self.ui.selectIn.clicked.connect(self.selectFile)
        self.ui.saveAsBtn.clicked.connect(self.saveFile)
        self.ui.pushButton.clicked.connect(self.Convertation_btn)
        self.ui.aboutApp.triggered.connect(self.AboutUs)
        ### implementation block end

    # implementation for select input file dialog box
    def selectFile(self):
        self.ui.progressBar.reset()
        fname = QtGui.QFileDialog.getOpenFileName(self, u'Выберите Excel файл')
        if fname.contains(".xls"):
            self.ui.inputPath.setText(fname)
            self.ui.saveAsBtn.setEnabled(True)
            self.ui.outputPath.setEnabled(True)
        else:
            self.ui.inputPath.setText(u'Некорректный формат файла!')
        # check if the file was selected or not.
        importPath = self.ui.inputPath.text()
        print unicode(importPath)
        if importPath == u'Некорректный формат файла!':
            self.ui.saveAsBtn.setEnabled(False)
            self.ui.outputPath.setEnabled(False)
        inputText = self.ui.inputPath.text()
        return inputText

    def saveFile(self):
        self.ui.progressBar.reset()
        fname = QtGui.QFileDialog.getSaveFileName(self, u'Сохранить как')
        self.ui.outputPath.setText(fname)
        saveFileTxt = self.ui.outputPath.text()
        importPath = self.ui.inputPath.text()
        if saveFileTxt != "" and importPath != "":
            self.ui.pushButton.setEnabled(True)
            self.ui.outputPath.setText(fname+".xls")
        else:
            self.ui.pushButton.setEnabled(False)
            self.ui.outputPath.setText(u'Входные данные не заданы!')
        outPath = self.ui.outputPath.text()
        return outPath

    def Convertation_btn(self):
        pb_int = 0
        pb_i = 0
        pb_max = 100
        self.ui.progressBar.setMaximum(pb_int)
        self.ui.progressBar.setMaximum(pb_max)
        self.ui.progressBar.setValue(pb_i)
        def ColumnOne():
            # формирование словаря №1
            def dict_one():
                inputText = self.ui.inputPath.text()
                workbook = xlrd.open_workbook(inputText, on_demand=True, formatting_info=True)
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
            self.ui.progressBar.setValue(pb_i+5)
            dict_one = dict_one()  # вывод значения функции dict_one
            dict_two = {} # создание словаря №2. Конвертация русских символов
            for i in dict_one:
                formatedDict = str(dict_one[i])
                frm_dict = formatedDict.decode('cp1251')
                dict_two[i] = frm_dict
                i += 1
            # инициализация врменного файла Excel
            ## в данный файл будет производится первичная сортировка позиций. Возможные идентификаторы сортируются в отдельный столбец.
            ### Затем будет применена процедура прогона запросов через веб-сервис Club Pro.
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
            self.ui.progressBar.setValue(pb_i+10)
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
            self.ui.progressBar.setValue(pb_i+15)
            dict_three = dict_three()
            del dict_three[0]
            dict_3 = {} # создание словаря №3 в качестве контейнера для значений для веб-сервиса
            workbook = xlrd.open_workbook("tmp/temp_table.xls", on_demand=True, formatting_info=True)
            worksheet2 = workbook.sheet_by_name('TempSheet')
            num_rows = worksheet2.nrows - 1
            self.ui.progressBar.setValue(pb_i+20)
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
            self.ui.progressBar.setValue(pb_i+25)
            wb.save('tmp/Output.xls')
        col_one = ColumnOne()
        def ColumnTwo():
            # формирование словаря №1
            def dict_one():
                inputText = self.ui.inputPath.text()
                workbook = xlrd.open_workbook(inputText, on_demand=True, formatting_info=True)
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
            self.ui.progressBar.setValue(pb_i+35)
            dict_one = dict_one()  # вывод значения функции dict_one
            dict_two = {} # создание словаря №2. Конвертация русских символов
            for i in dict_one:
                formatedDict = str(dict_one[i])
                frm_dict = formatedDict.decode('cp1251')
                dict_two[i] = frm_dict
                i += 1
            # инициализация врменного файла Excel
            ## в данный файл будет производится первичная сортировка позиций. Возможные идентификаторы сортируются в отдельный столбец.
            ### Затем будет применена процедура прогона запросов через веб-сервис Club Pro.
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
            wb.save('tmp/temp_table2.xls')
            self.ui.progressBar.setValue(pb_i+40)
            # формирование словаря 3
            def dict_three():
                workbook = xlrd.open_workbook("tmp/temp_table2.xls", on_demand=True, formatting_info=True)
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
            self.ui.progressBar.setValue(pb_i+45)
            dict_three = dict_three()
            del dict_three[0]
            dict_3 = {} # создание словаря №3 в качестве контейнера для значений для веб-сервиса
            workbook = xlrd.open_workbook("tmp/temp_table2.xls", on_demand=True, formatting_info=True)
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
            self.ui.progressBar.setValue(pb_i+50)
            wb.save('tmp/Output2.xls')
        col_two = ColumnTwo()
        def ColumnTree():
            # формирование словаря №1
            def dict_one():
                inputText = self.ui.inputPath.text()
                workbook = xlrd.open_workbook(inputText, on_demand=True, formatting_info=True)
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
                append = 1
                while cur_row < num_rows:
                    cur_row += 1
                    row = worksheet2.cell_value(cur_row, 2)
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
            self.ui.progressBar.setValue(pb_i+65)
            dict_one = dict_one()  # вывод значения функции dict_one
            dict_two = {} # создание словаря №2. Конвертация русских символов
            for i in dict_one:
                formatedDict = str(dict_one[i])
                frm_dict = formatedDict.decode('cp1251')
                dict_two[i] = frm_dict
                i += 1
            # инициализация врменного файла Excel
            ## в данный файл будет производится первичная сортировка позиций. Возможные идентификаторы сортируются в отдельный столбец.
            ### Затем будет применена процедура прогона запросов через веб-сервис Club Pro.
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
            self.ui.progressBar.setValue(pb_i+75)
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
            self.ui.progressBar.setValue(pb_i+85)
            wb.save('tmp/Output3.xls')
        col_tree = ColumnTree()
        outPath = self.ui.outputPath.text()
        inputText = self.ui.inputPath.text()
        workbook0 = xlrd.open_workbook(inputText, on_demand=True, formatting_info=True)
        worksheet0 = workbook0.sheet_by_name('Sheet1')
        num_rows0 = worksheet0.nrows - 1
        workbook = xlrd.open_workbook("tmp/Output.xls", on_demand=True, formatting_info=True)
        worksheet = workbook.sheet_by_name('Sheet')

        workbook2 = xlrd.open_workbook("tmp/Output2.xls", on_demand=True, formatting_info=True)
        worksheet2 = workbook2.sheet_by_name('Sheet')

        workbook3 = xlrd.open_workbook("tmp/Output3.xls", on_demand=True, formatting_info=True)
        worksheet3 = workbook3.sheet_by_name('Sheet')

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Sheet')

        curr_row = 0
        while curr_row < num_rows0:
            curr_row += 1
            # формирование массива из первого столбца
            col1 = worksheet.cell_value(curr_row, 0)
            col1_1 = worksheet2.cell_value(curr_row, 0)
            col1_2 = worksheet3.cell_value(curr_row, 0)
            if worksheet.cell_type(curr_row, 0) == 0 or worksheet.cell_type(curr_row, 0) == 6:
                pass
            else:
                ws.write(curr_row, 0, col1)

            if worksheet2.cell_type(curr_row, 0) == 0 or worksheet2.cell_type(curr_row, 0) == 6:
                pass
            else:
                ws.write(curr_row, 0, col1_1)

            if worksheet3.cell_type(curr_row, 0) == 0 or worksheet3.cell_type(curr_row, 0) == 6:
                pass
            else:
                ws.write(curr_row, 0, col1_2)

            # формирование массива из второго столбца
            col2 = worksheet.cell_value(curr_row, 1)
            col2_1 = worksheet2.cell_value(curr_row, 1)
            col2_2 = worksheet3.cell_value(curr_row, 1)
            if worksheet.cell_type(curr_row, 1) == 0 or worksheet.cell_type(curr_row, 1) == 6:
                pass
            else:
                ws.write(curr_row, 1, col2)

            if worksheet2.cell_type(curr_row, 1) == 0 or worksheet2.cell_type(curr_row, 1) == 0:
                pass
            else:
                ws.write(curr_row, 1, col2_1)

            if worksheet3.cell_type(curr_row, 1) == 0 or worksheet3.cell_type(curr_row, 1) == 0:
                pass
            else:
                ws.write(curr_row, 1, col2_2)


            # формирование массива из третьего столбца
            col3 = worksheet.cell_value(curr_row, 2)
            col3_1 = worksheet2.cell_value(curr_row, 2)
            col3_2 = worksheet3.cell_value(curr_row, 2)
            if worksheet.cell_type(curr_row, 2) == 0 or worksheet.cell_type(curr_row, 2) == 6:
                pass
            else:
                ws.write(curr_row, 2, col3)

            if worksheet2.cell_type(curr_row, 2) == 0 or worksheet2.cell_type(curr_row, 2) == 6:
                pass
            else:
                ws.write(curr_row, 2, col3_1)

            if worksheet3.cell_type(curr_row, 2) == 0 or worksheet3.cell_type(curr_row, 2) == 6:
                pass
            else:
                ws.write(curr_row, 2, col3_2)


            # формирование массива из четвертого столбца
            col4 = worksheet.cell_value(curr_row, 3)
            col4_1 = worksheet2.cell_value(curr_row, 3)
            col4_2 = worksheet3.cell_value(curr_row, 3)
            if worksheet.cell_type(curr_row, 3) == 0 or worksheet.cell_type(curr_row, 3) == 6:
                pass
            else:
                ws.write(curr_row, 3, col4)

            if worksheet2.cell_type(curr_row, 3) == 0 or worksheet2.cell_type(curr_row, 3) == 6:
                pass
            else:
                ws.write(curr_row, 3, col4_1)

            if worksheet3.cell_type(curr_row, 3) == 0 or worksheet3.cell_type(curr_row, 3) == 6:
                pass
            else:
                ws.write(curr_row, 3, col4_2)
        self.ui.progressBar.setValue(pb_i+95)
        wb.save("%s" %outPath)
        #os.remove('tmp/Output.xls')
        #os.remove('tmp/Output2.xls')
        #os.remove('tmp/Output3.xls')
        #os.remove('tmp/temp_table.xls')
        #os.remove('tmp/temp_table2.xls')
        #shutil.rmtree('tmp')
        self.dialog1 = QtGui.QMainWindow()
        self.uiDialog1 = Ui_dialogBoxStatusCheck()
        self.uiDialog1.setupUi(self.dialog1)
        self.dialog1.setWindowTitle(u'Club Pro Auchers') # Automatic Check Relation Setup
        self.label1 = QtGui.QLabel(self.dialog1)
        self.label1.setGeometry(QtCore.QRect(55, 15, 200, 100))
        self.label1.setText(u'Конвертация завершена успешно')
        self.uiDialog1.okBtn.setText(u'OK')
        self.uiDialog1.labelError.setText("")
        self.dialog1.show()
        self.uiDialog1.okBtn.clicked.connect(self.dialog1.close)
        self.ui.progressBar.setValue(pb_i+100)
        print "Convertation was done!"

    def AboutUs(self):
        if self.ui.aboutApp.triggered:
            self.dialog = QtGui.QMainWindow()
            self.uiDialog = Ui_dialogBoxStatusCheck()
            self.uiDialog.setupUi(self.dialog)
            self.dialog.setWindowTitle(u'О программе')
            self.label = QtGui.QLabel(self.dialog)
            self.label.setGeometry(QtCore.QRect(27, 15, 400, 120))
            self.label.setText(u'                      Над проектом работал'+'\n'+'\n'+u'Разработчик: Лашов Антон Владимирович'+'\n'+'\n'+u'                                Контакты'+'\n'+u'e-mail: Alashov@sportmaster.ru'+'\n'+'mob: +7-925-287-34-74'+'\n'+u'ГК "Спортмастер" 2014(c)')
            self.uiDialog.okBtn.setText(u'OK')
            self.uiDialog.labelError.setText("")
            self.dialog.show()
            self.uiDialog.okBtn.clicked.connect(self.dialog.close)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = Main()
    app.processEvents()
    window.show()
    sys.exit(app.exec_())