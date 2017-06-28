# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 13:12:18 2017

@author: Damon Lee
"""
import numpy as np
import matplotlib.pyplot as plt

#◎ 基本題
#1. 將作業3 [1] 的前五個圖，增大至30x30後，分別跑Gx與Gy [2]，共輸出10個圖，以圖示呈現 [3], [4]，並請反白處理 [4]。
#
#Gx： 
#-1 0 +1
#-2 0 +2
#-1 0 +1

#Gy：
#+1 +2 +1
#0 0 0
#-1 -2 -1

#2. 將作業3 [1] 的第一個圖，分別增大至 32x32、34x34、36x36，然後跑5x5、7x7、9x9的filter [5]，輸出其值為 28x28 的矩陣，格式以下面 4x4 矩陣為例：

#00 11 22 33
#44 55 66 77
#88 99 AA BB
#CC DD EE FF

#◎ 進階題
#3. 試以文字說明 Gx 為何可以達到 edge detection 的功能。

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
    

def make_pad(img,num):    
    
    new_img=np.lib.pad(img,(num,num),'constant',constant_values=(0, 0))
    return new_img
    
def run_filter(Filter,img):    
    new_img=np.zeros([28,28])
    for i in range(len(new_img)):
        for j in range(len(new_img[0])):
            new_img[i][j]=np.sum(np.multiply(Filter,img[i:i+len(Filter),j:j+len(Filter)]))
    return new_img

def basic1():    
    all_pic=get_images('train-images.idx3-ubyte')
    pic=[]
    #generate 30*30 image
    for i in range(5):
        pic.append(make_pad(all_pic[i],1))
    # run Gx and Gy
    Gx=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    Gy=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
    img_Gx=[]
    img_Gy=[]
    for i in range(5):
        img_Gx.append(run_filter(Gx,pic[i]))
        img_Gy.append(run_filter(Gy,pic[i]))
    
    #show handled pictures    
    for i in range(5): 
        plt.subplot(1, 5, i + 1)
        plt.imshow(img_Gx[i],cmap='Greys')
        plt.axis('off')
    plt.show()
    
    for i in range(5): 
        plt.subplot(1, 5, i + 1)
        plt.imshow(img_Gy[i],cmap='Greys')
        plt.axis('off')
    plt.show()


def basic2():    
    all_pic=get_images('train-images.idx3-ubyte')
    pic=all_pic[0]
    #generate 32*32,34*34, 36*36 picture
    pic_32= make_pad(pic,2)
    pic_34= make_pad(pic,3)
    pic_36= make_pad(pic,4)
    
    filter_55=np.array([[2,1,0,-1,-2],[3,2,0,-2,-3],[4,3,0,-3,-4],[3,2,0,-2,-3],[2,1,0,-1,-2]])
    filter_77=np.array([[3,2,1,0,-1,-2,-3],[4,3,2,0,-2,-3,-4],[5,4,3,0,-3,-4,-5],[6,5,4,0,-4,-5,-6],[5,4,3,0,-3,-4,-5],[4,3,2,0,-2,-3,-4],[3,2,1,0,-1,-2,-3]])
    filter_99=np.array([[4,3,2,1,0,-1,-2,-3,-4],[5,4,3,2,0,-2,-3,-4,-5],[6,5,4,3,0,-3,-4,-5,-6],[7,6,5,4,0,-4,-5,-6,-7],[8,7,6,5,0,-5,-6,-7,-8],[7,6,5,4,0,-4,-5,-6,-7],[6,5,4,3,0,-3,-4,-5,-6],[5,4,3,2,0,-2,-3,-4,-5],[4,3,2,1,0,-1,-2,-3,-4]])
    
    
    
    ans_pic_32=run_filter(filter_55,pic_32)
    ans_pic_34=run_filter(filter_77,pic_34)
    ans_pic_36=run_filter(filter_99,pic_36)
    
    plt.imshow(ans_pic_32,cmap='Greys')
    plt.show()
    ans_pic_32=ans_pic_32.astype(np.uint8)
    print(form_StrMatrix(ans_pic_32))
    plt.imshow(ans_pic_34,cmap='Greys')
    plt.show()
    ans_pic_34=ans_pic_34.astype(np.uint8)
    print(form_StrMatrix(ans_pic_34))
    plt.imshow(ans_pic_36,cmap='Greys')
    plt.show()
    ans_pic_36=ans_pic_36.astype(np.uint8)
    print(form_StrMatrix(ans_pic_36))
    
    
        
def main():    
    basic1()
    basic2()
    
    
if __name__ == '__main__':
    main()     
    
'''    
￼

￼

￼
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 FA D9 CA CD 0A A8 50 BF 1E 1B 8B E5 CC F5 6D FE 00 00
00 00 00 00 00 00 C4 9A 20 8C 69 C6 05 93 E9 C6 75 44 B5 A7 54 41 9E 92 A9 FD 00 00
00 00 00 00 00 9E 99 70 D8 0B 46 8C DF BC 1B E8 C0 6E 4B B9 85 00 4F D4 70 BC 00 00
00 00 00 00 00 49 94 6E A8 5E F4 7C 6F EC 96 B3 E2 C2 89 C6 DA D9 62 F2 24 7D 00 00
00 00 00 00 00 06 06 65 07 3B 0D C2 BC 2D 22 B8 82 B1 1E 38 7F 66 17 A6 D2 BE 00 00
00 00 00 00 00 25 06 B2 53 96 6E B7 FD B4 AB B0 70 12 08 EB CC 5E 12 9D 3B 80 00 00
00 00 00 00 00 68 FE E1 CE 29 11 31 01 E6 B2 BE 80 87 40 CC 86 CF DC 97 4E 00 00 00
00 00 00 00 00 DC 48 7F 74 B9 C7 39 C8 24 51 26 D0 B9 94 B0 00 00 00 00 00 00 00 00
00 00 00 00 00 00 60 4E 6F CE 0B C9 69 E4 3D 2A B7 D7 C9 36 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 E4 F0 FE EB 4F 32 16 D7 19 33 96 B7 0A 32 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 C9 9F F4 F0 F0 B8 CA B3 28 74 2B 92 36 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 EA 10 EB C3 C6 13 4F B4 0D 55 42 11 C7 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 BA 08 27 8C 17 C5 C3 EC 71 EC 54 CF 80 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 5E EC 1C 5B 9B B9 38 3B 6B 01 48 C4 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 B2 B1 BE 95 D7 B1 B0 A7 31 7A D2 E8 06 00 00 00 00 00
00 00 00 00 00 00 00 00 D0 04 5F 37 1C A5 40 2E D7 A3 E1 0A F5 45 C8 00 00 00 00 00
00 00 00 00 00 00 D2 65 CC C2 62 1C 11 7D 73 57 89 F5 F1 79 7C 7B 86 00 00 00 00 00
00 00 00 00 DC 98 5A 49 75 B7 55 A6 B4 09 62 01 28 02 63 F4 5B C2 04 00 00 00 00 00
00 00 92 71 5A 36 E0 6D 03 24 01 D6 9B E6 60 A1 8D 0C 14 F3 94 6C 00 00 00 00 00 00
00 00 4B 0C C3 62 C2 A9 42 28 BD 00 76 4C F9 CE 6C C1 BA E6 9C 00 00 00 00 00 00 00
00 00 8C A4 4D 05 FC FB 9A 99 78 DD 86 33 2F B7 C0 F8 A4 04 00 00 00 00 00 00 00 00
00 00 3B 02 F3 F8 7B 67 CD F9 EB E2 9D BB 59 F7 A9 12 00 00 00 00 00 00 00 00 00 00
00 00 FA 6A 9F 7A 3F F7 21 79 63 F9 8F 9D 15 16 00 00 00 00 00 00 00 00 00 00 00 00
00 00 F0 7E 09 91 68 15 68 2A 1F 92 18 20 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00

￼
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 F7 C4 A3 94 53 72 A4 38 03 57 B0 A6 F2 1A E7 6A E3 7D 00
00 00 00 00 00 A6 58 80 52 82 2A E1 32 BE A0 71 48 F4 22 71 AF A0 0A 21 7B 22 BC 00
00 00 00 00 6D 5C 12 01 79 5D 94 89 21 CA ED 90 DD 8B 25 C6 97 06 77 FC DB 10 7B 00
00 00 00 00 06 6A F5 AD BB 0F A0 8E 53 AD AD 4B C4 D6 F4 73 26 60 EE FB A4 B0 3A 00
00 00 00 00 C3 50 39 87 8B A0 AC 92 F0 27 EF 59 04 C5 9E C4 E9 C8 E5 C2 83 64 FB 00
00 00 00 00 80 12 5F F4 1A 04 69 B1 17 02 27 53 D3 C4 65 D3 4E 22 26 25 78 12 3C 00
00 00 00 00 9F 12 D9 41 C9 9F CE BB EA 52 83 2A 92 DD FA 9A 1D C8 AF 26 AF 72 7D 00
00 00 00 00 E2 EC 27 38 37 89 6F 09 7B AB 3F E1 F3 0E 55 FA 40 75 5E DC F1 65 C0 00
00 00 00 00 25 A2 B3 BD 55 A0 AF 6E 4C 4D 6A CF 46 48 20 47 40 E6 D2 8D F6 75 00 00
00 00 00 00 CA 0B 9B D7 0E 81 E9 27 4C 60 20 4E 7E 8B E4 F2 D6 4B 00 00 00 00 00 00
00 00 00 00 00 10 54 09 17 B9 C7 AD 53 73 72 FD DA CE A6 E7 38 5C 51 00 00 00 00 00
00 00 00 00 00 00 D6 E1 BF 8B 73 75 E6 57 50 38 DB 35 F8 C8 52 93 9D 00 00 00 00 00
00 00 00 00 00 00 00 00 33 2B D6 4E 24 A9 F3 59 BE 0A 23 7D 21 3E DE C0 00 00 00 00
00 00 00 00 00 00 00 00 DF 24 C0 4D 6A 21 F0 7E 3E 56 CA 39 A1 5B 5E 06 00 00 00 00
00 00 00 00 00 00 00 00 00 22 99 0E 6A A8 7F F9 27 EB BE 55 6F A7 2A 48 00 00 00 00
00 00 00 00 00 00 00 B8 7A D1 25 A0 C0 21 50 88 FA 15 6D CC D6 C3 14 8A 00 00 00 00
00 00 00 00 00 BB 0C 86 0D 94 93 62 70 9E 08 60 72 FA 5D E0 81 A5 8C 4C 00 00 00 00
00 00 00 CA DB AB 5B 86 50 C7 62 04 99 09 21 9B DD A4 B8 F9 9D EF 2C 0A 00 00 00 00
00 5B 8E 83 B7 60 AB 6E 6A 99 C8 62 8B 8C 56 D0 0E 1E 0C FB A8 1C 3B C8 00 00 00 00
00 8C A4 33 81 21 8E 84 72 97 80 60 DD B6 70 11 41 C9 45 E8 3F 27 49 06 00 00 00 00
00 CD 3C DA 42 B5 7D 78 4F 1E A6 1D 27 42 74 18 87 92 13 73 B9 92 22 00 00 00 00 00
00 0E D4 A5 7D 79 72 F2 A0 B1 8F 24 B8 32 F9 94 68 3C F6 21 FF EA 00 00 00 00 00 00
00 BD 32 FA CE 87 8F 00 B3 2F 5F 56 0D DC 38 3B FA 2F 1A F7 06 00 00 00 00 00 00 00
00 7C 9A 53 0D 4F ED 6C 57 9D 5C 9B 10 3A 70 02 1E 02 1B 00 00 00 00 00 00 00 00 00
00 3B 02 D0 B4 33 2C B5 FD 84 2D 40 A2 A4 31 A5 21 00 00 00 00 00 00 00 00 00 00 00
00 68 F9 87 12 15 D3 21 2F 21 16 0E AD AC 30 00 00 00 00 00 00 00 00 00 00 00 00 00

￼
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 F4 AF 7C 5B 9C 33 B6 3C AC 4F C3 FC 9E 12 D6 4F 02 DF 59 FC
00 00 00 00 88 16 E0 18 9B 34 DC 93 40 B2 29 A7 CD 7F 91 44 19 3C F9 53 AD E5 9B 7B
00 00 00 3C 1F B4 48 0B 21 0C 43 FC 96 65 C4 46 18 48 41 DD 70 13 6A 3C F8 A4 B0 3A
00 00 00 C3 40 AD DC 2C C5 BE 2B 96 EC 19 E6 74 A8 6A 53 AF 53 B1 CE 53 B6 6D 50 F9
00 00 00 80 D6 05 1C 7E FA 0C 0F CD 29 0A 39 D6 58 D3 CC 35 E9 E4 32 6A 74 36 F0 B8
00 00 00 3D 5C 99 F7 B2 BF 4E 15 89 33 32 3D 77 EA 9B 11 73 16 47 B8 15 FC 15 A4 79
00 00 00 FA 1E DB 31 0C A7 2F FD 14 5D 01 D8 29 CF 63 32 E5 1F A2 C6 04 A0 0A 52 BA
00 00 00 19 1E 55 9D A5 09 35 7E 8D 29 CF B6 8E CA 3D 87 15 98 53 62 ED E2 41 B2 FB
00 00 00 5C F8 A3 D7 03 F3 9A 92 85 34 2C D0 6D 01 C7 7F CF F4 26 FE D6 24 78 12 3C
00 00 00 9F 72 C9 BF 09 51 D4 C4 12 96 8B 84 74 53 FF 61 E8 C7 58 17 26 7F 45 8F 00
00 00 00 E2 46 B3 45 0F 7F 79 73 D1 49 CD DF D9 FF BC 39 4E DD CC 6C 41 3E 55 9C 00
00 00 00 B8 CE B7 8A 31 55 01 5E 45 DF 27 F6 C0 A1 A4 E3 11 87 0B 15 73 00 00 00 00
00 00 00 00 C0 5A A3 84 FA 5F 35 50 6F E6 5F 7C 0E D4 F5 A3 A7 AD F6 ED 00 00 00 00
00 00 00 00 00 C8 D2 80 71 60 89 49 C9 5F 5A FE 14 91 0E F3 94 F0 13 3E 48 00 00 00
00 00 00 00 00 00 00 9D 1B A0 AE D5 E2 CC 8D 50 69 01 0A D2 5A 09 71 F6 8A 00 00 00
00 00 00 00 00 00 A0 C4 7B 8E FF 08 C7 C1 08 66 BA FC 7C FA CA 33 4B 56 CC 00 00 00
00 00 00 00 A4 B3 40 58 52 75 6F EB A7 38 18 8A 74 E2 C4 AB 8B 06 CB 40 0E 00 00 00
00 00 B8 1E FC 6D AE F5 2C 8C 44 4D 28 2B 77 D1 D3 1C DC 65 31 72 DF B8 D0 00 00 00
24 AB AC 38 F2 EF 20 A1 10 87 AD 20 BD 6F 25 93 17 A1 42 00 8C B5 0C 8E 8E 00 00 00
CD 3C DA 4C 7D 58 0C E7 26 23 32 6E C3 EE 65 8E 9C 78 8C 86 97 87 45 A7 4C 00 00 00
0E D4 81 4E 7B FB 0E F3 1F A9 D0 CF 4A A4 9C 1E B4 DA 97 73 A0 6E 1E FB 0A 00 00 00
4F 6C 28 50 A7 50 6C 55 3A 99 A4 0E F9 28 A4 12 EE 9D E1 81 31 D0 F3 D0 08 00 00 00
90 04 F3 CC 03 CF CA 37 C3 CD F2 61 93 79 13 83 8B 6E B6 3B 84 7F 90 D8 00 00 00 00
3F 62 48 CC 6F 92 4A 65 23 FD DC AF 85 87 63 67 5E 00 BB 29 88 18 38 00 00 00 00 00
FE CA A1 CA 71 EF C0 F3 B2 1D 6C 41 26 6C 07 48 FD 34 9E 3C 4A 08 00 00 00 00 00 00
BD 32 FA C8 B8 40 F0 54 0D A4 BC 02 65 49 6D 1A AB 45 5B 24 00 00 00 00 00 00 00 00
7C 9A 89 EB 9C 9C A4 95 6D F9 A6 25 BA 3B B9 C5 35 2C 00 00 00 00 00 00 00 00 00 00    
'''    