def palindrome_product(n):
    """
    Returns the largest palindrome that is the product of two n-digit numbers.
    """
    max_limit = 10**n - 1  # Mayor número de n dígitos
    min_limit = 10**(n-1)  # Menor número de n dígitos
    largest_palindrome = 0

    # Recorremos los dos números de n dígitos en orden descendente
    for a in range(max_limit, min_limit - 1, -1):
        for b in range(a, min_limit - 1, -1):  # No necesitamos repetir cálculos simétricos
            product = a * b
            if str(product) == str(product)[::-1]:  # Verificamos si el producto es un palíndromo
                if product > largest_palindrome:   # Actualizamos el mayor palíndromo encontrado
                    largest_palindrome = product

    return largest_palindrome

# Ejemplo de uso
print(palindrome_product(3))  # Encuentra el mayor palíndromo de dos números de 3 dígitos
