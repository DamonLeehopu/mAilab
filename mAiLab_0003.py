# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:35:41 2017

@author: Damon Lee
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#1. 下載以下四個檔案 [1]：
# train-images-idx3-ubyte.gz: training set images (9912422 bytes)
# train-labels-idx1-ubyte.gz: training set labels (28881 bytes)
# t10k-images-idx3-ubyte.gz: test set images (1648877 bytes)
# t10k-labels-idx1-ubyte.gz: test set labels (4542 bytes) 
# 將其用解壓縮軟體解壓縮之後得到四個檔案，如圖1所示。
# 解壓縮之後的檔，其檔案格式可在 [1] 的下方取得，參考圖2。
#2. 輸出 train-images.idx3-ubyte 檔案中的第一個圖，大小為 28x28。
# 格式以下面 4x4 矩陣為例：
#  00 11 22 33
#  44 55 66 77
#  88 99 AA BB
#  CC DD EE FF
#3. 輸出 train-images.idx3-ubyte 檔案中前十個圖的平均圖，採無條件捨去，大小為 28x28。
#4. 輸出 train-labels.idx1-ubyte 檔案中前十個 labels 的平均，精確度取至小數點以下兩位，#採無條件捨去。
#5. 輸出 train-images.idx3-ubyte 檔案中的第一個圖，大小為 32x32。原圖置中，多出來的地方補0。
#◎ 進階題
#6. 做基本題2時，將圖檔存成BMP格式 [2]。

def get_images(file_name):
    with open(file_name, "rb") as f:
        data=f.read()
    dt = np.dtype(np.uint32).newbyteorder('>')
    #get first 4 variables
    _, n_imgs, rows, cols = np.frombuffer(data[:16], dt, 4)
    #get all pictures' pixel
    all_pic = np.frombuffer(data[16:], np.uint8, n_imgs * rows * cols)
    #reshape to picture form
    all_pic = all_pic.reshape(n_imgs, rows, cols)    
    return all_pic    
    
def get_labels(file_name):    
    with open(file_name, "rb") as f:
        data=f.read()
    dt = np.dtype(np.uint32).newbyteorder('>')
    #get first 2 variables
    _, n_imgs = np.frombuffer(data[:8], dt, 2)
    #get all labels
    all_label = np.frombuffer(data[8:], np.uint8, n_imgs)  
    return all_label 


def form_StrMatrix(img):
    str_pic=[]
    for i in range(len(img)):
        str_pic.append(' '.join(['{:02X}'.format(a) for a in img[i,:]]))
    str_pic = '\n'.join(str_pic)
    return str_pic
    


def basic2():
    
    all_pic=get_images("train-images.idx3-ubyte")
    #show first picture
    plt.imshow(all_pic[0,:,:],cmap='Greys')
    plt.show()  
    
    #tranform picture to str_matrix form
    str_pic=form_StrMatrix(all_pic[0])
    print(str_pic)
        
def basic3():
    all_pic=get_images("train-images.idx3-ubyte")
    #average and 無聊件捨去至整數位
    avg_pic=np.mean(all_pic[0:10,:,:],axis=0)
    '''
    (rows,cols)=avg_pic.shape
    
    avg_pic=avg_pic.flatten()
    for i in range(len(avg_pic)):
        avg_pic[i]=math.floor(avg_pic[i])

    avg_pic=avg_pic.reshape(rows,cols)
    
    '''
    avg_pic=np.floor(avg_pic)
    avg_pic = avg_pic.astype(np.uint8)
    plt.imshow(avg_pic,cmap='Greys')
    plt.show()
    
    #tranform picture to str_matrix form
    str_pic=form_StrMatrix(avg_pic)
    print(str_pic)

def basic4():
    all_label=get_labels("train-labels.idx1-ubyte")
    avg_label=np.floor(np.mean(all_label[0:10])*100)/100
    print(avg_label)
    
def basic5():
    new_pic=np.zeros((32,32),dtype=np.uint8)
    all_pic=get_images("train-images.idx3-ubyte")
    first_pic=all_pic[0]
    for i in range(len(first_pic)):
        for j in range(len(first_pic[0])):
            new_pic[i+2][j+2]=first_pic[i][j]            
    
    
    plt.imshow(new_pic,cmap='Greys')
    plt.show()  
    
    #tranform picture to str_matrix form
    str_pic=form_StrMatrix(new_pic)
    print(str_pic) 
        
def main():    
    basic2()
    basic3()
    basic4()    
    basic5()
    
    
if __name__ == '__main__':
    main() 

'''

￼
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 03 12 12 12 7E 88 AF 1A A6 FF F7 7F 00 00 00 00
00 00 00 00 00 00 00 00 1E 24 5E 9A AA FD FD FD FD FD E1 AC FD F2 C3 40 00 00 00 00
00 00 00 00 00 00 00 31 EE FD FD FD FD FD FD FD FD FB 5D 52 52 38 27 00 00 00 00 00
00 00 00 00 00 00 00 12 DB FD FD FD FD FD C6 B6 F7 F1 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 50 9C 6B FD FD CD 0B 00 2B 9A 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 0E 01 9A FD 5A 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 8B FD BE 02 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 0B BE FD 46 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 23 F1 E1 A0 6C 01 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 51 F0 FD FD 77 19 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D BA FD FD 96 1B 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 10 5D FC FD BB 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F9 FD F9 40 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 2E 82 B7 FD FD CF 02 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 27 94 E5 FD FD FD FA B6 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 18 72 DD FD FD FD FD C9 4E 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 17 42 D5 FD FD FD FD C6 51 02 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 12 AB DB FD FD FD FD C3 50 09 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 37 AC E2 FD FD FD FD F4 85 0B 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 88 FD FD FD D4 87 84 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

￼
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 0E 19 15 08 0F 19 0F 05 00 00 12 13 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 07 1C 2B 4D 3B 41 4A 5C 4D 42 45 35 1C 00 00 00 00
00 00 00 00 06 08 00 00 03 07 17 26 3B 6D 88 6A 64 6D 78 6B 6B 59 31 0F 00 00 00 00
00 00 00 00 0C 10 00 04 17 2B 32 37 5D A2 AC 8A 7B 73 65 79 80 5F 20 00 00 00 00 00
00 00 00 00 16 10 00 01 15 25 41 65 95 B7 A1 6D 5E 78 6E 7F 7D 50 0A 00 00 00 00 00
00 00 00 00 16 10 00 00 08 1A 31 68 95 A6 68 26 38 56 66 84 77 36 00 00 00 00 00 00
00 00 00 04 18 10 00 00 00 21 4A 5B 7D 78 3D 3B 39 44 62 74 6D 35 05 00 00 00 00 00
00 00 00 0C 19 10 00 00 11 2C 3F 46 4C 61 36 40 42 4E 65 6A 65 1E 10 00 00 00 00 00
00 00 00 0F 19 0C 00 0D 2B 31 2C 20 2D 50 58 5D 55 5E 68 62 49 1B 13 00 00 00 00 00
00 00 00 0F 19 06 01 1C 32 32 28 2C 25 6F 9B 90 7A 6A 64 41 25 19 13 00 00 00 00 00
00 00 00 0F 19 08 02 2D 40 4A 3A 4F 69 B1 C8 BC 9D 71 52 1C 1D 19 13 00 00 00 00 00
00 00 00 0F 19 17 1D 4D 65 72 7B 7D 95 B8 B3 BE 89 63 56 2E 19 19 0E 00 00 00 00 00
00 00 00 00 0B 11 22 4A 60 60 4B 39 3A 5D 7E 82 69 6E 7C 5A 22 13 01 00 00 00 00 00
00 00 00 00 00 00 1C 3C 39 19 16 17 1D 56 8A 7D 5A 6E 7A 60 36 19 06 04 04 00 00 00
00 00 00 00 00 00 21 35 26 0A 19 19 24 5D 84 76 49 66 67 3A 10 18 19 19 16 00 00 00
00 00 00 00 00 0A 22 39 20 01 20 2B 44 55 81 7D 73 6B 5B 1F 00 08 12 12 03 00 00 00
00 00 00 00 00 1D 34 4A 30 34 39 4C 6A 5A 79 95 65 68 42 0F 00 00 00 00 00 00 00 00
00 00 00 00 00 29 3A 4B 48 5D 67 76 6A 5F 85 8B 49 3D 25 09 00 00 00 00 00 00 00 00
00 00 00 00 00 16 27 4C 5A 67 7B 7A 5B 48 5F 63 32 2B 1C 0F 00 00 00 00 00 00 00 00
00 00 00 00 05 16 26 35 45 64 71 7A 39 19 3E 4B 22 2A 1D 0F 00 00 00 00 00 00 00 00
00 00 00 00 0D 19 1A 23 2F 3A 37 21 02 00 1A 2E 16 0D 19 0F 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 12 19 11 01 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 01 0E 19 04 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
3.0

￼
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 03 12 12 12 7E 88 AF 1A A6 FF F7 7F 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 1E 24 5E 9A AA FD FD FD FD FD E1 AC FD F2 C3 40 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 31 EE FD FD FD FD FD FD FD FD FB 5D 52 52 38 27 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 12 DB FD FD FD FD FD C6 B6 F7 F1 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 50 9C 6B FD FD CD 0B 00 2B 9A 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 0E 01 9A FD 5A 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 8B FD BE 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 0B BE FD 46 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 23 F1 E1 A0 6C 01 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 51 F0 FD FD 77 19 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2D BA FD FD 96 1B 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 10 5D FC FD BB 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 F9 FD F9 40 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 2E 82 B7 FD FD CF 02 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 27 94 E5 FD FD FD FA B6 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 18 72 DD FD FD FD FD C9 4E 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 17 42 D5 FD FD FD FD C6 51 02 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 12 AB DB FD FD FD FD C3 50 09 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 37 AC E2 FD FD FD FD F4 85 0B 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 88 FD FD FD D4 87 84 10 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
'''    