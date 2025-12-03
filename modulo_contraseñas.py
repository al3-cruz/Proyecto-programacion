import modulo_cifrado
import modulo_analizador
import modulo_log
import datetime
import pickle
import os

ARCHIVO_CONTRASEÑAS = "datos/contraseñas.bin"

def cargar_contrasenas():
    """Carga las contraseñas desde archivo binario"""
    contrasenas = []
    
    if os.path.exists(ARCHIVO_CONTRASEÑAS):
        try:
            with open(ARCHIVO_CONTRASEÑAS, "rb") as archivo:
                contrasenas = pickle.load(archivo)
            print(f"\n Cargadas {len(contrasenas)} contraseñas")
        except:
            print("\n Error al cargar contraseñas. Se creará nueva lista.")
            contrasenas = []
    else:
        print("\n📭 No se encontraron contraseñas guardadas")
    
    return contrasenas

def guardar_contrasenas(contrasenas):
    """Guarda las contraseñas en archivo BIN y TXT"""
    
    # Verificar que contrasenas no sea None
    if contrasenas is None:
        print("  Error: No hay datos para guardar")
        return False
    
    try:
        # Crear carpeta si no existe
        if not os.path.exists("datos"):
            os.makedirs("datos")
        
        # Guardar en BIN
        with open(ARCHIVO_CONTRASEÑAS, "wb") as archivo_bin:
            pickle.dump(contrasenas, archivo_bin)
        
        # Guardar también en TXT (backup legible)
        with open("datos/contraseñas.txt", "w", encoding="utf-8") as archivo_txt:
            archivo_txt.write("\n SAFEKEY VAULT+ - REGISTRO DE CONTRASEÑAS\n")
            archivo_txt.write(f"Fecha de exportación: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            
            if not contrasenas:
                archivo_txt.write("No hay contraseñas almacenadas.\n")
            else:
                for i, item in enumerate(contrasenas, 1):
                    archivo_txt.write(f"REGISTRO #{i}\n")
                    archivo_txt.write(f"Servicio: {item.get('servicio', 'N/A')}\n")
                    archivo_txt.write(f"Usuario: {item.get('usuario', 'N/A')}\n")
                    archivo_txt.write(f"Contraseña CIFRADA: {item.get('contrasena', 'N/A')}\n")
                    archivo_txt.write(f"Método: {item.get('metodo', 'N/A')}\n")
                    archivo_txt.write(f"Fecha: {item.get('fecha', 'N/A')}\n")
                    archivo_txt.write(f"Fortaleza: {item.get('fortaleza', 'N/A')}\n")
                    archivo_txt.write("-"*40 + "\n\n")
        
        print(f"\n {len(contrasenas)} contraseña(s) guardada(s) en BIN y TXT")
        return True
        
    except Exception as e:
        print(f" Error al guardar: {e}")
        return False

def mostrar_contrasenas(contrasenas):
    """Muestra todas las contraseñas almacenadas"""
    if not contrasenas:
        print("\n No hay contraseñas guardadas")
        return
    
    print("\n          CONTRASEÑAS ALMACENADAS\n")
    
    for i, registro in enumerate(contrasenas, 1):
        print(f"\n{i}. Servicio: {registro['servicio']}")
        print(f"   Usuario: {registro['usuario']}")
        print(f"   Fecha: {registro['fecha']}")
        print(f"   Método: {'César' if registro['metodo'] == 1 else 'Recursivo'}")
        
        # Preguntar si quiere ver la contraseña
        mostrar = input(f"   ¿Mostrar contraseña? (s/n): ").lower()
        if mostrar == 's':
            contrasena_descifrada = modulo_cifrado.aplicar_cifrado(
                registro['contrasena'], 
                registro['metodo'], 
                cifrar=False
            )
            print(f"  Contraseña: {contrasena_descifrada}")
            
def agregar_contrasena(contrasenas):
    """Agrega una nueva contraseña al sistema - VERSIÓN COMPLETA"""
    print("\n         AGREGAR NUEVA CONTRASEÑA\n")
    
    # Solicitar datos básicos
    servicio = input("Nombre del servicio (ej: Gmail): ").strip()
    usuario = input("Usuario/Correo: ").strip()
    
    # Solicitar contraseña con validación
    while True:
        contrasena = input("Contraseña: ").strip()
        
        # Verificar y bloquear contraseñas prohibidas
        es_valida, mensaje, fortaleza = modulo_analizador.verificar_y_bloquear_contrasena(contrasena)
        
        if not es_valida:
            print(f"\n {mensaje}")
            print(" Esta contraseña NO está permitida.")
            opcion = input("¿Intentar con otra contraseña? (s/n): ").lower()
            if opcion != 's':
                print("Operación cancelada")
                return contrasenas
            continue
        
        print(f"\n Fortaleza: {fortaleza}")
        
        # Si es débil, preguntar si quiere continuar
        if fortaleza == "Débil":
            print(" ADVERTENCIA: Contraseña débil detectada")
            print(" Recomendación: Use al menos 8 caracteres con mayúsculas, números y símbolos")
            continuar = input("¿Continuar con esta contraseña débil? (s/n): ").lower()
            if continuar != 's':
                print("   Ingrese una nueva contraseña...")
                continue
        
        # Si llegamos aquí, la contraseña es aceptable
        break
    
    # Seleccionar método de cifrado
    metodo = modulo_cifrado.seleccionar_metodo_cifrado()
    
    # Cifrar contraseña
    contrasena_cifrada = modulo_cifrado.aplicar_cifrado(contrasena, metodo, cifrar=True)
    
    # Crear registro
    nuevo_registro = {
        'servicio': servicio,
        'usuario': usuario,
        'contrasena': contrasena_cifrada,
        'metodo': metodo,
        'fecha': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'fortaleza': fortaleza
    }
    
    # Agregar a la lista
    contrasenas.append(nuevo_registro)
    
    # Guardar cambios
    guardar_contrasenas(contrasenas)
    
    print(f"\n Contraseña para '{servicio}' agregada exitosamente")
    modulo_log.registrar_accion(f"Agregada contraseña para {servicio}")
    
    return contrasenas

def editar_contrasena(contrasenas):
    """Edita una contraseña existente"""
    if not contrasenas:
        print("\n No hay contraseñas para editar")
        return contrasenas
    
    # Mostrar servicios disponibles
    print("\n Servicios disponibles:")
    for i, registro in enumerate(contrasenas, 1):
        print(f"{i}. {registro['servicio']} ({registro['usuario']})")
    
    try:
        indice = int(input("\nSeleccione número a editar: ")) - 1
        
        if 0 <= indice < len(contrasenas):
            registro = contrasenas[indice]
            
            print(f"\n  Editando: {registro['servicio']}")
            print(f"Usuario actual: {registro['usuario']}")
            
            # Mostrar contraseña actual (descifrada)
            mostrar = input("¿Ver contraseña actual? (s/n): ").lower()
            if mostrar == 's':
                contrasena_actual = modulo_cifrado.aplicar_cifrado(
                    registro['contrasena'], 
                    registro['metodo'], 
                    cifrar=False
                )
                print(f"Contraseña actual: {contrasena_actual}")
            
            # Solicitar nuevos datos
            nuevo_servicio = input(f"Nuevo nombre servicio [{registro['servicio']}]: ").strip()
            nuevo_usuario = input(f"Nuevo usuario [{registro['usuario']}]: ").strip()
            nueva_contrasena = input("Nueva contraseña (dejar vacío para no cambiar): ").strip()
            
            # Actualizar campos si se ingresaron nuevos valores
            if nuevo_servicio:
                registro['servicio'] = nuevo_servicio
            if nuevo_usuario:
                registro['usuario'] = nuevo_usuario
            if nueva_contrasena:
                # Cifrar nueva contraseña
                registro['contrasena'] = modulo_cifrado.aplicar_cifrado(
                    nueva_contrasena, 
                    registro['metodo'], 
                    cifrar=True
                )
                registro['fortaleza'] = modulo_analizador.analizar_fortaleza(nueva_contrasena)
            
            registro['fecha'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Guardar cambios
            guardar_contrasenas(contrasenas)
            print(f"\n Contraseña actualizada exitosamente")
            modulo_log.registrar_accion(f"Editada contraseña para {registro['servicio']}")
        else:
            print("\n Índice fuera de rango")
    except ValueError:
        print("\n Entrada no válida")
    
    return contrasenas

def eliminar_contrasena(contrasenas):
    """Elimina una contraseña del sistema"""
    if not contrasenas:
        print("\n No hay contraseñas para eliminar")
        return contrasenas
    
    # Mostrar servicios disponibles
    print("\n Servicios disponibles:")
    for i, registro in enumerate(contrasenas, 1):
        print(f"{i}. {registro['servicio']} ({registro['usuario']})")
    
    try:
        indice = int(input("\nSeleccione número a eliminar: ")) - 1
        
        if 0 <= indice < len(contrasenas):
            servicio = contrasenas[indice]['servicio']
            confirmar = input(f"¿Eliminar '{servicio}'? (s/n): ").lower()
            
            if confirmar == 's':
                eliminado = contrasenas.pop(indice)
                guardar_contrasenas(contrasenas)
                print(f"\n Contraseña para '{servicio}' eliminada")
                modulo_log.registrar_accion(f"Eliminada contraseña para {servicio}")
            else:
                print("\n Operación cancelada")
        else:
            print("\n Índice fuera de rango")
    except ValueError:
        print("\n Entrada no válida")
    
    return contrasenas