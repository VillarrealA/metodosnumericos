# -*- coding: utf-8 -*-
"""
Created on Sat May  2 20:06:38 2020

@author: Acustica

http://blog.espol.edu.ec/matg1013/runge-kutta-d2y-dx2/
ecuacion de segundo orden
"""
import numpy as np
import matplotlib.pyplot as plt

xi=1
xf=20
y0=1
u0=2

h=0.2

x=np.linspace(xi,xf,int((xf-xi)/h)+1)

y=np.zeros([len(x)])
u=np.zeros([len(x)])
sol=np.zeros([len(x)])
e1=np.zeros([len(x)])

def up(x,y,u):
    return (-2/x)*u+(1/x**2)

def yp(u):
    return u

sol[0]=y0
e1[0]=0
y[0] = y0
u[0]= u0

for i in range(1,len(x)):
    m1 = yp(u[i-1])
    K1 = up(x[i-1],y[i-1],u[i-1])
    
    m2 = yp(u[i-1] + h*K1/2)
    K2 = up(x[i-1]+h/2, y[i-1] + h*m1/2, u[i-1] + h*K1/2)
    
    m3 = yp(u[i-1] + h*K2/2)
    K3 = up(x[i-1]+h/2, y[i-1] + h*m2/2, u[i-1] + h*K2/2)

    m4 = yp(u[i-1] + h*K3)
    K4 = up(x[i-1]+h, y[i-1] + h*m3, u[i-1] + h*K3)

    y[i] = y[i-1] + h*(m1+2*m2+2*m3+m4)/6
    u[i] = u[i-1] + h*(K1+2*K2+2*K3+K4)/6
    sol[i]=np.log(x[i])-(1/x[i])+2
    e1[i]=abs(y[i]-sol[i])

plt.figure(0)
plt.plot(x,y),plt.plot(x,sol)
plt.figure(1)
plt.plot(x,e1)
