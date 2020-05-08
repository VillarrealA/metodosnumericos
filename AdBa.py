# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 11:46:53 2020

@author: Acustica
Adams-Bashforth

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
e1=np.zeros([len(x)])
e2=np.zeros([len(x)])

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
    sol[i+1]=(4*x[i+1]-3+19*np.exp(4*x[i+1]))/16
    
for i in range(4,len(x)-1):
    v1 = 55 *  f(x[i],y[i])
    v2 = -59 * f(x[i-1],y[i-1])
    v3 = 37 * f(x[i-2],y[i-2])
    v4 = -9 * f(x[i-3],y[i-3])
    y[i+1]= y[i]+ (h/24)*(v1 + v2 + v3 + v4)
    sol[i+1]=(4*x[i+1]-3+19*np.exp(4*x[i+1]))/16

plt.figure(0)
plt.plot(x,y),plt.plot(x,sol)