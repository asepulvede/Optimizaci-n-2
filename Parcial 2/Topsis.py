import numpy as np
import math 
from math import sqrt

#Método auxiliar para construir la matriz normalizada ponderada
def matriz_norm_ponderada(matrix, lp, w):
  rows, columns= matrix.shape
  newMatrix= np.zeros((rows,columns))
  aux= np.zeros(columns)
  a= np.zeros(columns)
  aux2=np.zeros((rows,columns))
  
  for i in range(columns):
    for j in range(rows):
      if lp==2:
        a[i]+= matrix[j,i]**lp
      elif lp==1:
        aux[i]+= abs(matrix[j,i])
      else: 
        aux2[j,i]= abs(matrix[j,i])
        aux= aux2.max(axis=0)


  for i in range(columns):
    if lp==2:
      aux[i]=sqrt(a[i])
    for j in range(rows):
      newMatrix[j,i]= float((matrix[j,i]/aux[i]))*w[i]

  return newMatrix
  
  #Método auxiliar para hallar solución ideal y anti-ideal
def soluciones(matrixPond, criterio): 
  rows, columns= matrixPond.shape
  solIdeal= np.zeros(len(criterio))
  solAntiIdeal= np.zeros(len(criterio))
  aux= np.zeros(columns)
  aux2= np.zeros(rows)
  
  #Soluciones ideales
  for i in range(len(criterio)):
    if criterio[i] != "indeseable":
      solIdeal= matrixPond.max(axis=0)
      solAntiIdeal= matrixPond.min(axis=0)
    else:
      for j in range(rows):
        aux2[j]= matrixPond[j,i]
        solIdeal[i]= np.min(aux2)
        solAntiIdeal[i]= np.max(aux2)

  return solIdeal, solAntiIdeal

#Método auxiliar para hallar la medida de las distancias
def distancias(matrixPond,lp,solIdeal,solAntiIdeal):
  rows, columns= matrixPond.shape
  distanciaIdeal= np.zeros(rows)
  distanciaAntiIdeal= np.zeros(rows)
  aux= np.zeros(rows)
  aux2= np.zeros(rows)
  auxiliar= np.zeros((columns,rows))
  auxiliar2= np.zeros((columns,rows))
  
  for i in range(rows):
    for j in range(columns):
        if lp==2:
          aux[i]+= float(((matrixPond[i,j]-solIdeal[j])**2))
          distanciaIdeal[i]= (aux[i])**(1/lp)
          aux2[i]+= float((matrixPond[i,j]-solAntiIdeal[j])**2)
          distanciaAntiIdeal[i]= (aux2[i])**(1/lp)
        elif lp==1:
          distanciaIdeal[i]+= abs(matrixPond[i,j]-solIdeal[j])
          distanciaAntiIdeal[i]+= abs(matrixPond[i,j]-solAntiIdeal[j])
        else: 
          auxiliar[j,i]= abs(matrixPond[i,j]-solIdeal[j])
          distanciaIdeal= auxiliar.max(axis=0)
          auxiliar2[j,i]= abs(matrixPond[i,j]-solAntiIdeal[j])
          distanciaAntiIdeal= auxiliar2.max(axis=0)

  return distanciaIdeal,distanciaAntiIdeal

def topsis(A,lp,w,criterio):
  rows, columns = A.shape
  proximidadR= np.zeros(rows)   
  
  #Construimos la matriz normalizada ponderada
  matrizPond= matriz_norm_ponderada(A,lp,w)
  print('matriz normalizada ponderada')
  print(matrizPond)
  
  #Hallamos soluciones ideales y anti-ideales
  solIdeal, solAntiIdeal= soluciones(matrizPond,criterio)
  print('solIdeal',solIdeal)
  print('sol Antiideal',solAntiIdeal)

  #Calculamos las distancias ideales y anti-ideales
  distanciaIdeal, distanciaAntiIdeal= distancias(matrizPond,lp,solIdeal,solAntiIdeal)
  print('distancia ideal',distanciaIdeal)
  print('distancia Antiideal',distanciaAntiIdeal)
  
  #Calculamos la proximidad de cada alternartiva
  for i in range(len(proximidadR)):
    proximidadR[i]= distanciaAntiIdeal[i]/(distanciaIdeal[i]+distanciaAntiIdeal[i]) 

  print('RS',proximidadR) 
  
topsis(np.array([[1,5],[4,2],[3,3]]),1,[0.5,0.5],np.array(["deseable","deseable"]))
topsis(np.array([[1,5],[4,2],[3,3]]),2,[0.5,0.5],np.array(["deseable","deseable"]))
topsis(np.array([[1,5],[4,2],[3,3]]),"infinito",[0.5,0.5],np.array(["deseable","deseable"]))
  

