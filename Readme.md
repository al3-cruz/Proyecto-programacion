## DESCRIPCIÓN
SAFEKEY VAULT+ es un gestor de contraseñas desarrollado en Python que permite almacenar, cifrar y gestionar contraseñas de forma segura. El sistema implementa autenticación con contraseña maestra, cifrado de datos, análisis de fortaleza, generación de contraseñas seguras y búsqueda inteligente usando recursividad.
## OBJETIVOS DEL PROYECTO
### Competencias evaluadas:
- **EC1**: Diseño descendente y modularidad
- **EC2**: Arreglos, estructuras de datos, archivos
- **EC3**: Recursividad (búsqueda, cifrado, validaciones)
### Funcionalidades implementadas:
Autenticación con contraseña maestra cifrada  
Gestión completa de contraseñas (CRUD)  
2 métodos de cifrado (César y Recursivo)  
Analizador de fortaleza de contraseñas  
Generador de contraseñas seguras  
Búsqueda inteligente con recursividad  
Registro de auditoría de acciones  
Validación recursiva de integridad  
Persistencia en archivos TXT y BIN  
## INSTALACIÓN Y EJECUCIÓN
### **Requisitos:**
- Python 3.6 o superior
- Sistema operativo: Windows, Linux o macOS
- Sin dependencias externas (solo módulos estándar)

### **Pasos para ejecutar:**
1. Descargar todos los archivos del proyecto
2. Abrir terminal/consola en la carpeta del proyecto
3. Ejecutar:
   ```bash
   python main.py

## Usar la contraseña inicial: Admin123!
## ¡IMPORTANTE! Cambiar la contraseña maestra inmediatamente

## SAFEKEY_VAULT/
    main.py                    # Punto de entrada principal
    modulo_acceso.py           # Autenticación y contraseña maestra
    modulo_cifrado.py          # Métodos de cifrado César y Recursivo
    modulo_contraseñas.py      # CRUD de contraseñas
    modulo_analizador.py       # Análisis de fortaleza
    modulo_generador.py        # Generación de contraseñas seguras
    modulo_busqueda.py         # Búsqueda recursiva e inteligente
    modulo_log.py              # Sistema de registro (log)
    modulo_validacion.py       # Validación recursiva de integridad
    datos/                     # Carpeta creada automáticamente
        maestro.dat            # Contraseña maestra CIFRADA
        contraseñas.bin        # Contraseñas en formato BIN
        contraseñas.txt        # Backup en TXT (cifrado)
        log_auditoria.txt      # Registro completo de acciones

## Texto:    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
## Cifrado:  D E F G H I J K L M N O P Q R S T U V W X Y Z A B C

## Ejemplo:  "HOLA" → "KROD"

## Paso 1: Invertir la cadena recursivamente
## Paso 2: Aplicar cifrado César al resultado

## Ejemplo:  "HOLA" → "ALOH" → "DORK"

1. Seleccionar opción 8 del menú
2. Especificar longitud (8-32 caracteres)
3. Elegir qué incluir:
   • Mayúsculas (A-Z)
   • Números (0-9)
   • Símbolos (!@#$%^&*...)
4. El sistema generará contraseña aleatoria
5. Se mostrará la fortaleza calculada

Tipos de búsqueda disponibles:
1. Por nombre exacto del servicio
2. Por usuario/correo
3. Búsqueda recursiva (coincidencia parcial)

Ejemplo recursivo: Buscar "mail" encontrará:
• "Gmail"
• "Outlook mail"
• "Yahoo Mail"

1. Seleccionar opción 10 del menú
2. Ingresar contraseña actual
3. Ingresar nueva contraseña (se verificará fortaleza)
4. Confirmar nueva contraseña
5. ✅ La nueva contraseña se guardará cifrada

1. Ejecutar: python main.py
2. Ingresar: Admin123! (contraseña por defecto)
3. Cambiar inmediatamente la contraseña maestra
4. El sistema creará automáticamente la carpeta 'datos/'

El sistema guarda información en 4 archivos:

📄 maestro.dat          → Contraseña maestra CIFRADA (TXT)
💽 contraseñas.bin      → Todas las contraseñas (BIN)
📄 contraseñas.txt      → Backup legible con contraseñas cifradas
📝 log_auditoria.txt    → Registro completo de todas las acciones

Todos los archivos se guardan en la carpeta 'datos/'

    SAFEKEY VAULT+ - MENÚ PRINCIPAL

1. Ver todas las contraseñas
2. Agregar nueva contraseña
3. Editar contraseña
4. Eliminar contraseña
5. Buscar contraseña
6. Generar contraseña segura
7. Analizar fortaleza de contraseña
8. Verificar integridad del sistema
9. Ver registro de actividades
10. Cambiar contraseña maestra
0. Salir

         AGREGAR NUEVA CONTRASEÑA

Nombre del servicio (ej: Gmail): Steam 
Usuario/Correo: Alejandro
Contraseña: NBsG7985$

 Fortaleza: Muy fuerte

          SELECCIONAR MÉTODO DE CIFRADO

1. Cifrado César (simple)
2. Cifrado Recursivo (avanzado)

Seleccione método (1-2): 2

 2 contraseña(s) guardada(s) en BIN y TXT

 Contraseña para 'Steam' agregada exitosamente

  Servicios disponibles:
1. Dis (Ale)
2. Steam (Alejandro)

Configuración:
• Longitud: 12 caracteres
• Incluir: Mayúsculas, Números, Símbolos

Resultado esperado:
✅ Contraseña de 12 caracteres generada
✅ Incluye al menos 1 mayúscula, 1 número, 1 símbolo
✅ Fortaleza: "Fuerte" o "Muy fuerte"
✅ No contiene patrones prohibidos

Datos de prueba:
1. Servicio: "Gmail", Usuario: "alice@gmail.com"
2. Servicio: "Outlook", Usuario: "bob@outlook.com"
3. Servicio: "Netflix", Usuario: "charlie@netflix.com"

Búsquedas:
• "mail" → Encuentra "Gmail" y "Outlook"
• "bob" → Encuentra registro 2
• "net" → Encuentra "Netflix"

✅ Búsqueda recursiva funciona en todos los campos

Acciones:
1. Agregar varias contraseñas
2. Menú → Opción 11 (Verificar integridad)
3. Verificar que no hay errores

Prueba de error:
1. Modificar manualmente archivo contraseñas.bin
2. Ejecutar verificación de integridad
3. Debe detectar y reportar problemas

✅ Sistema detecta corrupción de datos