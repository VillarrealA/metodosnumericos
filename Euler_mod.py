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
e=np.zeros([len(x)])

eps=0.1

def f(x,y):
    return 1-x+4*y#3-2*x-0.5*y

y[0]=y0
sol[0]=y0
e[0]=0

for i in range(len(x)-1):
    f1=y[i]+h*f(x[i],y[i])
    y[i+1]=y[i]+(f(x[i],y[i])+f(x[i+1],f1))*h/2
    
    sol[i+1]=(4*x[i+1]-3+19*np.exp(4*x[i+1]))/16

plt.figure(0)
plt.plot(x,y),plt.plot(x,sol)
