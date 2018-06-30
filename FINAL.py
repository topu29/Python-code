import cv2
import glob
import numpy as np
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
#import Image


files = sorted(glob.glob("E:/study/study/books/4th Year 2nd Term (4-2)/Data Mining Lab/Lab1/*.jpg"))
a = np.zeros(shape=(15,9))
i = -1;
for im in files:
    image = cv2.imread(im);
    x = np.zeros(shape=(1,9))
    average_color = [image[:, :, i].mean() for i in range(image.shape[-1])]
    median_colorB = np.median(image[:, :, 0])
    median_colorG = np.median(image[:, :, 1])
    median_colorR = np.median(image[:, :, 2])
    rangeB  = np.ptp(image[:, :, 0])
    rangeG  = np.ptp(image[:, :, 1])
    rangeR  = np.ptp(image[:, :, 2])     # B G R
    #print(average_color[0])
    #print(median_colorB)
    #print(median_colorG)
    #print(median_colorR)
    #mean_color = [image[:, :, i].mean() for i in range(image.shape[-1])]
    #median_colorB = np.median(image[:, :, 0])
    x[0][0] = (average_color[0])
    x[0][1] = (average_color[1])
    x[0][2] = (average_color[2])
    x[0][3] = (median_colorB)
    x[0][4] = (median_colorG)
    x[0][5] = (median_colorR)
    x[0][6] = (rangeB)
    x[0][7] = (rangeG)
    x[0][8] = (rangeR)
    i += 1
    a[i] = x
    #print(a[i])


#print(a[i])
#mean_color = [image[:, :, i].mean() for i in range(image.shape[-1])]
#median_colorB = np.median(image[:, :, 0])
meanB = np.zeros(shape=(15,15))
meanG = np.zeros(shape=(15,15))
meanR = np.zeros(shape=(15,15))
medB  = np.zeros(shape=(15,15))
medG  = np.zeros(shape=(15,15))
medR  = np.zeros(shape=(15,15))
ranB  = np.zeros(shape=(15,15))
ranG  = np.zeros(shape=(15,15))
ranR  = np.zeros(shape=(15,15))

row = a.shape[0]
col = a.shape[1]


data1 = a[:,0]
data2 = a[:,1]
data3 = a[:,2]
data4 = a[:,3]
data5 = a[:,4]
data6 = a[:,5]
data7 = a[:,6]
data8 = a[:,7]
data9 = a[:,8]
#print("data 1")
#print(data1)


for i in range(row):
    temp1 = np.zeros(shape=(1, 15))
    temp2 = np.zeros(shape=(1, 15))
    temp3 = np.zeros(shape=(1, 15))
    temp4 = np.zeros(shape=(1, 15))
    temp5 = np.zeros(shape=(1, 15))
    temp6 = np.zeros(shape=(1, 15))
    temp7 = np.zeros(shape=(1, 15))
    temp8 = np.zeros(shape=(1, 15))
    temp9 = np.zeros(shape=(1, 15))
    for j in range( col):
        temp1[0][j] = abs((data1[i]) - (data1[j]))
        temp2[0][j] = abs((data2[i]) - (data2[j]))
        temp3[0][j] = abs((data3[i]) - (data3[j]))
        temp4[0][j] = abs((data4[i]) - (data4[j]))
        temp5[0][j] = abs((data5[i]) - (data5[j]))
        temp6[0][j] = abs((data6[i]) - (data6[j]))
        temp7[0][j] = abs((data7[i]) - (data7[j]))
        temp8[0][j] = abs((data8[i]) - (data8[j]))
        temp9[0][j] = abs((data9[i]) - (data9[j]))

    meanB[i] = temp1
    meanG[i] = temp2
    meanR[i] = temp3
    medB[i] = temp4
    medG[i] = temp5
    medR[i] = temp6
    ranB[i] = temp7
    ranG[i] = temp8
    ranR[i] = temp9

    # city block distance

dis_mat = np.zeros(shape=(15,15))

for i in range(15):

    for j in range(15):
        dis_mat[i][j] = (meanB[i][j] + meanG[i][j] + meanR[i][j] + medB[i][j] + medG[i][j]+medR[i][j] + ranB[i][j]+ranG[i][j]+ranR[i][j]) / 9




print("Most Dissimilar two Image:")
ind = np.unravel_index(np.argmax(dis_mat, axis=None), dis_mat.shape)


#image = cv2.imread("E:/study/study/books/4th Year 2nd Term (4-2)/Data Mining Lab/Lab1/30%d.jpg" % (ind[i]))
#plt.subplot("12%d"%i)
#plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
#plt.title("Image: "+"30%d"%ind[i])
#plt.xticks([]) , plt.yticks([])
#plt.axis('off')

#ind1 = np.unravel_index(np.argmin(sis_mat, axis=None), sis_mat.shape)

print(ind)
#print(x)

for i in range(2):
    image = cv2.imread("E:/study/study/books/4th Year 2nd Term (4-2)/Data Mining Lab/Lab1/30%d.jpg" % (ind[i]))
    plt.subplot("12%d"%i)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Image: "+"30%d"%ind[i])
    plt.xticks([]) , plt.yticks([])
    plt.axis('off')

plt.show()