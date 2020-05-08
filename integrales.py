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
n=5

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

print(S)
print(abs(np.log(2)-S))
