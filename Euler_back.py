# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:21:17 2020

@author: AVL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xi=0
xf=1
y0=1

h=0.2

x=np.linspace(xi,xf,int((xf-xi)/h)+1)
#x=np.append(x,xf+h)

y=np.zeros([len(x)])
sol=np.zeros([len(x)])

y[0]=y0
sol[0]=y0
for i in range(len(x)-1):
    y[i+1]=(y[i]+(1-x[i+1])*h)/(1-4*h)
    sol[i+1]=(4*x[i+1]-3+19*np.exp(4*x[i+1]))/16


df=pd.DataFrame({'x':x,'y':y,'sol':sol,'dif':y-sol})
print(df)

plt.plot(x,y),plt.plot(x,sol)
