from tkinter import *
import pandas as pd
import numpy as np

root = Tk()
root.title('Interface')
#root.config(background = 'blue')
root.geometry("309x200")
root.resizable(width=FALSE,height=FALSE)
Label(root, text = "Data Preprocessing", font = 16).pack()

sheet = pd.read_excel('E:/study/study/books/4th Year 2nd Term (4-2)/Data Mining Lab/Lab2/Data_Sheet.xlsx',sheet_name=0)

def read():
    print('Excell sheet datas:')
    #sheet1 = pd.read_excel('E:/study/study/books/4th Year 2nd Term (4-2)/Data Mining Lab/Lab2/Data_Sheet.xlsx',sheet_name=0)
    print(sheet)

Headphone = (sheet[0:6])
Printer = (sheet[6:12])
Scanner = (sheet[12:18])
Computer = (sheet[18:24])

loopH = len(Headphone.index)
loopP = len(Printer.index)
loopS = len(Scanner.index)
loopC = len(Computer.index)

#Printer updated by meadian
temp1 = []
for i in range(loopP):
    temp1.append(Printer.iloc[i]['Price_AllElectronics'])


a = np.array(temp1)
MeadPrinter_Price_AllElectronics = np.nanmedian(a)


temp2 = []
for i in range(loopP):
    temp2.append(Printer.iloc[i]['Price_Hightech'])

b = np.array(temp2)
MeadPrinter_Price_Hightech = np.nanmedian(b)

PrinterFin1 = Printer.fillna(MeadPrinter_Price_AllElectronics)['Price_AllElectronics']
PrinterFin2 = Printer.fillna(MeadPrinter_Price_Hightech)['Price_Hightech']


mergedPrinter = pd.concat([PrinterFin1, PrinterFin2],axis=1)

mergedPrinter = pd.DataFrame(mergedPrinter, columns=['Item','Price_AllElectronics','Price_Hightech'])
for b in range(loopS):
    mergedPrinter.update(mergedPrinter.iloc[[b]].fillna('Printer '))


#Scanner Updated by Median

temp3 = []
for i in range(loopS):
    temp3.append(Scanner.iloc[i]['Price_AllElectronics'])

c = np.array(temp3)
MeadScanner_Price_AllElectronics = np.nanmedian(c)


temp4 = []
for i in range(loopS):
    temp4.append(Scanner.iloc[i]['Price_Hightech'])


c = np.array(temp4)
MeadScanner_Price_Hightech = np.nanmedian(c)


ScannerFin1 = Scanner.fillna(MeadScanner_Price_AllElectronics)['Price_AllElectronics']
ScannerFin2 = Scanner.fillna(MeadScanner_Price_Hightech)['Price_Hightech']


mergedScanner = pd.concat([ScannerFin1, ScannerFin2],axis=1)

mergedScanner = pd.DataFrame(mergedScanner, columns=['Item','Price_AllElectronics','Price_Hightech'])

for b in range(loopS):
    mergedScanner.update(mergedScanner.iloc[[b]].fillna('Scanner '))

Marge1 = pd.concat([Headphone, mergedPrinter])
Marge2 = pd.concat([mergedScanner, Computer])
FinalOutPut = pd.concat([Marge1, Marge2])
#copy = FinalOutPut

#print(reduce)
def missVal():
    Marge1 = pd.concat([Headphone, mergedPrinter])
    Marge2 = pd.concat([mergedScanner, Computer])
    FinalOutPut = pd.concat([Marge1, Marge2])
    writer = pd.ExcelWriter('miss_val.xlsx', engine='xlsxwriter')
    FinalOutPut.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print('\n')
    print('----------------------------------------------------')
    print('Filling the missing value using Median technique.')
    print(FinalOutPut)


# Headphone Mean Update
addH = 0
for i in range(loopH):
    addH = addH+FinalOutPut.iloc[i]['Price_AllElectronics']

MeanHeadphone_Price_AllElectronics = addH/loopH

for i in range(loopH):
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.Price_AllElectronics[i] = MeanHeadphone_Price_AllElectronics

addHH = 0
for i in range(loopH):
    addHH = addHH+FinalOutPut.iloc[i]['Price_Hightech']

MeanHeadphone_Price_Hightech = addHH/loopH

for i in range(loopH):
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.Price_Hightech[i] = MeanHeadphone_Price_Hightech

# Printer Mean Update
addP = 0
for i in range(6,12):
    addP = addP+FinalOutPut.iloc[i]['Price_AllElectronics']

MeanPrinter_Price_AllElectronics = addP/6

for i in range(6,12):
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.Price_AllElectronics[i] = MeanPrinter_Price_AllElectronics


addPP = 0
for i in range(6,12):
    addPP = addPP+FinalOutPut.iloc[i]['Price_Hightech']

MeanPrinter_Price_Hightech = addPP/loopP
#print(MeanPrinter_Price_Hightech)
for i in range(6,12):
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.Price_Hightech[i] = MeanPrinter_Price_Hightech


# Scanner Mean Update
addS = 0
for i in range(12,18):
    addS = addS+FinalOutPut.iloc[i]['Price_AllElectronics']

MeanScanner_Price_AllElectronics = addS/loopS

for i in range(12,18):
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.Price_AllElectronics[i] = MeanScanner_Price_AllElectronics

addSS = 0
for i in range(12,18):
    addSS = addSS+FinalOutPut.iloc[i]['Price_Hightech']

MeanScanner_Price_Hightech = addHH/loopH

for i in range(12,18):
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.Price_Hightech[i] = MeanScanner_Price_Hightech
    # Setting the new value

# Computer Mean Update

addC = 0
for i in range(loopC):
    addC = addC+Computer.iloc[i]['Price_AllElectronics']

MeanComputer_Price_AllElectronics = addC/loopC

for i in range(18, 24):
    # Setting the new value
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.loc[FinalOutPut.Item == 'Computer', 'Price_AllElectronics'] = [MeanComputer_Price_AllElectronics]


addCC = 0
for i in range(loopC):
    addCC = addCC+Computer.iloc[i]['Price_Hightech']

MeanComputer_Price_Hightech = addCC/loopC

for i in range(18, 24):
    # Setting the new value
    pd.set_option('mode.chained_assignment', None)
    FinalOutPut.loc[FinalOutPut.Item == 'Computer', 'Price_Hightech'] = [MeanComputer_Price_Hightech]

c = FinalOutPut

def rednoise():
    global c
    writer = pd.ExcelWriter('red_noise.xlsx', engine='xlsxwriter')
    c.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    print('\n')
    print('----------------------------------------------------')
    print('Noise reduced data using smoothing by bin mean technique.')
    pd.set_option('mode.chained_assignment', None)

    print(c)

#print(copy)
#copy = FinalOutPut

Marge1 = pd.concat([Headphone, mergedPrinter])
Marge2 = pd.concat([mergedScanner, Computer])
FinalOutPut = pd.concat([Marge1, Marge2])
copy = FinalOutPut
sumAll = 0
sumHigh = 0
sum = 0

for j in range(24):
    sumAll = sumAll+c.Price_AllElectronics[j]
    sumHigh = sumHigh + copy.Price_Hightech[j]
    sum = sum+(copy.Price_AllElectronics[j]*copy.Price_Hightech[j])
#print(sumAll)


test = ((sum/24)-(sumAll/24)*(sumHigh/24))

def rise_fall():
    print('\n')
    print('----------------------------------------------------')
    print('Co-Variance of price is: '+str(test))

    if test > 0:
        print('Price is Rising')
    else:
        print('Price is Falling')

button1 = Button(text = 'Show Data',fg = "red",command = read)
button2 = Button(text = 'Fill Missing Value',fg = "red", command = missVal)
button3 = Button(text = 'Reduce Noise',fg = "red", command = rednoise)
button4 = Button(text = 'Rise/Fall',fg = "red", command = rise_fall)

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = LEFT)
root.mainloop()