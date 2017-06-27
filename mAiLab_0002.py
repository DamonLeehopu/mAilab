# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 14:34:51 2017

@author: Damon Lee
"""

#◎ 基本題 
#v1. 產生五個亂數，並將其輸出。
#v2. 產生N個介於-1與1之間的亂數，計算其平均值與標準差並輸出，每個亂數的值則不用輸出。N=10**1, 10**2, 10**3, 10**4, 10**5。

#◎ 進階題
#v3. 做基本題2時，一併輸出產生每N個亂數前後的系統時間，並計算所需的時間。 
# 4. 自己寫一個亂數產生器。

import random
import numpy as np
import time


#1.
def basic1():
    print('basic#1:')
    for i in range(5):
        print(random.random())
        #use random function to get random number 

def basic2_adv3():
    print('basic#2 and advanced#3:')
    for N in [10,10**2,10**3,10**4,10**5]:
        start_time=time.time() #get start time
        print('N='+str(N)+':')
        print('start_time='+str(time.asctime( time.localtime(start_time))))
        random_numbers=[]
        for i in range(N):
            random_numbers.append(random.uniform(-1,1))   #generate N random numbers which between -1 and 1     

        print('average:'+str(np.mean(random_numbers)))   #average of random numbers
        print('standard_deviation:'+str(np.std(random_numbers)))  #standard deviation of random numbers
        end_time=time.time() #get end time
        print('end_time='+str(time.asctime( time.localtime(end_time))))
        print('used_sys_time='+str())
        print(end_time-start_time)   #print time difference between start_time and end_time

        
def main():    
    basic1()
    basic2_adv3()    

    
    
if __name__ == '__main__':
    main() 
    
'''  
basic#1:
0.7509444618435627
0.2524879768693492
0.8644224655521993
0.8336061209446637
0.5688493244770654
basic#2 and advanced#3:
N=10:
start_time=Tue Jun 27 15:15:15 2017
average:-0.235500053553
standard_deviation:0.465155214589
end_time=Tue Jun 27 15:15:15 2017
used_sys_time=
0.002000093460083008
N=100:
start_time=Tue Jun 27 15:15:15 2017
average:0.0662467040977
standard_deviation:0.56427785265
end_time=Tue Jun 27 15:15:15 2017
used_sys_time=
0.0
N=1000:
start_time=Tue Jun 27 15:15:15 2017
average:0.00565919525565
standard_deviation:0.570535035689
end_time=Tue Jun 27 15:15:15 2017
used_sys_time=
0.0010001659393310547
N=10000:
start_time=Tue Jun 27 15:15:15 2017
average:0.00112683374344
standard_deviation:0.576638259685
end_time=Tue Jun 27 15:15:15 2017
used_sys_time=
0.008000373840332031
N=100000:
start_time=Tue Jun 27 15:15:15 2017
average:-0.00186716250688
standard_deviation:0.577614697791
end_time=Tue Jun 27 15:15:15 2017
used_sys_time=
0.07300400733947754
'''  
    