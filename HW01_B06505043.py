#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''Turing machine是由英國數學家Alan Turing提出的一種理想計算模型，其由一條無限長的紙帶TAPE、
    一個讀寫頭HEAD、一套控制規則TABLE、一個狀態暫存器組成。TAPE被劃分成連續的小格且每個小格上皆記錄著符號，HEAD在紙
    帶上移動讀取每一格的符號，TABLE根據機器所處的狀態及讀到的符號來確定下一步的動作，並改變狀態暫存器的值，令機器進入
    一個新的狀態，狀態站存器是用來儲存當前Turing machine所處的狀態。
'''
    vonNewmannModelSTR = '''    von Neumann Model分成四個部分有Memory、Arithmetic Logic Unit、Control Unit & Input/Output。
  其與早期的計算機最大的差異性在於他的儲存程式型概念，此概念的目的之一就是讓程式自行增加內容或改變程式指令的記憶體位置。但此概念也是有缺陷的，
  修改程式可能是具有傷害性的，無論無意或設計錯誤。在一個簡單的儲存程式型電腦上，一個設計不良的程式可能會傷害自己、其他程式甚或是作業系統，導致當機。

    '''
    
    if model == "Alen Turing":
        print(turingModelSTR)
    elif model == "von Newmann":
        print(vonNewmannModelSTR)
    else:
        pass
        
        
if __name__ == "__main__":
    modelPrinter("Alen Turing")
    print("=====我是分隔線=====")
    modelPrinter("von Newmann")
