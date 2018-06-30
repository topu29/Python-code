#from PIL import Image,ImageTk
import pandas as pd
from tkinter import *
from sklearn.neighbors import KNeighborsClassifier
import cv2
import glob
from tkinter import filedialog
import os
import numpy as np

root = Tk()
root.title('User Interface')

root.geometry("1000x300")
root.resizable(width=FALSE,height=FALSE)
Label(root, text = "KNN Classifier",font = 16).pack()


concat_dir = ''
def browse_botton():
    global concat_dir
    filename = filedialog.askdirectory(parent = root, initialdir = '/',title = 'browse folder')
    concat_dir = filename + '/*.jpg'

X = []
def xfeatStoreXL():
    global X
    global concat_dir
    #print(concat_dir)
    for filename in glob.glob(concat_dir):
        #print(filename)
        im = cv2.imread(filename,0)
        surf = cv2.xfeatures2d.SURF_create()
        f, des = surf.detectAndCompute(im, None)
        des = des.flatten()
        des = des[0:9000]
        # s = des.shape
        # print(s[0])
        # print(filename)
        # if(s[0]<minimum):
        #    minimum = s[0]
        X.append(des)
    df = pd.DataFrame(X)
    writer = pd.ExcelWriter('Extracted_feature.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
sheet = pd.read_excel('E:/study/study/books/4th Year 2nd Term (4-2)/python practise/Extracted_feature.xlsx',sheet_name=0)
model = KNeighborsClassifier(n_neighbors=3)
Y=[]
for i in range(150):
    if(i<50):
        Y.append(1)
    if(i>=50 and i<100):
        Y.append(2)
    if(i>= 100):
        Y.append(3)
def load_feat():
    global neigh
    global X
    global Y
    global sheet
    excelpath = filedialog.askopenfilename(initialdir="/", title="Select Feature data",filetypes=[("Excel File", "*.xlsx")])

    model.fit(sheet, Y)

filePath = ''
def browse_file():
    global filePath
    filePath = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Testing Image",filetypes=[("Image Files", "*.jpg")])
    #T.insert(END, "")


T = Text(root, height=1, width=30)
T.pack(side = LEFT)
T.insert(END, "")



def class_name():
    global Y
    global filePath
    global neigh
    global test
    global test1
    test = cv2.imread(filePath,0) # testing image
    test1 = cv2.imread(filePath)
    surf = cv2.xfeatures2d.SURF_create()  # surf object creation
    f, des = surf.detectAndCompute(test, None)  # surf feature extract
    des = des.flatten()
    # print(des.shape)
    des = des[0:9000]
    result = model.predict([des])
    if (result[0] == 1):
        T.insert(END, "Bus")

    if (result[0] == 2):
        T.insert(END, "Dinosaur")

    if (result[0] == 3):
        T.insert(END, "Flower")




def show():

    global test1

    cv2.imshow('Display',test1)  # Display the picture
    cv2.waitKey(0)  # wait for closing
    cv2.destroyAllWindows()


button1 = Button(text = 'Browse\n(Training Image Folder)',command = browse_botton )
button2 = Button(text = 'Extract feature' , command = xfeatStoreXL)
button3 = Button(text = 'Load Feature \nDataset',command =  load_feat)
button4 = Button(text ='Input \nImage', command = browse_file )
button5 = Button(text = 'Show  \nClass',command  = class_name)
button6 = Button(text = 'Show  \nImage', command = show)



button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = LEFT)
button5.pack(side = LEFT)
button6.pack(side = LEFT)


root.mainloop()