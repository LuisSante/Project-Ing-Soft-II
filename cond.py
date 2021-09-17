import numpy as np
def NuevaMatriz(f,c):
    matriz=[]
    for i in range(f):
        matriz.append([0]*c)
    return matriz

def LLmatriz():
    f = int(input("Numero de filas: "))
    c = int(input("Numero de columnas: "))
    matriz=NuevaMatriz(f,c)
    for i in range (f):
        for j in range(c):
            matriz[i][j]=float(input("Elemento: "))
    return matriz

def mostrar(M,f,c):
    for i in range (f):
        for j in range (c):
            print(M[i][j], end="\t")
        print()

def hilb():
    n = int (input("N: "))
    matrizH = NuevaMatriz(n,n)
    for i in range (n):
        for j in range (n):
            matrizH[i][j] = 1/((i+1)+(j+1)-1)
    return matrizH

def vector(I, F=None, S=None):
  while True:
    if S > 0 and I > F:
      break
    elif S < 0 and I < F:
      break
    yield (I)
    I = I + S

def vander():
  i = float (input("Inicio: "))
  f = float (input("Final: "))
  s = float (input("Salto: "))
  V=list(vector(i, f, s))
  V = np.array(V)
  n = len(V)
  matrizV= NuevaMatriz(n,n)
  for i in range(n):
    for j in range(n):
      potencia = (n-1)-j
      matrizV[i][j] = V[i]**potencia
  return matrizV     

def metodo(matriz):
    while not 4:
        print ("1. Num de condicionamiento de la norma 1")
        print ("2. Num de condicionamiento de la norma 2")
        print ("3. Num de condicionamiento de la norma inf")
        print ("4. Salir")
        opcion = int(input("Opcion: "))
        if opcion == 1:
            print(np.linalg.cond(matriz,1))
        elif opcion == 2:
            print(np.linalg.cond(matriz,2))
        elif opcion == 3:
            print(np.linalg.cond(matriz,np.inf))
        elif opcion == 4:
            break

while not 4:
    print ("1. Usar matriz de Hilbert")
    print ("2. Usar matriz de Valdermonde")
    print ("3. Usar otra matriz")
    print ("4. Salir")
    opcion = int(input("Opcion: "))
    if opcion == 1:
        matriz=hilb()
        print("MATRIZ DE HILBERT")
        mostrar(matriz,len(matriz),len(matriz))
        metodo(matriz)
    elif opcion == 2:
        matriz=vander()
        print("MATRIZ DE VANDERMONDE")
        mostrar(matriz,len(matriz),len(matriz))
        metodo(matriz)
    elif opcion == 3:
        matriz=LLmatriz()
        print("MATRIZ")
        mostrar(matriz,len(matriz),len(matriz))
        metodo(matriz)
    elif opcion == 4:
        break