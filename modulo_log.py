import datetime
import os

ARCHIVO_LOG = "datos/log_auditoria.txt"

def registrar_accion(accion):
    """Registra una acción en el archivo de log"""
    
    # Crear directorio si no existe
    if not os.path.exists("datos"):
        os.makedirs("datos")
    
    # Obtener fecha y hora actual
    fecha_hora = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    
    # Formatear entrada de log
    entrada_log = f"{fecha_hora} {accion}\n"
    
    # Escribir en archivo
    with open(ARCHIVO_LOG, "a", encoding="utf-8") as archivo:
        archivo.write(entrada_log)

def mostrar_registro():
    """Muestra el registro completo de acciones"""
    
    if not os.path.exists(ARCHIVO_LOG):
        print("\n No hay registro de actividades")
        return
    
    print("\n             REGISTRO DE ACTIVIDADES\n ")
    
    with open(ARCHIVO_LOG, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
    
    # Mostrar las últimas 50 entradas (o todas si son menos)
    lineas_a_mostrar = lineas[-50:] if len(lineas) > 50 else lineas
    
    for linea in lineas_a_mostrar:
        print(linea.strip())
    
    print(f"\nTotal de entradas: {len(lineas)}")