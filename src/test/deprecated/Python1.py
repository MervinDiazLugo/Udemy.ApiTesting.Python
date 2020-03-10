#imprimir

Nombre  = "Mervin Alberto"
Nombre2  = "Antony Jose"
print (f'Hola {str(Nombre)}')


#Trabajando con Arreglos
array = ['Venezuela', 'Argentina', 'Chile', 'Perú']

#añadir un valor a un arreglo
array.append('Bolivia')

#print (array[4])
i = 0
for pais in array:
    print(pais)

    if pais == "Argentina":
        print(f'{Nombre}, vive en {pais}')
        #break #romper con el loop
        continue #pasa al siguiente elemento

    if pais == "Chile":
        array[i] = "Aguante la educación Gratuita en Chile!"
        print(array[i])
        #break #romper con el loop
        continue #pasa al siguiente elemento

    if pais == "Perú":
        print(f'{Nombre2}, vive en {pais}')
        break
    i++1

#Validar =  isinstance(array, list)

#Trabajando con diccionarios

diccionario = {'nombre' : 'Carlos', 'edad' : 22, 'cursos': ['Python','Django','JavaScript'] }

Nombre = diccionario['nombre']

print (f'Hola {Nombre}!')

diccionario['nombre'] = 'MySQuality'

Nombre = diccionario['nombre']
print (diccionario)

#Validar =  isinstance(dicc, dict)
