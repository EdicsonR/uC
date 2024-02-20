from array import array
# Representar una matriz 3x3 como un arreglo de 9 elementos
A = array("f",[])
#A=array("f",[1,2,3,4,5,6,7,8,9])
# Solicitar al usuario que ingrese 9 valores y agregarlos al arreglo
for i in range(9):
    valor = float(input("Ingrese un valor: "))
    A.append(valor)
print("La matriz A es :",A)
def element(A, i, j):
  if 0 <= i < 3 and 0 <= j < 3:
      # Calcular el índice en el arreglo basado en la posición (i, j) en la matriz
      indice = i * 3 + j
      # Devolver el elemento en la posición (i, j)
      return A[indice]
  else:
      # Manejar el caso en el que los índices estén fuera de rango
      return None
elemento_00 = element(A, 0, 0)
elemento_01=element(A,0,1)
elemento_02 = element(A, 0,2)
elemento_10 = element(A, 1, 0)
elemento_11 = element(A, 1, 1)
elemento_12=element(A,1,2)
elemento_20 = element(A, 2, 0)
elemento_21 = element(A, 2, 1)
elemento_22 = element(A, 2, 2)
print("Elemento (0, 0):", elemento_00)
print("Elemento (0, 1):", elemento_01)
print("Elemento (0, 2):", elemento_02)
print("Elemento (1, 0):", elemento_10)
print("Elemento (1, 1):", elemento_11)
print("Elemento (1, 2):", elemento_12)
print("Elemento (2, 0):", elemento_20)
print("Elemento (2, 1):", elemento_21)
print("Elemento (2, 2):", elemento_22)

#Intercambio de Reglones
def CambioReglon():
  print("si desea cambiar el reglon 0 con el 1, ingrese 1")
  print("si desea cambiar el reglon 0 con el 2, ingrese 2")
  print("si desea cambiar el reglon 1 con el 2, ingrese 3")
  i = input("¿Que desea hacer? ")
  if i == "1":
    A[0], A[3], A[1], A[4], A[2], A[5] = A[3], A[0], A[4], A[1], A[5], A[2]
    return A
  elif i=="2":
    A[0], A[6], A[1], A[7], A[2], A[8] = A[6], A[0], A[7], A[1], A[8], A[2]
    return A
  else: 
    A[3], A[6], A[4], A[7], A[5], A[8] = A[6], A[3], A[7], A[4], A[8], A[5]
    return A
print("Resultado de la matriz: ",CambioReglon())

#Multiplicacion por una constante
def MultiplicacionPorConstante():
  print("A continuacion se hara la multiplicacion de un reglon por una constante")
  a =float(input("Digite el valor de la constante a multiplicar "))
  global Reglon,A,resultado
  Reglon = int(input("Digite el reglon a multiplicar "))
  if Reglon == 0:
    resultado =array("f",[a * i for i in A[0:3]])
    A=resultado+A[3:9]
    return resultado
  elif Reglon ==1:
    resultado =array("f",[a * i for i in A[3:6]])
    A=A[0:3]+resultado+A[6:9]
    return resultado
  elif Reglon ==2:
    resultado =array("f",[a * i for i in A[6:9]])
    A=A[0:6]+resultado
    return resultado
  else:
    print("No se encuentra el vector")
    return 

print("El reglon ",Reglon,"queda ",MultiplicacionPorConstante())
print("La matriz resultantes es: ",A)

#Multiplicar y sumar en un reglon
def MultSuma():
  print("Ahora se multiplicara un reglon por una constante y se sumara en otro reglon (k*Ri+Rj=>Rj)")
  const=float(input("Inserte constante de multiplicacion "))
  reg=int(input("ingrese el reglon a multiplicar "))
  reglondes=int(input("A que reglon desea sumarlo "))
  if reg ==0:
    resultado1 =array("f",[const * i for i in A[0:3]])
    if reglondes==0:
      result=array("f",[x + y for x, y in zip(resultado1, A[0:3])])+A[3:9]
      return result
    elif reglondes==1:
      result=A[0:3]+array("f",[x + y for x, y in zip(resultado1, A[3:6])])+A[6:9]
      return result
    elif reglondes==2:
      result=A[0:6]+array("f",[x + y for x, y in zip(resultado1, A[6:9])])
      return result
    else:
      a=print("Resultado invalido")
      return a
  elif reg==1:
    resultado1=array("f",[const * i for i in A[3:6]])
    if reglondes==0:
      result=array("f",[x + y for x, y in zip(resultado1, A[0:3])])+A[3:9]
      return result
    elif reglondes==1:
      result=A[0:3]+array("f",[x + y for x, y in zip(resultado1, A[3:6])])+A[6:9]
      return result
    elif reglondes==2:
      result=A[0:6]+array("f",[x + y for x, y in zip(resultado1, A[6:9])])
      return result
    else:
      a=print("Resultado invalido")
      return a
  elif reg==2:
    resultado1=array("f",[const * i for i in A[6:9]])
    if reglondes==0:
      result=array("f",[x + y for x, y in zip(resultado1, A[0:3])])+A[3:9]
      return result
    elif reglondes==1:
      result=A[0:3]+array("f",[x + y for x, y in zip(resultado1, A[3:6])])+A[6:9]
      return result
    elif reglondes==2:
      result=A[0:6]+array("f",[x + y for x, y in zip(resultado1, A[6:9])])
      return result
    else:
      a=print("Resultado invalido")
      return a
print("La matriz queda: ",MultSuma())
