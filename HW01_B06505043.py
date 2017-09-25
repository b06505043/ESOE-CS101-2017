#!/usr/bin/env python3
# -*- coding:utf-8 -*-


#Chapter 01

#第 01 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 Turing Model，並寫在以下第 15 行處。

#第 02 題
#請和同組同學討論後，用平白易懂的描述，在 300 個字符內說明何為 von Newmann Model，並寫在以下第 20 行處。


def modelPrinter(model):
    turingModelSTR = '''Turing machine是一種抽象的數學計算模型，由四個部分組成: 1.TAPE:是一條可向右伸展的無限長紙帶，且紙帶被劃分為連續的小格，每一格上都註記著符號。
    2.HEAD:一個讀寫頭，可在TAPE上左右移動讀取每格上的符號。3.TABLE:一套控制的規則，會根據當前機器的狀態及讀寫頭所指的格子上的符號來確定讀寫頭下一步的動作，並改變狀態暫
    存器的值，令機器進入一個新的狀態。 4.狀態暫存器:用來儲存Turing machine當前的狀態。
    '''
    
    vonNewmannModelSTR = '''vonNewmann Model與Turing Model的概念相似，但vonNewmann Model分為四個部分:算術邏輯單元(arithmetic logic unit)
    、記憶體(memory)、控制單元(control unit)及輸入與輸出(input/output)。且與Turing machine最大的不同是可以儲存程式並在程式執行時自我修改程式
    的運算內容。

    
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
