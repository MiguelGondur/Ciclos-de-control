#coding = utf-8

#peograma que imprima los numeros del 1 al 10 de forma ascendente
print('programa que visualiza los numeros del 1 al 10 \n')

#partes de un ciclo de contorl 
#1. Variable de control y su asignacion inicial
#2. condicion del ciclo que hace que mientras sea verdadero se ejecute
#3. Sentencia de salida del ciclo

numero = 1 #variable de control

while numero <= 10: #condicion del ciclo
  #accion que se repetira mientras la condicion sea verdadera
  print(numero)
  numero = numero + 1 #sentencia de salida del ciclo
print('\n fin del programa, la variable numero es: ',numero)

#Programa que imprima los numeros del 1 al 10 de forma descendente
print('programa que visualiza los numeros del 10 al 1 \n')

numero = 10 #variable de control

while numero >=1: #condicion del ciclo
  #accion que se repetira mientras la condicion sea verdadera
  print(numero)
  numero = numero - 1 #sentencia de salida del ciclo
print('\n fin del programa, la variable numero es: ',numero)

#Programa que imprima los primeros 12 multiplos de 7
print('programa que visualiza los multiplos de 7 \n')

total_multiplos = int(input('ingrse la cantidad de multiplos'))#condiocion del ciclo
contador = 1 #variable de control

if total_multiplos > 0:
  contador = 1
  while contador <= total_multiplos: #condicion del ciclo
    #accion que se repetira mientras la condicion sea verdadera
    print(f'7 x {contador} = {contador * 7}')
    contador += 1 #sentencia de salida del ciclo
else:
  print('la cantidad de multiplos debe ser mayor a 0')

# generar patrones en forma de arbolitos
  print('programa que genera patrones en forma de arbolitos \n')

print('primer arbolito: ladeado a la izquierda')

ramas = 1 #variable de control

while ramas <= 10: #condicion del ciclo
  print('*' * ramas)
  ramas += 1 #sentencia de salida del ciclo

#Programa generar patrones en forma de arbolitos
print('programa que genera patrones en forma de arbolitos \n')

#Segundo arbolito: ladeado a la izquierda
print('Segundo arbolito: ladeado a la derecha, ascendente')

ramas = 1 #variable de control
total_espacios = 9

while ramas <= 10: #condicion del ciclo
  
  print((' ' * total_espacios) + ('*' * ramas))
  ramas += 1 #sentencia de salida del ciclo
  total_espacios -= 1

#tercer arbolito: ladeado a la izquierda, descendente
print ('\n tercer arbolito: ladeado a la izq, descendente')

ramas = 10

while ramas >= 1: #condicion del ciclo
  print('*' * ramas)
  ramas -= 1 #sentencia de salida del ciclo

# Cuarto arbolito: ladeado a la izq, descendente
print ('\n cuarto arbolito: ladeado a la derecha, descendente')

ramas = 10 #variable de control
total_espacios = 0

while ramas >= 1: #condicion del ciclo
  print((' ' * total_espacios) + ('*' * ramas))
  ramas -= 1 #sentencia de salida del ciclo
  total_espacios += 1

# Quinto arbolito: ladeado a la izquierda, descendente
print ('\n quinto arbolito: centrado ascentente')
ramas = 1 #variable de control
total_espacios = 10
while ramas <= 20: #condicion del ciclo
  print((' ' * total_espacios) + ('*' * ramas))
  ramas += 2 #sentencia de salida del ciclo
  total_espacios -= 1

# Sexto arbolito: centrado descendente
print ('\n sexto arbolito: centrado descendente')
ramas = 19 #variable de control
total_espacios = 0
while ramas >=1: #condicion del ciclo
  print((' ' * total_espacios) + ('*' * ramas))
  ramas -= 2 #sentencia de salida del ciclo
  total_espacios += 1
