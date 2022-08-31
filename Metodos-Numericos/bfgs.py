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

#Punto 3.a.b
def bfgs(e, x1ini, x2ini, x3ini, f, B, i):
  x= Matrix([x1ini, x2ini, x3ini])
  fd= Matrix([f])
  g= fd.jacobian(cbl).T

  gx0= g.subs(x1,x1ini).evalf() #Gradiene evaluado con x1
  gx1= gx0.subs(x2,x2ini).evalf() 
  gradientx0= gx1.subs(x3,x3ini).evalf() #gradiente evaluado en x1 evaluado con x2
  norma= gradientx0.norm()
  if norma<e:
    print(x, 'es el minimo en la iteracion', (i))
  else: 
    pk= -B.inv()*gradientx0
    np= x+ a*pk
    nf= fd.subs(x1, np[0]).subs(x2,np[1]).subs(x3,np[2])
    gl= diff(nf,a)
    ak= solve(gl,a)
    ak_value = list(ak.values())[0]
    sk= ak_value*pk
    xn= x + sk
    yk= g.subs(x1, xn[0]).subs(x2,xn[1]).subs(x3,xn[2]) - g.subs(x1,x[0]).subs(x2,x[1]).subs(x3,x[2])
    s= yk.T*sk
    b= sk.T*B*sk
    Bk1= B + (1/s[0])*(yk*yk.T)- (1/b[0])*(B*sk*sk.T*B.T)
    return bfgs(e, xn[0], xn[1], xn[2], f, Bk1, i+1)
