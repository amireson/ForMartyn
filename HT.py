#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as pl
from scipy.integrate import odeint


# In[2]:


def thetaFun(psi,pars):
    psi_dummy=psi.copy()
    psi_dummy[psi_dummy>0]=0.
    Se=(1+(pars['alpha']*psi_dummy)**pars['n'])**(-pars['m'])
    return Se*(pars['thetaS']-pars['thetaR'])+pars['thetaR']

def CFun(psi,pars):
    psi_dummy=psi.copy()
    psi_dummy[psi_dummy>0]=0.
    m=pars['m']
    Se=(1+(pars['alpha']*psi_dummy)**pars['n'])**(-m)
    C=-pars['alpha']*m/(1-m)*(pars['thetaS']-pars['thetaR'])*Se**(1/m)*(1-Se**(1/m))**m
    C[psi_dummy>=0]=0.
    return C

def GCE(T,pars):
    psi=pars['Lf']/pars['g']/pars['T0']*T
    psi[psi>0]=0.
    return psi

def SFC(T,pars):
    psi=GCE(T,pars)
    theta=thetaFun(psi,pars)
    return theta 

def CFC(T,pars):
    psi=GCE(T,pars)
    C=CFun(psi,pars)*pars['Lf']/pars['g']/pars['T0']
    return C


# In[3]:


def BulkHeatCapacityfun(T,pars):
    thL=SFC(T,pars)
    thI=pars['thetaS']-thL
    thS=1-pars['thetaS']
    BHC=pars['CI']*thI*pars['rhoI']
    BHC+=pars['CL']*thL*pars['rhoL']
    BHC+=pars['CS']*thS*pars['rhoS']
    fdash=CFC(T,pars)
    A=(pars['T0']+T)*pars['rhoL']*(pars['CL']-pars['CI'])
    B=pars['rhoL']*pars['Lf']
    BHC+=fdash*(A+B)
    BHC=BHC
    return BHC


# In[4]:


def BulkThermalConductivityfun(T,pars):
    thL=SFC(T,pars)
    thI=pars['thetaS']-thL
    thS=1-pars['thetaS']
    X=thL*pars['lamL']**pars['a']
    X+=thI*pars['lamI']**pars['a']
    X+=thS*pars['lamS']**pars['a']
    lam=X**(1/pars['a'])
    return lam


# In[5]:


def ODEfun(T,t,tB,TB,Hsurf,dz,pars,nz):

    lam=BulkThermalConductivityfun(T,pars)
    BHC=BulkHeatCapacityfun(T,pars)
    
    # Heat fluxes:
    H=np.zeros(nz+1)
    H[1:-1]=-(lam[1:]+lam[:-1])/2*(T[1:]-T[:-1])/(dz)
    # Upper boundary:
    if Hsurf==[]:
        TB=np.interp(t,tB,TB)
        H[0]=-lam[0]*(T[0]-TB)/(dz/2.)
    else:
        H[0]=Hsurf*86400.
    # Lower boundary:
    H[-1]=0.
    
    dTdt=-(H[1:]-H[:-1])/dz/BHC
    return dTdt


# # Define parameters:

# In[6]:


