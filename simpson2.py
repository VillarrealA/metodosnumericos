# -*- coding: utf-8 -*-
"""
Created on Mon May  4 10:56:47 2020

@author: Acustica
simpson
"""

import numpy as np
import matplotlib.pyplot as plt
import math as ma

a=1
b=2

err=0.0002

K=2/(a)**3
n=ma.ceil(((K*(b-a)**4)/(180*err))**(1/4))

if n % 2 == 1:
        n+=1

def f(x):
    return 1/x
    
S=f(a)
x=np.linspace(a,b,n+1)
for i in range(1,n):
    print(S)
    if i % 2 == 1:
        A=4*f(x[i])
    else:
        A=2*f(x[i])
    S+=A
S+=f(b)
S=S*(b-a)/(3*n)

print("El area bajo la curva en el intervalo [", a, b, "] es", S)
print("El error para n=",n,"es:", abs(np.log(2)-S))
plt.figure(0)
plt.fill_between(x,f(x),color="green")
