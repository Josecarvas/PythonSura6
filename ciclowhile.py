#ciclo mientras


#declarar una variable centinela y de control para evaluar la ejecucion de mi ciclo

#i=0
# despues de declarar la variable que controla, programo la estructura del ciclo while
#while(i!=5):
#    i=int(input("Digite un numero: "))
#    print("Estoy saltando cuerda",i)
#print("Terminamos de saltar")

#i=i+1  #asi es un contador en PY

# vamos a hacer un cicclo con un menu de opciones:
#siempre inicializo la variables
'''
i=0

#Menu de opciones

print("*****Menu****")
print("1. saluda")
print("2. despedir")
print("3. contar quien gano el clasico")
print("4. contar si esta lloviendo")
print("5. salir")

while(i!=5):
    i=int(input("Digite un opcion del Menu: "))
    if(i==1):
        print("Hola Como Estas")
    elif(i==2):
        print("Chao que te vaya bien")
    elif(i==3):
        print("El DIM Gano")
    elif(i==4):
        print("no esta lloviendo todavia")
    elif(i==5):
        print("hasta pronto")
        break
    else:
        print("ingresa una opcion valida")

print("terminamos de saltar")

'''
from ast import Raise
import math


i=0
Num1 =0
Num2 =0
suma =0
resta =0
raiz =0
multiplicacion =0

print("*****Menu****")
print("1. sumar dos numeros")
print("2. restar dos numeros")
print("3. encontrar la raiz de un numero")
print("4. multiplicar dos numeros")
print("5. salir")

while(i!=5):
    i=int(input("Digite un opcion del Menu: "))
    if(i==1):
        num1=int(input("Digite un Numero: "))
        num2=int(input("Digite un Numero: "))
        suma= num1 + num2
        print("la suma de los numeros ingresados es ",suma)

    elif(i==2):
        num1=int(input("Digite un Numero: "))
        num2=int(input("Digite un Numero: "))
        resta=num1-num2
        print("la suma de los numeros ingresados es ",resta)

    elif(i==3):
        num1=int(input("Digite un Numero: "))
        raiz = math.sqrt(num1)
        print("la Raiz cuadrada del numero ingresado es ",raiz)
    elif(i==4):
        num1=int(input("Digite un Numero: "))
        num2=int(input("Digite un Numero: "))
        multiplicacion = num1 * num2
        print("la suma de los numeros ingresados es ",multiplicacion)

    elif(i==5):
        print("hasta pronto")
        break
    else:
        print("ingresa una opcion valida")

print("terminamos de saltar")