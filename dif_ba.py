# -*- coding: utf-8 -*-
"""
Created on Fri May  1 13:10:05 2020

@author: Acustica
diferenciacion hacia atras

"""

import numpy as np
import matplotlib.pyplot as plt

xi=0
xf=2
y0=1

h=0.2

x=np.linspace(xi,xf,int((xf-xi)/h)+1)

y=np.zeros([len(x)])
sol=np.zeros([len(x)])

def f(x,y):
    return 1-x+4*y
    
y[0]=y0
sol[0]=y0

for i in range(4):
    k1 = f(x[i], y[i]) 
    k2 = f(x[i] + 0.5 * h, y[i] + 0.5 *h* k1) 
    k3 = f(x[i] + 0.5 * h, y[i] + 0.5 *h* k2) 
    k4 = f(x[i]+h, y[i] + h*k3) 
    y[i+1] = y[i] + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
    sol[i+1]=(4*x[i]-3+19*np.exp(4*x[i]))/16
    
for i in range(4,len(x)-1):
    y[i+1] = (1/(25-48*h))*(48*y[i]-36*y[i-1]+16*y[i-2]-3*y[i-3]+12*h-12*h*x[i+1])
    sol[i+1] = (4*x[i+1]-3+19*np.exp(4*x[i+1]))/16
print(abs(sol[len(x)-1]-y[len(x)-1]))    
plt.figure(1)
plt.plot(x,y),plt.plot(x,sol)

    