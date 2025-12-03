def obtener_contrasenas_prohibidas():
    """Devuelve lista de contraseñas prohibidas (débiles)"""
    return [
        # Contraseñas más comunes del mundo
        "123456", "password", "12345678", "qwerty", "123456789",
        "12345", "1234", "111111", "1234567","123123", "abc123",
        "696969", "666666",
        # Otras contraseñas débiles
        "welcome", "login", "pass","qwerty123",
        "pass123", "password1", "password123",
        # Secuencias simples
        "abcdef", "qwertyuiop", "asdfghjkl", "zxcvbnm",
        # Años comunes
        "2020", "2021", "2022", "2023", "2024", "2025",
        # Nombres comunes
        "jesus", "michael", "jennifer", "robert", "john",
        # Patrones de teclado
        "1qaz2wsx", "1q2w3e4r", "qazwsx"
    ]
    
def es_contrasena_permitida(contrasena):
    """Verifica si una contraseña NO está en la lista prohibida"""
    contrasena_lower = contrasena.lower()
    
    # 1. Verificar contraseñas completas prohibidas
    contrasenas_prohibidas = obtener_contrasenas_prohibidas()
    if contrasena_lower in contrasenas_prohibidas:
        return False, "Contraseña demasiada común, intente denuevo."
    
    # 2. Verificar si es solo números (demasiado simple)
    if contrasena.isdigit() and len(contrasena) < 10:
        return False, "SOLO NÚMEROS (demasiado predecible)"
    
    # 3. Verificar si es solo letras (sin números ni símbolos)
    if contrasena.isalpha() and len(contrasena) < 12:
        return False, "SOLO LETRAS (agrega números o símbolos)"
    
    # 4. Verificar repetición excesiva de un mismo carácter
    if len(contrasena) >= 3:
        for i in range(len(contrasena) - 2):
            if contrasena[i] == contrasena[i+1] == contrasena[i+2]:
                return False, "MUCHAS REPETICIONES DEL MISMO CARÁCTER"
    
    return True, "Contraseña permitida"

def analizar_fortaleza(contrasena):
    """Analiza la fortaleza de una contraseña"""
    
    # Primero verificar si está permitida
    permitida, mensaje = es_contrasena_permitida(contrasena)
    if not permitida:
        return "PROHIBIDA - " + mensaje
    
    puntaje = 0
    
    # 1. Verificar longitud
    longitud = len(contrasena)
    if longitud >= 16:
        puntaje += 4
    elif longitud >= 12:
        puntaje += 3
    elif longitud >= 8:
        puntaje += 2
    elif longitud >= 6:
        puntaje += 1
    
    # 2. Verificar mayúsculas
    if any(c.isupper() for c in contrasena):
        puntaje += 1
    
    # 3. Verificar minúsculas
    if any(c.islower() for c in contrasena):
        puntaje += 1
    
    # 4. Verificar números
    if sum(c.isdigit() for c in contrasena) >= 2:
        puntaje += 2
    elif any(c.isdigit() for c in contrasena):
        puntaje += 1
    
    # 5. Verificar símbolos
    simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    if sum(c in simbolos for c in contrasena) >= 2:
        puntaje += 3
    elif any(c in simbolos for c in contrasena):
        puntaje += 2
    
    # 6. Verificar mezcla de tipos de caracteres
    tipos = 0
    if any(c.islower() for c in contrasena):
        tipos += 1
    if any(c.isupper() for c in contrasena):
        tipos += 1
    if any(c.isdigit() for c in contrasena):
        tipos += 1
    if any(c in simbolos for c in contrasena):
        tipos += 1
    
    if tipos >= 4:
        puntaje += 2
    elif tipos >= 3:
        puntaje += 1
    
    # 7. Penalizar información personal común
    info_personal = ["nombre", "apellido", "cumple", "nacim", "mascota", "ciudad"]
    contrasena_lower = contrasena.lower()
    for palabra in info_personal:
        if palabra in contrasena_lower:
            puntaje -= 1
    
    # Determinar fortaleza basada en puntaje
    if puntaje <= 3:
        return "Débil"
    elif puntaje <= 6:
        return "Media"
    elif puntaje <= 9:
        return "Fuerte"
    else:
        return "Muy fuerte"

def verificar_y_bloquear_contrasena(contrasena):
    """
    Verifica y bloquea contraseñas prohibidas.
    Devuelve: (es_valida, mensaje, fortaleza)
    """
    # Primero verificar si está permitida
    permitida, mensaje = es_contrasena_permitida(contrasena)
    
    if not permitida:
        return False, mensaje, "PROHIBIDA"
    
    # Si está permitida, analizar fortaleza
    fortaleza = analizar_fortaleza(contrasena)
    
    # Si es débil, preguntar si quiere continuar
    if fortaleza == "Débil":
        return True, "Contraseña débil detectada", fortaleza
    
    return True, "Contraseña aceptada", fortaleza