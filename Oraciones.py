def vocales(frase):
    for car in frase:
        if car in('a','e','i','o','u'):
           print(car)

oracion = input('Ingrese oracion: ')
vocales(oracion.lower())

