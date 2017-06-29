# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 17:23:56 2017

@author: Damon Lee
"""

import numpy as np
import matplotlib.pyplot as plt

#◎ 基本題

#畫出底下的函數及其一次微分的圖：
#1. Sigmoid
#2. tanh
#3. ReLU
#4. Leaky ReLU
#5. ELU


def draw(x,y1,y2):
    plt.subplot(121)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("function")
    ax = plt.gca() 
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    plt.plot(x,y1)
    
    plt.subplot(122)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("derived_function")
    ax = plt.gca() 
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',0))
    ax.spines['left'].set_position(('data',0))
    plt.plot(x,y2)
    plt.show()

def functions(fun_name,x):

    if fun_name=='Sigmoid':
        return (1 / (1 + np.exp(-x)))
    elif fun_name=='tanh':
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    elif fun_name=='ReLU':
        return np.where(x > 0, x, 0)
    elif fun_name=='Leaky ReLU':    
        return np.where(x > 0.01 * x, x, 0.01 * x)
    elif fun_name=='ELU': 
        alpha=0.09
        return np.where(x > 0, x, alpha * (np.exp(x) - 1))    
    
    
def derived_funs(fun_name,x):
    
    if fun_name=='Sigmoid':
        return (functions('Sigmoid',x) * (1 - functions('Sigmoid',x)))
    elif fun_name=='tanh':
        return (1 - np.square(functions('tanh',x)))
    elif fun_name=='ReLU':
        return np.where(x > 0, 1, 0)
    elif fun_name=='Leaky ReLU':    
        return np.where(x > 0.01 * x, 1, 0.01)
    elif fun_name=='ELU': 
        alpha=0.09
        return np.where(x > 0, 1, functions('ELU',x) + alpha)
                
def main():
    x=np.linspace(-10,10,100)
    activation_functions=['Sigmoid','tanh','ReLU','Leaky ReLU','ELU']
    for funs in activation_functions:
        y1=functions(funs,x)
        y2=derived_funs(funs,x)
        draw(x,y1,y2)
  

if __name__=='__main__':
    main()    