import numpy
m = int(input("Valor de m:"))
n = int(input("Valor de n:"))
matrix = numpy.zeros((m,n))
#vector = numpy.zeros((n))
x=numpy.zeros((m))
print("Introduce la matriz de coeficientes y el vector solución")
for r in range(0,m):#r = raw c = column
    for c in range(0,n):
        matrix[(r),(c)]=(input("Elemento a["+str(r+1)+","+str(c+1)+"] "))
    #2vector[(r)]=(input("b["+str(r+1)+"]: "))
print(matrix)

print(numpy.linalg.cond(matrix))