# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 14:07:38 2017

@author: Damon Lee
"""

import numpy as np
import matplotlib.pyplot as plt

#◎ 基本題
#1. 將作業3 [1] 的前五個圖，分別跑 max pooling 與 average pooling [2]，共輸出10個圖，以圖示呈現 [3], [4]，並請反白處理 [4]。


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
    
def make_avg_pooling(pic):
    rows,cols=pic.shape
    new_pic=np.zeros([rows/2,cols/2])
    for i in range(len(new_pic)):
        for j in range(len(new_pic[0])):
            new_pic[i][j]=np.round(np.mean(pic[i*2:i*2+2,j*2:j*2+2]))
            
    return new_pic        

    
    
    
def make_max_pooling(pic):
    rows,cols=pic.shape
    new_pic=np.zeros([rows/2,cols/2])
    for i in range(len(new_pic)):
        for j in range(len(new_pic[0])):
            new_pic[i][j]=np.amax(pic[i*2:i*2+2,j*2:j*2+2])
            
    return new_pic   
        
    
def main():    
    all_pic=get_images('train-images.idx3-ubyte')
    all_pic=all_pic.astype(np.uint8)
    for pic in all_pic[0:5]:
        avg_pooling_pic=make_avg_pooling(pic)
        max_pooling_pic=make_max_pooling(pic)
        plt.imshow(avg_pooling_pic,cmap='Greys')
        plt.show()
        plt.imshow(max_pooling_pic,cmap='Greys')
        plt.show()     
    
if __name__ == '__main__':
    main()     