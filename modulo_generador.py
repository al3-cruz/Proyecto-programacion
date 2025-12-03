import random
import string

def generar_contrasena_segura():
    """Genera una contraseña segura basada en preferencias"""
    print("\n          GENERAR CONTRASEÑA SEGURA\n ")
    
    # Solicitar preferencias
    while True:
        try:
            longitud = int(input("Longitud de contraseña (8-32): "))
            if 8 <= longitud <= 32:
                break
            print("Longitud debe ser entre 8 y 32 caracteres")
        except ValueError:
            print("Ingrese un número válido")
    
    print("\nOpciones de complejidad:")
    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'
    
    # Definir conjuntos de caracteres
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase if incluir_mayusculas else ""
    numeros = string.digits if incluir_numeros else ""
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?" if incluir_simbolos else ""
    
    # Combinar todos los caracteres disponibles
    todos_caracteres = minusculas + mayusculas + numeros + simbolos
    
    # Verificar que haya al menos un conjunto seleccionado
    if not todos_caracteres:
        print("Debe seleccionar al menos un tipo de caracter")
        return "Error: No hay caracteres disponibles"
    
    # Asegurar al menos un caracter de cada tipo seleccionado
    contrasena = []
    
    if incluir_mayusculas:
        contrasena.append(random.choice(mayusculas))
    if incluir_numeros:
        contrasena.append(random.choice(numeros))
    if incluir_simbolos:
        contrasena.append(random.choice(simbolos))
    
    # Completar con caracteres aleatorios
    while len(contrasena) < longitud:
        contrasena.append(random.choice(todos_caracteres))
    
    # Mezclar la contraseña
    random.shuffle(contrasena)
    
    # Convertir a string
    contrasena_generada = ''.join(contrasena)
    
    # Mostrar fortaleza
    import modulo_analizador
    fortaleza = modulo_analizador.analizar_fortaleza(contrasena_generada)
    
    print(f"\n Contraseña generada: {contrasena_generada}")
    print(f" Fortaleza: {fortaleza}")
    
    return contrasena_generada