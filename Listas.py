'''
listas o arreglos de datos
utiles para almacenar mas de un datos en una sola variables 

nos permite guardar muchas variables en una posicion de memoria, es decir todos de un mismo tipo de datos
no de datos diferentes en cada arreglo
cada dato dentro del arreglo se llama elementos, el cual tiene una posicion o su indice
creamos una variables
'''
numero = [1,2,3,4,5]
nombres = ["Juan","Sara","Carlos","Catalina"]

print(numero) #con este me imprime todo lo que hay en el arreglo

print(numero[0]) #con este me imprime SOLO lo que hay en LA POSICION CERO

#recorrer  o  iterar una lista, un vector o un arreglo
#tener una rutina repetidiva para que muestra los datos uno a uno sin que yo tenga darle algo raro
#se recorre una lista usando un FOR
#le ponemos igualmente una variable de control
'''  variable auxilia IN y la lista  '''
for observador in numero:
    print(observador+10)

for observador in nombres:
    print(observador,"llego tarde")