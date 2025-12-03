import modulo_log

def verificar_integridad_recursivo(contrasenas, indice=0, problemas=None, corregidos=0):
    """Función recursiva para verificar integridad del sistema"""
    
    if problemas is None:
        problemas = []
    
    # Caso base: hemos revisado todas las contraseñas
    if indice >= len(contrasenas):
        return problemas, corregidos
    
    registro = contrasenas[indice]
    tiene_problema = False
    
    # Verificar 1: Registro vacío
    if not registro:
        problemas.append(f"Registro {indice+1}: Vacío")
        tiene_problema = True
    
    # Verificar 2: Campos obligatorios faltantes
    campos_obligatorios = ['servicio', 'usuario', 'contrasena', 'metodo', 'fecha']
    for campo in campos_obligatorios:
        if campo not in registro:
            problemas.append(f"Registro {indice+1}: Falta campo '{campo}'")
            tiene_problema = True
    
    # Verificar 3: Contraseña no cifrada (verificación básica)
    if 'contrasena' in registro:
        # Verificar si parece texto plano (solo verificación simple)
        contrasena = registro['contrasena']
        if len(contrasena) < 5:  # Contraseñas muy cortas podrían ser sospechosas
            problemas.append(f"Registro {indice+1}: Contraseña muy corta, posiblemente no cifrada")
            tiene_problema = True
    
    # Verificar 4: Método de cifrado no reconocido
    if 'metodo' in registro and registro['metodo'] not in [1, 2]:
        problemas.append(f"Registro {indice+1}: Método de cifrado inválido ({registro['metodo']})")
        tiene_problema = True
        
        # Intentar corregir asignando método por defecto
        registro['metodo'] = 1
        corregidos = corregidos + 1
    
    # Si hay problemas, intentar corregir algunos
    if tiene_problema:
        # Intentar corregir fecha faltante
        if 'fecha' not in registro:
            from datetime import datetime
            registro['fecha'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            corregidos = corregidos + 1
    
    # Llamada recursiva para siguiente registro
    return verificar_integridad_recursivo(contrasenas, indice + 1, problemas, corregidos)

def verificar_integridad(contrasenas):
    """Función principal de verificación de integridad"""
    print("\n         VERIFICACIÓN DE INTEGRIDAD\n ")
    
    if not contrasenas:
        print("No hay contraseñas para verificar")
        return
    
    # Ejecutar verificación recursiva
    problemas, corregidos = verificar_integridad_recursivo(contrasenas)
    
    # Mostrar resultados
    if not problemas:
        print("Todos los registros están correctos")
    else:
        print(f"\n Se encontraron {len(problemas)} problema(s):")
        for problema in problemas:
            print(f"   • {problema}")
        
        print(f"\n Se corrigieron automáticamente {corregidos} problema(s)")
    
    # Verificar archivos del sistema
    print("\n Verificación de archivos del sistema:")
    
    archivos_necesarios = [
        "datos/maestro.dat",
        "datos/contraseñas.bin",
        "datos/log_auditoria.txt"
    ]
    
    for archivo in archivos_necesarios:
        import os
        if os.path.exists(archivo):
            print(f"    {archivo} - PRESENTE")
        else:
            print(f"    {archivo} - AUSENTE")
    
    # Registrar la verificación
    modulo_log.registrar_accion("Verificación de integridad ejecutada")
    print("\n Verificación completada")