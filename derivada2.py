# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:45:33 2020

@author: Acustica
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

h=0.01

a=0

x = np.linspace(0,5*np.pi,100)
dydx=np.zeros([len(x)])

x = np.linspace(0,5*np.pi,100)
dydx=np.zeros([len(x)])

for i in range(len(x)-1):
    dydx[i] = (f(x[i]-2*h)-8*f(x[i]-h)+8*f(x[i]+h)-f(x[i]+2*h))/(12*h)

dYdx = -np.sin(x)

plt.figure(figsize=(12,5))
plt.plot(x,dydx,'r.',label='Diferencia central')
plt.plot(x,dYdx,'b',label='Valor verdadero')

plt.title('Cálculo numérico de la derivada de y = cos(x)')
plt.legend(loc='best')

