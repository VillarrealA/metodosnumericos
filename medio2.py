# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:23:43 2020

@author: Acustica
"""

import numpy as np
import matplotlib.pyplot as plt
import math as ma

a=1
b=2

err=0.0001
K=2/(a)**3
#K=2*np.exp(b**2)*(2*b**2+1)
n=ma.ceil(np.sqrt((K*(b-a)**3)/(24*err)))

def f(x):
    return 1/x
    
S=0
x=np.linspace(a,b,n+1)
for i in range(n):
    xi=(x[i]+x[i+1])/2
    #print(xi)
    S+=f(xi)

S=S*(b-a)/n

print("El area bajo la curva en el intervalo [", a, b, "] es", S)
print("El error para n=",n,"es:", abs(np.log(2)-S))
plt.figure(0)
plt.fill_between(x,f(x),color="green")

    