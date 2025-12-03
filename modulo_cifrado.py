# Método 1: Cifrado César
def cifrar_cesar(texto, desplazamiento=3):
    """Cifra un texto usando el método César"""
    texto_cifrado = ""
    for caracter in texto:
        if caracter.isalpha():
            ascii_base = ord('A') if caracter.isupper() else ord('a')
            nuevo_caracter = chr((ord(caracter) - ascii_base + desplazamiento) % 26 + ascii_base)
            texto_cifrado += nuevo_caracter
        else:
            texto_cifrado += caracter
    return texto_cifrado

def descifrar_cesar(texto_cifrado, desplazamiento=3):
    """Descifra un texto cifrado con César"""
    return cifrar_cesar(texto_cifrado, -desplazamiento)

# Método 2: Cifrado Recursivo
def invertir_cadena_recursivo(cadena):
    """Invierte una cadena usando recursividad"""
    if len(cadena) == 0:
        return ""
    else:
        return invertir_cadena_recursivo(cadena[1:]) + cadena[0]

def cifrado_recursivo_completo(contrasena, desplazamiento=3):
    """Aplica cifrado recursivo completo"""
    # Paso 1: Invertir la contraseña recursivamente
    contrasena_invertida = invertir_cadena_recursivo(contrasena)
    
    # Paso 2: Aplicar cifrado César
    contrasena_cifrada = cifrar_cesar(contrasena_invertida, desplazamiento)
    
    return contrasena_cifrada

def descifrado_recursivo_completo(contrasena_cifrada, desplazamiento=3):
    """Descifra una contraseña cifrada con el método recursivo"""
    # Paso 1: Descifrar César
    contrasena_invertida = descifrar_cesar(contrasena_cifrada, desplazamiento)
    
    # Paso 2: Volver a invertir (deshacer la inversión)
    contrasena_original = invertir_cadena_recursivo(contrasena_invertida)
    
    return contrasena_original

def seleccionar_metodo_cifrado():
    """Permite al usuario seleccionar método de cifrado"""
    print("\n          SELECCIONAR MÉTODO DE CIFRADO\n ")
    print("1. Cifrado César (simple)")
    print("2. Cifrado Recursivo (avanzado)")
    
    while True:
        opcion = input("\nSeleccione método (1-2): ")
        if opcion in ["1", "2"]:
            return int(opcion)
        print("Opción no válida. Intente nuevamente.")

def aplicar_cifrado(contrasena, metodo, cifrar=True):
    """Aplica cifrado o descifrado según el método seleccionado"""
    if metodo == 1:
        if cifrar:
            return cifrar_cesar(contrasena, 3)
        else:
            return descifrar_cesar(contrasena, 3)
    elif metodo == 2:
        if cifrar:
            return cifrado_recursivo_completo(contrasena, 3)
        else:
            return descifrado_recursivo_completo(contrasena, 3)
    return contrasena