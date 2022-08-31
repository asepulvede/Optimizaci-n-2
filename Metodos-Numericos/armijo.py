#Punto 2.a
from sympy import *
from sympy.plotting import plot
from sympy.abc import x
from sympy.abc import y
init_printing()
f = 5*x**2 + 5*y**2 - x*y - 11*x + 11*y + 11
dfx = diff(f, x) # 1era. derivada
dfy = diff(f, y)
pc = solve([dfx,dfy], (x, y))

#Punto 2.b
from sympy.plotting import plot3d
def graf():
  g = plot3d(f, show = False)
  g.show()
graf()

#Punto 2.c
def gradiente1(fx):
  dx = fx.diff(x)
  dy = fx.diff(y)
  gradiente = []
  grad_=[]
  gradiente.append(dx)
  gradiente.append(dy)
  gradiente = sp.lambdify([x,y], gradiente)
  return gradiente

def hessiana(fx):
  dx = fx.diff(x)
  dy = fx.diff(y)
  dxx = dx.diff(x)
  dyx = dx.diff(y)
  dxy = dy.diff(x)
  dyy = dy.diff(y)
  hessiana = np.zeros((2,2))
  hessiana[0,0] = dxx
  hessiana[0,1] = dxy
  hessiana[1,0] = dxy
  hessiana[1,1] = dyy
  return hessiana

def armijo(f,t,xn):
  tolerancia = 0.08
  gr = gradiente1(f)
  h = hessiana(f)
  hinv = np.linalg.inv(h)
  dir = -np.matmul(gr(xn[0], xn[1]), hinv)
  if f.subs(x, xn[0]+t*dir[0]).subs(y, xn[1]+t*dir[1])<=(f.subs(x,xn[0]).subs(y, xn[1])+tolerancia*t*np.matmul(np.array(gr(xn[0],xn[1])).T,dir)):
    return t
  else:
    t = t*0.08
    return armijo(f,t,xn)

def gdes(tolerancia, xn, f, iter):
  gr = gradiente1(f)
  normagr = np.linalg.norm(gr(xn[0], xn[1]))
  if normagr<tolerancia or iter ==10:
    print('El numero minimo en la iteración es', xn, (iter))
    print('Con Y', f.subs([(x,xn[0]),(y,xn[1])]).evalf(), 'siendo el punto mínimo en la función objetivo ')
  else:
    tamPas = armijo(f,0.1,xn)
    xn = xn - np.multiply(tamPas, gr(xn[0], xn[1]))
    return gdes(tolerancia, xn, f, iter+1)

x0 = []
x0.append(0.5)
x0.append(1.5)
gdes(0.5*10**(-15),x0, f, 0)
