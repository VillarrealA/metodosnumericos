# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:21:17 2020

@author: AVL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xi=0
xf=2
y0=1

h=0.2

x=np.linspace(xi,xf,int((xf-xi)/h)+1)

y=np.zeros([len(x)])
sol=np.zeros([len(x)])
e1=np.zeros([len(x)])

def f(x,y):
    return 1-x+4*y#3-2*x-0.5*y

y[0]=y0
sol[0]=y0
e1[0]=0
for i in range(len(x)-1):
    k1 = f(x[i], y[i]) 
    k2 = f(x[i] + 0.5 * h, y[i] + 0.5 *h* k1) 
    k3 = f(x[i] + 0.5 * h, y[i] + 0.5 *h* k2) 
    k4 = f(x[i]+h, y[i] + h*k3) 
    y[i+1] = y[i] + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
    #sol[i+1]=14-4*x[i+1]-13*np.exp(-x[i+1]/2)
    sol[i+1]=(4*x[i+1]-3+19*np.exp(4*x[i+1]))/16
    e1[i+1]=abs(y[i+1]-sol[i+1])


df=pd.DataFrame({'x':x,'y':y,'sol':sol,'dif':y-sol})
print(df)
plt.figure(0)
plt.plot(x,y),plt.plot(x,sol)
plt.figure(1)
plt.plot(x,e1)