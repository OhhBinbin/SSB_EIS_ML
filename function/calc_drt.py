#!/usr/bin/env python
# coding: utf-8

# In[14]:

import numpy as np

def calc_drt(Re,Im,freq,iter):
    w = 2*np.pi*freq
    [Are,Aim] = calc_A(w)
    
    #fig = plt.figure()
    #ax = fig.add_subplot(111, projection='3d')
    #X, Y = np.meshgrid(np.log(freq), np.log(freq))
    #ax.plot_surface(X,Y,Aim)
    Aim = Aim * (-1)
    Z = Im.reshape(len(Im),1)
    H1 = Aim
    #print(Z)
    H2 = np.matmul(H1, Aim)
    N_iterationen = iter
    drt = np.ones((len(freq),1))*0.001
    
    for i in range(0,N_iterationen):
        drt = np.multiply(np.divide(np.matmul(H1, Z),(np.matmul(H2,drt))),drt)
        #drt = (H1*Z)/(H2*drt) * drt
    
    return drt



def calc_A(w):
    dw = np.mean(np.gradient(np.log(1./w)))
    
    Are = np.zeros((len(w),len(w)))
    Aim = np.zeros((len(w),len(w)))
    
    for iter_n in range(0,len(w)):
        for iter_m in range(0,len(w)):
            w_n = w[iter_n]
            w_m = w[iter_m]
            Are[iter_n,iter_m] = 1/(1+(w_n/w_m)**2)
            Aim[iter_n,iter_m] = -(w_n/w_m)/(1+(w_n/w_m)**2)
        
    Aim = -Aim*dw
    Are = -Are*dw
    return [Are,Aim]