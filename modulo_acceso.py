import modulo_cifrado
import modulo_log
import os

# Constantes
MAX_INTENTOS = 3
ARCHIVO_MAESTRO = "datos/maestro.dat"

def inicializar_sistema():
    """Inicializa el sistema si es la primera vez"""
    if not os.path.exists("datos"):
        os.makedirs("datos")
    
    # Si no existe archivo maestro, crear uno por defecto
    if not os.path.exists(ARCHIVO_MAESTRO):
        contrasena_por_defecto = "Admin123!"
        contrasena_cifrada = modulo_cifrado.cifrar_cesar(contrasena_por_defecto, 3)
        
        with open(ARCHIVO_MAESTRO, "w") as archivo:
            archivo.write(contrasena_cifrada)
        
        print("\n Sistema inicializado con contraseña maestra por defecto.")
        print("Contraseña: Admin123!")
        print("¡Cámbiala inmediatamente por seguridad!")

def autenticar_usuario():
    """Autentica al usuario con contraseña maestra"""
    inicializar_sistema()
    
    intentos = 0
    
    # Cargar contraseña maestra cifrada
    with open(ARCHIVO_MAESTRO, "r") as archivo:
        contrasena_maestra_cifrada = archivo.read().strip()
    
    # Descifrar para comparación
    contrasena_maestra_real = modulo_cifrado.descifrar_cesar(contrasena_maestra_cifrada, 3)
    
    while intentos < MAX_INTENTOS:
        print("\n          AUTENTICACIÓN REQUERIDA\n")
        
        contrasena_ingresada = input("Ingrese contraseña maestra: ")
        
        if contrasena_ingresada == contrasena_maestra_real:
            print("\n Acceso concedido")
            return True
        else:
            intentos += 1
            intentos_restantes = MAX_INTENTOS - intentos
            print(f"\n Contraseña incorrecta. Intentos restantes: {intentos_restantes}")
            modulo_log.registrar_accion(f"Intento fallido de acceso ({intentos}/{MAX_INTENTOS})")
    
    print(f"\n ¡Demasiados intentos fallidos! Sistema bloqueado.")
    return False

def cambiar_contrasena_maestra():
    """Permite cambiar la contraseña maestra"""
    print("\n          CAMBIAR CONTRASEÑA MAESTRA\n")
    
    # Verificar contraseña actual
    contrasena_actual = input("Contraseña actual: ")
    
    with open(ARCHIVO_MAESTRO, "r") as archivo:
        contrasena_cifrada = archivo.read().strip()
    
    contrasena_real = modulo_cifrado.descifrar_cesar(contrasena_cifrada, 3)
    
    if contrasena_actual != contrasena_real:
        print("\n Contraseña actual incorrecta")
        return False
    
    # Solicitar nueva contraseña
    nueva_contrasena = input("Nueva contraseña: ")
    confirmar = input("Confirmar nueva contraseña: ")
    
    if nueva_contrasena != confirmar:
        print("\n Las contraseñas no coinciden")
        return False
    
    # Guardar nueva contraseña cifrada
    nueva_cifrada = modulo_cifrado.cifrar_cesar(nueva_contrasena, 3)
    
    with open(ARCHIVO_MAESTRO, "w") as archivo:
        archivo.write(nueva_cifrada)
    
    print("\n Contraseña maestra cambiada exitosamente")
    modulo_log.registrar_accion("Contraseña maestra cambiada")
    return True