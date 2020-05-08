# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:13:14 2020

@author: Acustica
http://aprendeenlinea.udea.edu.co/lms/men_udea/pluginfile.php/25793/mod_resource/content/0/Integracion_numerica/integracion_NUMERICA1.pdf

derivada
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.cos(x)

h=0.01

a=0

#print("La derivada de la función evaluada en el punto", a, "es", (f(a+h)-f(a-h))/(2*h))

#print("La derivada de la función evaluada en el punto", a, "es", (f(a+h) -f(a))/h)

#print("La derivada de la función evaluada en el punto", a, "es", (f(a)-f(a-h))/h)


x = np.linspace(0,5*np.pi,100)
dydx=np.zeros([len(x)])

for i in range(len(x)-1):
    dydx[i] = (f(x[i]+h)-f(x[i]-h))/(2*h)

dYdx = -np.sin(x)

plt.figure(figsize=(12,5))
plt.plot(x,dydx,'r.',label='Diferencia central')
plt.plot(x,dYdx,'b',label='Valor verdadero')

plt.title('Cálculo numérico de la derivada de y = cos(x)')
plt.legend(loc='best')

