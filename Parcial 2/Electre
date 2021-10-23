import numpy as np
import math 
from math import sqrt

#Método auxiliar para construir la matriz normalizada ponderada
def matriz_norm(matrix,w,criterio):
  rows, columns= matrix.shape
  newMatrixPond= np.zeros((rows,columns))
  minimo= matrix.min(axis=0)
  maximo= matrix.max(axis=0)
  rango= np.zeros(columns)

  for i in range(len(rango)):
    rango[i]= maximo[i]-minimo[i]
  
  for i in range(columns):
    if criterio[i] != "indeseable":
      for j in range(rows):
        newMatrixPond[j,i]= ((matrix[j,i]-minimo[i])/(rango[i]))
    else: 
      for j in range(rows):
        newMatrixPond[j,i]= ((maximo[i]-matrix[j,i])/rango[i])
  return newMatrixPond
  
#Método auxiliar para construir la matriz de concordancia
def concordancia(matrixPond,w):
  rows, columns= matrixPond.shape
  matrizConcordancia= np.zeros((rows,rows))
  aux= np.zeros(columns)

  for i in range(rows):
    for j in range(rows):
      if i==j:
        matrizConcordancia[i,j]= "NaN"
      else:
        for k in range(columns):
          if matrixPond[i,k]==matrixPond[j,k]:
            matrizConcordancia[i,j]= w[k]*0.5
          elif matrixPond[i,k]>matrixPond[j,k]:
            matrizConcordancia[i,j]+= w[k]
          else:
            continue
        
  return matrizConcordancia
  
#Método auxiliar para construir la matriz de discordancia 
def discordancia(matrixPon):
  rows, columns= matrixPon.shape
  matrizDiscordancia= np.zeros((rows,rows))
  
  for i in range(rows):
    for j in range(rows):
      diferenciaN=[]
      diferenciaD=[]
      if i==j:
        matrizDiscordancia[i,j]= "NaN"
      else:
        for k in range(columns):
          diferenciaD.append(abs(matrixPon[i,k]-matrixPon[j,k]))
          if matrixPon[i,k]<matrixPon[j,k]:
            diferenciaN.append(matrixPon[j,k]-matrixPon[i,k])
        if len(diferenciaN)!=0:
          matrizDiscordancia[i,j]= max(diferenciaN)/max(diferenciaD)
        
  return matrizDiscordancia
 
#Método auxiliar para hallar la matriz de dominancia concordante y discordante
def matriz_domConDis(matrizCon,matrizDis,uc,ud):
  rows, columns= matrizCon.shape
  matrizDominanciaCon= np.zeros((rows,columns))
  matrizDominanciaDis= np.zeros((rows,columns))
  for i in range(rows):
    for j in range(columns):
      if i==j:
        matrizDominanciaCon[i,j]= "NaN"
        matrizDominanciaDis[i,j]= "NaN"
      else:
        if matrizCon[i,j]>uc:
          matrizDominanciaCon[i,j]=1
        if matrizDis[i,j]<ud:
          matrizDominanciaDis[i,j]=1
          
  return matrizDominanciaCon, matrizDominanciaDis
  
#Método auxiliar para construir la matriz de dominancia agregada
def matriz_domAgregada(matriz,matriz2):
  rows, columns= matriz.shape
  matrizDomAgregada= np.zeros((rows,columns))
  for i in range(rows):
    for j in range(columns):
      if matriz[i,j]==1 and matriz2[i,j]==1:
        matrizDomAgregada[i,j]=1
      else:
        matrizDomAgregada[i,j]=0
      if i==j:
        matrizDomAgregada[i,j]= "NaN"

  return matrizDomAgregada
 
def electre(matrix,w,criterio,uc,ud):
  rows, columns= matrix.shape
  matrizPonderada= np.zeros((rows,columns))

  #Construimos la matriz normalizada
  matrizNormalizada= matriz_norm(matrix,w,criterio)
  print('matriz normalizada')
  print(matrizNormalizada)

  #Construimos la matriz normalizada ponderada
  for i in range(rows):
    for j in range(columns):
      matrizPonderada[i,j]= matrizNormalizada[i,j]*w[j]
  print('matriz ponderada')
  print(matrizPonderada)

  #Construimos la matriz de conconrdancia
  matrizConcordancia=concordancia(matrizNormalizada,w)
  print('matriz de concordancia')
  print(matrizConcordancia)

  #Construimos la matriz de discordancia
  matrizDiscordancia= discordancia(matrizPonderada)
  print('matriz de discordancia')
  print(matrizDiscordancia)

  #Construimos las matrices de dominancia concordante y discordante
  matrizDomConcordante, matrizDomDiscordante= matriz_domConDis(matrizConcordancia,matrizDiscordancia,uc,ud)
  print('matriz de dominanca concordante')
  print(matrizDomConcordante)
  print('matriz de dominanca discordante')
  print(matrizDomDiscordante)

  #Construimos la matriz de dominancia agregada
  matrizDomAgregada= matriz_domAgregada(matrizDomConcordante,matrizDomDiscordante)
  print('matriz de dominancia agregada')
  print(matrizDomAgregada)

  #Calculamos la suma de las filas y las columnas de la matriz de dominancia agregada
  vectorSumaFila= np.zeros(rows)
  vectorSumaColumna= np.zeros(rows)
  for i in range(rows):
    for j in range(rows):
      if i!=j:
        vectorSumaFila[i]+= matrizDomAgregada[i,j]
        vectorSumaColumna[i]+= matrizDomAgregada[j,i]

  print('vector suma fila', vectorSumaFila)
  print('vector suma columna', vectorSumaColumna)
  #Construcción del grafo
  

electre(np.array([[1,5],[4,2],[3,3]]),[0.5,0.5],np.array(["deseable", "deseable"]),0.5,0.5)
