# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:05:55 2020

@author: Acustica
"""

import numpy as np
from matplotlib import pyplot as plt

def diff(x,y):
    return 3-2*x-0.5*y 

x = np.linspace(-1,5,20)
y = np.linspace(-5,5,20)

for j in x:
    for k in y:
        slope = diff(j,k)
        domain = np.linspace(j-0.07,j+0.07,2)
        def fun(x1,y1):
            z = slope*(domain-x1)+y1
            return z
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')

plt.title("Ejemplo")
plt.grid(True)
plt.show()