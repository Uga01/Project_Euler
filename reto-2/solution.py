def fibonacci(limit):
    list_fibonacci = [0, 1]  # Inicializamos la lista con los primeros dos términos
    while list_fibonacci[-1] + list_fibonacci[-2] < limit:  # Generamos hasta alcanzar el límite
        list_fibonacci.append(list_fibonacci[-1] + list_fibonacci[-2])
    
    # Filtramos los números pares y calculamos la suma
    return sum([x for x in list_fibonacci if x % 2 == 0])

# Llamada a la función con el límite de 4 millones
print(fibonacci(4000000))
