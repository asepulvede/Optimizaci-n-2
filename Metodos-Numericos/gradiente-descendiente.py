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
##Punto 1.a
def gradiente(e, x1ini, x2ini, f, i):
  x= Matrix([x1ini, x2ini])
  fd= Matrix([f])
  g= fd.jacobian(sbl).T
  
  gx0= g.subs(x1,x1ini).evalf()
  gradientx0= gx0.subs(x2,x2ini).evalf()
  norm= gradientx0.norm()
  if norm<e or i==10:
    print(x, 'es el minimo en la iteración', (i))
  else:
    xi= x- l*gradientx0
    x1i= xi[0]
    x2i= xi[1]
    nf= fd.subs(x1, x1i)
    nf2= nf.subs(x2,x2i)
    gl= diff(nf2,l)
    print(gl)
    landa= solve(gl,l)
    landa_value = list(landa.values())[0]
    xii= x-landa_value*gradientx0
    return gradiente(e, xii[0], xii[1], f, i+1)
