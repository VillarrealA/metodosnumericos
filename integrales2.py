# -*- coding: utf-8 -*-
"""
Created on Sun May  3 17:04:11 2020

@author: Acustica
Integral regla del trapecio
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=1
b=2

err=0.0001
K=2/(a)**3
n=ma.ceil(np.sqrt((K*(b-a)**3)/(12*err)))

def f(x):
    return 1/x
    
dx=(b-a)/n
xi=a
S=f(xi)

for i in range(1,n):
    xi+=dx
    S+=2*f(xi)
S+=f(b)
S=S*dx/2

print("El area bajo la curva en el intervalo [", a, b, "] es", S)
print("El error para n=",n,"es:", abs(np.log(2)-S))

