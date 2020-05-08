# -*- coding: utf-8 -*-
"""
Created on Sun May  3 18:05:25 2020

@author: Acustica
Medio
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

a=1
b=2
n=5

def f(x):
    return 1/x
    
S=0
x=np.linspace(a,b,n+1)
for i in range(n):
    xi=(x[i]+x[i+1])/2
    S+=f(xi)

S=S*(b-a)/n

print(S)
print(abs(np.log(2)-S))