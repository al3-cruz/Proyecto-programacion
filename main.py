# Importar todos los módulos necesarios
import modulo_acceso
import modulo_contraseñas
import modulo_analizador
import modulo_generador
import modulo_busqueda
import modulo_log
import modulo_validacion

# Variables globales del sistema
contrasena_maestra_actual = None
usuario_autenticado = False

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n        SAFEKEY VAULT+ - MENÚ PRINCIPAL\n")
    print("1. Ver todas las contraseñas")
    print("2. Agregar nueva contraseña")
    print("3. Editar contraseña")
    print("4. Eliminar contraseña")
    print("5. Buscar contraseña")
    print("6. Generar contraseña segura")
    print("7. Analizar fortaleza de contraseña")
    print("8. Verificar integridad del sistema")
    print("9. Ver registro de actividades")
    print("10. Cambiar contraseña maestra")
    print("0. Salir\n")
    return input("Seleccione una opción: ")

def ejecutar_sistema():
    """Función principal que ejecuta todo el sistema"""
    # Registrar inicio del sistema
    modulo_log.registrar_accion("Sistema iniciado")
    # Autenticar usuario
    if not modulo_acceso.autenticar_usuario():
        modulo_log.registrar_accion("Intento fallido de acceso - Sistema bloqueado")
        print("\n Sistema bloqueado. Contacte al administrador.")
        return
    
    modulo_log.registrar_accion("Usuario autenticado correctamente")
    
    # Cargar contraseñas desde archivo
    contrasenas = modulo_contraseñas.cargar_contrasenas()
    
    # Bucle principal del sistema
    while True:
        opcion = mostrar_menu_principal()
        
        if opcion == "1":
            # Ver todas las contraseñas
            modulo_contraseñas.mostrar_contrasenas(contrasenas)
            
        elif opcion == "2":
            # Agregar nueva contraseña
            contrasenas = modulo_contraseñas.agregar_contrasena(contrasenas)
            
        elif opcion == "3":
            # Editar contraseña
            contrasenas = modulo_contraseñas.editar_contrasena(contrasenas)
            
        elif opcion == "4":
            # Eliminar contraseña
            contrasenas = modulo_contraseñas.eliminar_contrasena(contrasenas)
            
        elif opcion == "5":
            # Buscar contraseña
            modulo_busqueda.buscar_contrasenas(contrasenas)
            
        elif opcion == "6":
            # Generar contraseña segura
            contrasena_generada = modulo_generador.generar_contrasena_segura()
            print(f"\nContraseña generada: {contrasena_generada}")
            
        elif opcion == "7":
            # Analizar fortaleza
            contrasena = input("\nIngrese contraseña a analizar: ")
            fortaleza = modulo_analizador.analizar_fortaleza(contrasena)
            print(f"\nFortaleza: {fortaleza}")
            
        elif opcion == "8":
            # Verificar integridad
            modulo_validacion.verificar_integridad(contrasenas)
            
        elif opcion == "9":
            # Ver registro
            modulo_log.mostrar_registro()
            
        elif opcion == "10":
            exito = modulo_acceso.cambiar_contrasena_maestra()
            if exito:
                print("\n Recuerda usar la nueva contraseña en el proximo inicio.\n")
            
        elif opcion == "0":
            # Salir del sistema
            modulo_contraseñas.guardar_contrasenas(contrasenas)
            modulo_log.registrar_accion("Sistema finalizado correctamente")
            print("\n Adios")
            break
            
        else:
            print("\n Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()