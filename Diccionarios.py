'''los diccionarios son variables especiales 
que me permiten almacenar multiples datos de diferentes tipos en una sola variable
le ingreso atributos:  ejemplo:  nombre, cedula ETC
y el valor seria la pareja que acompaña el atributo

si para acceder a un elemento de una posicion colocaba el numeros 

'''

empleado = { 
    'nombre':"Jose",
    'cedula':89473290478123,
    'cargo': "Analista de datos",
    'salario':7000000,
    'Horas trabajadas a la semana':48,
    'aplica subsidio de transporte':False,
    'deudas':[1500000,800000]
    }

print(empleado)
print(empleado['nombre'])
print(empleado['deudas'])
print(empleado['deudas'][1])


#recorriendo un diccionario:
#recorres objetos en un ciclo FOR y solo con FOR

for observadordeAtributo, observadorValor in empleado.items(): # le colocamos las dos variables porque en el diccionario va el  atributo y el valor ingresadp
    print(observadordeAtributo)
    print(observadorValor)