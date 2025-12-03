import modulo_cifrado

def buscar_contrasenas(contrasenas):
    """Busca contraseñas por diferentes criterios"""
    
    if not contrasenas:
        print("\n No hay contraseñas para buscar")
        return
    
    print(" \n         BÚSQUEDA DE CONTRASEÑAS\n")
    print("1. Por nombre de servicio")
    print("2. Por usuario/correo")
    print("3. Búsqueda recursiva (coincidencia parcial)\n ")
    
    opcion = input("Seleccione tipo de búsqueda: ")
    
    if opcion == "1":
        buscar_por_servicio(contrasenas)
    elif opcion == "2":
        buscar_por_usuario(contrasenas)
    elif opcion == "3":
        buscar_recursiva(contrasenas)
    else:
        print("Opción no válida")

def buscar_por_servicio(contrasenas):
    """Busca por nombre exacto del servicio"""
    termino = input("\n Ingrese nombre del servicio: ").lower()
    
    resultados = []
    for registro in contrasenas:
        if registro['servicio'].lower() == termino:
            resultados.append(registro)
    
    mostrar_resultados(resultados)

def buscar_por_usuario(contrasenas):
    """Busca por usuario o correo"""
    termino = input("\n Ingrese usuario/correo: ").lower()
    
    resultados = []
    for registro in contrasenas:
        if termino in registro['usuario'].lower():
            resultados.append(registro)
    
    mostrar_resultados(resultados)

def buscar_recursiva_auxiliar(contrasenas, termino, indice=0, resultados=None):
    """Función recursiva auxiliar para búsqueda"""
    if resultados is None:
        resultados = []
    
    # Caso base: terminamos de revisar todas las contraseñas
    if indice >= len(contrasenas):
        return resultados
    
    registro = contrasenas[indice]
    
    # Verificar coincidencia parcial en servicio o usuario
    if (termino in registro['servicio'].lower() or 
        termino in registro['usuario'].lower()):
        resultados.append(registro)
    
    # Llamada recursiva para el siguiente registro
    return buscar_recursiva_auxiliar(contrasenas, termino, indice + 1, resultados)

def buscar_recursiva(contrasenas):
    """Búsqueda recursiva por coincidencia parcial"""
    termino = input("\n Ingrese término de búsqueda: ").lower()
    
    resultados = buscar_recursiva_auxiliar(contrasenas, termino)
    mostrar_resultados(resultados)

def mostrar_resultados(resultados):
    """Muestra los resultados de búsqueda"""
    if not resultados:
        print("\n No se encontraron resultados")
        return
    
    print(f"\n Se encontraron {len(resultados)} resultado(s):\n ")
    
    for i, registro in enumerate(resultados, 1):
        print(f"\n{i}. Servicio: {registro['servicio']}")
        print(f"   Usuario: {registro['usuario']}")
        print(f"   Fecha: {registro['fecha']}")
        print(f"   Fortaleza: {registro['fortaleza']}")
        
        # Preguntar si quiere ver la contraseña
        mostrar = input("   ¿Mostrar contraseña? (s/n): ").lower()
        if mostrar == 's':
            contrasena_descifrada = modulo_cifrado.aplicar_cifrado(
                registro['contrasena'], 
                registro['metodo'], 
                cifrar=False
            )
            print(f"   Contraseña: {contrasena_descifrada}")