# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:46:34 2020

@author: Acustica
Runge adaptativo

"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

xi=0
xf=2
y0=1

h=10
h1=[]

TOL=0.1

x=[]
y=[]

hmin=0.0001

def f(x,y):
    return 1-x+4*y#0.5+0.25*np.sin(x)-y/50

x.append(xi)
y.append(y0)
#sol[0]=y0

i = 0
    
while x[i] < xf:
    # Tentativo.
    f1=y[i]+h*f(x[i],y[i])
    yE=y[i]+(f(x[i],y[i])+f(x[i]+h,f1))*h/2
        
    # Cálculo del error normalmente (dos métodos de distinto orden).
    k1 = f(x[i], y[i]) 
    k2 = f(x[i] + 0.5 * h, y[i] + 0.5 *h* k1) 
    k3 = f(x[i] + 0.5 * h, y[i] + 0.5 *h* k2) 
    k4 = f(x[i]+h, y[i] + h*k3) 
    yR = y[i] + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
    
    ERR = abs(yE-yR)
    h1.append(h)
    if ERR <= TOL:
        x.append(x[i]+h)
        y.append(yE)
        i = i + 1;
    else:
        h=h*np.sqrt(TOL/ERR)    
    if h < hmin:        # Aquí habrá seguramente una asíntota, así que paramos y hacemos return.
        print('Error: el paso es más pequeño que hmin')
        break

sol=np.zeros([len(x)])    
for i in range(len(y)-1):
    sol[i+1]=(4*x[i+1]-3+19*np.exp(4*x[i+1]))/16
plt.plot(x,y),plt.plot(x,sol)    