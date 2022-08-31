!pip install sympy
import numpy as np
from scipy import linalg
import sympy as sp
from sympy import *
from math import *
import pandas as pd
import math 
init_printing()

#Declara la funcion (sympy)
x1= symbols('x1')
x2= symbols('x2')
x3= symbols('x3')
l= symbols('l')
a= symbols('a')
sbl= Matrix(symbols('x1,x2'))
cbl= Matrix(symbols('x1,x2,x3'))
#Punto 1.b
def newton(e, x1ini, x2ini, f, i):
  x= Matrix([x1ini,x2ini])
  fd= Matrix([f])
  g= fd.jacobian(sbl).T
  h= g.jacobian(sbl)

#Iteraciones

  gradientx0= g.subs(x1, x[0]).subs(x2,x[1]).evalf() #gradiente evaluado en x1 evaluado con x2
  hx0= h.subs(x1,x1ini).evalf() #Hessiana evaluada con x1
  hessianx0= hx0.subs(x2,x2ini).evalf() #Hessiana evaluada con x1 con x2
  hinv= hessianx0.inv() #Hessiana inversa
  norma= gradientx0.norm()
  if norma<e or i==10:
    print(x, 'es el minimo en la iteracion', (i))
  else:
    xi=x - hinv*gradientx0  #Xk+1
    return newton(e, xi[0], xi[1], f,i+1)
