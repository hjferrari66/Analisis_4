# Práctica 2 - Ejercicio 1   
Dada una función analítica <img src="https://render.githubusercontent.com/render/math?math=\large f(z)">, calcular 
<img src="https://render.githubusercontent.com/render/math?math=\large\int_{z_1}^{z_2} f(z)">
- La integral no depende del camino
- La integral sobre un camino cerrado es cero
- Existe una función F(z) tal que <img src="https://render.githubusercontent.com/render/math?math=\large f(z) = \frac{dF(z)}{dz}">
- <img src="https://render.githubusercontent.com/render/math?math=\large \int_{z_1}^{z_2} f(z) = F(z_2) - F(z_1)">


```python
from sympy import *
z, f, F = symbols('z f F')
init_printing(use_unicode=True)
```

En la siguiente celda defino una función que dada <img src="https://render.githubusercontent.com/render/math?math=\large f(z), z_1 y z_2"> calcula 
<img src="https://render.githubusercontent.com/render/math?math=\large F(z)"> y el valor de la integral


```python
def integral1(f,z1,z2):
    if (not (integrate(f, z).has(Integral))):
        F = integrate(f, z)
        print('f=', f, 'F=', F, 'F(z2)=', F.evalf(subs={z:z2}), 'F(z1)=', F.evalf(subs={z:z1}))
        return F.evalf(subs={z:z2}) - F.evalf(subs={z:z1})
    else:
        print('No encuentro la primitiva')
```


```python
integral1(1/z**3,-1+2j,-3+1j)
```

    f= z**(-3) F= -1/(2*z**2) F(z2)= -0.04 - 0.03*I F(z1)= 0.06 - 0.08*I




\int_{z_1}^{z_2} f(z) = F(z_2) - F(z_1)
$\displaystyle -0.1 + 0.05 i$




```python
integral1(1/cos(z**3),2j,-3)
```

    No encuentro la primitiva

