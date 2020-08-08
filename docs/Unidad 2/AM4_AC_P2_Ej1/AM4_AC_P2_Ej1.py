#!/usr/bin/env python
# coding: utf-8

# # Práctica 2 - Ejercicio 1   
# Dada una función analítica $f(z)$, calcular $\int_{z_1}^{z_2} f(z) $  
# - La integral no depende del camino
# - La integral sobre un camino cerrado es cero
# - Existe una función F(z) tal que $f(z) = \frac{dF(z)}{dz}$
# - $\int_{z_1}^{z_2} f(z) = F(z_2) - F(z_1)$

# In[36]:


from sympy import *
z, f, F = symbols('z f F')
init_printing(use_unicode=True)


# En la siguiente celda defino una función que dada $f(z), z_1 y z_2$ calcula $F(z)$ y el valor de la integral

# In[66]:


def integral1(f,z1,z2):
    if (not (integrate(f, z).has(Integral))):
        F = integrate(f, z)
        print('f=', f, 'F=', F, 'F(z2)=', F.evalf(subs={z:z2}), 'F(z1)=', F.evalf(subs={z:z1}))
        return F.evalf(subs={z:z2}) - F.evalf(subs={z:z1})
    else:
        print('No encuentro la primitiva')


# In[69]:


integral1(1/z**3,-1+2j,-3+1j)


# In[70]:


integral1(1/cos(z**3),2j,-3)

