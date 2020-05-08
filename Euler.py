# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:21:17 2020

@author: AVL
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

for i in range(1,len(x)):
    y[i]=y[i-1]+f(x[i-1],y[i-1])*h
    sol[i]=(4*x[i]-3+19*np.exp(4*x[i]))/16
    e1[i]=abs(sol[i]-y[i])


#df=pd.DataFrame({'x':x,'y':y,'sol':sol,'dif':y-sol})
print(e1[len(x)-1])

plt.figure(0)
plt.plot(x,y),plt.plot(x,sol)
#plt.figure(1)
#plt.plot(x,e1),plt.xlim(xi,xf)