# -*- coding: utf-8 -*-
"""
Created on Thu May  7 10:45:52 2020

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
dydx2=np.zeros([len(x)])
dydx3=np.zeros([len(x)])

for i in range(len(x)-1):
    dydx[i] = (f(x[i]-2*h)-8*f(x[i]-h)+8*f(x[i]+h)-f(x[i]+2*h))/(12*h)

for i in range(len(x)-1):
    dydx2[i] = (-f(x[i]-2*h)+16*f(x[i]-h)-30*f(x[i])+16*f(x[i]+h)-f(x[i]+2*h))/(12*h**2)
    
for i in range(len(x)-1):
    dydx3[i] = (f(x[i]-3*h)-8*f(x[i]-2*h)+13*f(x[i]-h)-13*f(x[i]+h)+8*f(x[i]+2*h)-f(x[i]+3*h))/(8*h**3)

dYdx = -np.sin(x)
dYdx2 = -np.cos(x)
dYdx3 = np.sin(x)

plt.figure(0)
plt.plot(x,dydx,'r.',label='Primera derivada')
plt.plot(x,dYdx,'b',label='Valor verdadero')

plt.title('Cálculo numérico de la primera derivada de y = cos(x)')
plt.legend(loc='best')

plt.figure(1)
plt.plot(x,dydx2,'r.',label='2da drivada')
plt.plot(x,dYdx2,'b',label='Valor verdadero')

plt.title('Cálculo numérico de la 2da derivada')
plt.legend(loc='best')

plt.figure(2)
plt.plot(x,dydx3,'r.',label='3ra derivada')
plt.plot(x,dYdx3,'b',label='Valor verdadero')

plt.title('Cálculo numérico de la 3ra derivada')
plt.legend(loc='best')