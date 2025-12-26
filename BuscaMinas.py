"""
PROYECTO: BUSCAMINAS EN CONSOLA
Autor: Pablo Calderón, Hugo, Miguel, Alejandro e Íñigo
Curso: 2º ASIR
Descripción: Juego de Buscaminas sin interfaz gráfica, solo por consola
"""
# =====================================================================
# PARTE 0: IMPORTACIÓN DE LIBRERÍAS
# =====================================================================
import random
import time
import json
import os

# =====================================================================
# PARTE 1: CONFIGURACIÓN DEL JUEGO Y COLORES
# =====================================================================
# Estas variables se configuran según el nivel de dificultad elegido
FILAS = 8          # Número de filas del tablero (se ajusta según dificultad)
COLUMNAS = 8       # Número de columnas del tablero (se ajusta según dificultad)
NUM_MINAS = 10     # Número de minas a colocar (se ajusta según dificultad)

# Configuraciones de dificultad
DIFICULTADES = {
    '1': {'nombre': 'Fácil', 'filas': 6, 'columnas': 6, 'minas': 5},
    '2': {'nombre': 'Medio', 'filas': 8, 'columnas': 8, 'minas': 10},
    '3': {'nombre': 'Difícil', 'filas': 12, 'columnas': 12, 'minas': 20}
}

# Archivo para guardar puntuaciones
ARCHIVO_PUNTUACIONES = 'puntuaciones.json'

# Colores ANSI para mejorar la visualización
class Colores:
    """Clase con códigos de colores ANSI para la consola"""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    # Colores de texto
    ROJO = '\033[91m'
    VERDE = '\033[92m'
    AMARILLO = '\033[93m'
    AZUL = '\033[94m'
    MAGENTA = '\033[95m'
    CIAN = '\033[96m'
    BLANCO = '\033[97m'
    GRIS = '\033[90m'
    # Fondos
    BG_ROJO = '\033[101m'
    BG_VERDE = '\033[102m'
    BG_AMARILLO = '\033[103m'

# Mapeo de números a colores
COLORES_NUMEROS = {
    '1': Colores.AZUL,
    '2': Colores.VERDE,
    '3': Colores.ROJO,
    '4': Colores.MAGENTA,
    '5': Colores.AMARILLO,
    '6': Colores.CIAN,
    '7': Colores.BLANCO,
    '8': Colores.GRIS
}


# =====================================================================
# PARTE 2: FUNCIÓN PARA CREAR EL TABLERO
# =====================================================================
def crear_tablero():
    """
    Crea un tablero vacío representado como una lista de listas.
    Cada celda contiene 0 (sin mina) inicialmente.
    
    Returns:
        list: Tablero de juego (matriz de FILAS x COLUMNAS)
    """
    # Crea una matriz (lista de listas) llena de ceros
    tablero = []
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append(0)  # 0 significa que no hay mina
        tablero.append(fila)
    return tablero


# =====================================================================
# PARTE 3: FUNCIÓN PARA COLOCAR MINAS
# =====================================================================
def colocar_minas(tablero, num_minas):
    """
    Coloca minas aleatoriamente en el tablero.
    Una mina se representa con el valor -1.
    
    Args:
        tablero (list): El tablero de juego
        num_minas (int): Número de minas a colocar
    """
    minas_colocadas = 0
    
    # Coloca minas hasta alcanzar el número deseado
    while minas_colocadas < num_minas:
        # Genera una posición aleatoria
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        
        # Si la celda está vacía (no tiene mina), coloca una mina
        if tablero[fila][columna] != -1:
            tablero[fila][columna] = -1  # -1 representa una mina
            minas_colocadas += 1


# =====================================================================
# PARTE 4: FUNCIÓN PARA CALCULAR LOS NÚMEROS
# =====================================================================
def calcular_numeros(tablero):
    """
    Calcula el número de minas adyacentes para cada celda sin mina.
    Este número se muestra al jugador cuando descubre una casilla.
    
    Args:
        tablero (list): El tablero de juego
    """
    # Recorre todas las celdas del tablero
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            # Si la celda NO tiene mina, calcula las minas adyacentes
            if tablero[fila][columna] != -1:
                minas_adyacentes = 0
                
                # Revisa las 8 celdas adyacentes (arriba, abajo, izq, der y diagonales)
                for i in range(-1, 2):      # -1, 0, 1
                    for j in range(-1, 2):  # -1, 0, 1
                        nueva_fila = fila + i
                        nueva_columna = columna + j
                        
                        # Verifica que la celda esté dentro del tablero
                        if (0 <= nueva_fila < FILAS and 
                            0 <= nueva_columna < COLUMNAS):
                            # Si la celda adyacente tiene mina, incrementa el contador
                            if tablero[nueva_fila][nueva_columna] == -1:
                                minas_adyacentes += 1
                
                # Guarda el número de minas adyacentes en la celda
                tablero[fila][columna] = minas_adyacentes


# =====================================================================
# PARTE 5: FUNCIÓN PARA CREAR EL TABLERO VISIBLE
# =====================================================================
def crear_tablero_visible():
    """
    Crea el tablero que ve el jugador.
    Al inicio, todas las celdas están cubiertas (representadas con '#').
    
    Returns:
        list: Tablero visible (matriz de FILAS x COLUMNAS)
    """
    tablero_visible = []
    for i in range(FILAS):
        fila = []
        for j in range(COLUMNAS):
            fila.append('#')  # '#' representa una celda cubierta
        tablero_visible.append(fila)
    return tablero_visible


# =====================================================================
# PARTE 6: FUNCIÓN PARA MOSTRAR EL TABLERO
# =====================================================================
def mostrar_tablero(tablero_visible):
    """
    Muestra el tablero en la consola con formato legible y colores.
    Incluye números de fila y columna para facilitar la jugada.
    
    Args:
        tablero_visible (list): El tablero que ve el jugador
    """
    # Muestra el encabezado con números de columna
    # Usamos 3 espacios para alinear con los números de fila (2 dígitos + 1 espacio)
    print("\n" + Colores.CIAN + "   ", end="")
    for col in range(COLUMNAS):
        print(f"{Colores.BOLD}{col:2d}{Colores.RESET}{Colores.CIAN} ", end="")
    print(Colores.RESET)
    
    # Muestra cada fila con su número y colores
    for i, fila in enumerate(tablero_visible):
        # Número de fila con ancho fijo
        print(f"{Colores.CIAN}{Colores.BOLD}{i:2d}{Colores.RESET} ", end="")
        for celda in fila:
            if celda == '#':
                # Celda cubierta en gris
                print(f" {Colores.GRIS}{celda}{Colores.RESET} ", end="")
            elif celda == '*':
                # Mina en rojo con fondo
                print(f" {Colores.BG_ROJO}{Colores.BLANCO}{celda}{Colores.RESET} ", end="")
            elif celda == ' ':
                # Celda vacía
                print(f" {celda} ", end="")
            elif celda in COLORES_NUMEROS:
                # Número con color específico
                color = COLORES_NUMEROS[celda]
                print(f" {color}{Colores.BOLD}{celda}{Colores.RESET} ", end="")
            else:
                print(f" {celda} ", end="")
        print()
    print()


# =====================================================================
# PARTE 7: FUNCIÓN PARA DESCUBRIR CELDAS
# =====================================================================
def descubrir_celda(tablero, tablero_visible, fila, columna):
    """
    Descubre una celda en el tablero visible (VERSION ITERATIVA).
    Si la celda tiene 0 minas adyacentes, descubre también las celdas vecinas.
    Usa una pila en lugar de recursión para evitar límites de profundidad.
    
    Args:
        tablero (list): El tablero real con minas y números
        tablero_visible (list): El tablero que ve el jugador
        fila (int): Fila de la celda a descubrir
        columna (int): Columna de la celda a descubrir
    
    Returns:
        bool: True si se descubrió exitosamente, False si había una mina
    """
    # Verifica que la celda inicial esté dentro del tablero
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        return True
    
    # Si la celda ya está descubierta, no hace nada
    if tablero_visible[fila][columna] != '#':
        return True
    
    # Si hay una mina, el jugador pierde
    if tablero[fila][columna] == -1:
        return False
    
    # Usa una pila para procesar celdas iterativamente
    pila = [(fila, columna)]
    
    while pila:
        f, c = pila.pop()
        
        # Verifica límites y si ya está descubierta
        if f < 0 or f >= FILAS or c < 0 or c >= COLUMNAS:
            continue
        if tablero_visible[f][c] != '#':
            continue
        
        # Descubre la celda mostrando el número de minas adyacentes
        valor = tablero[f][c]
        
        if valor == 0:
            tablero_visible[f][c] = ' '  # Muestra espacio vacío
            # Añade las 8 celdas adyacentes a la pila
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i != 0 or j != 0:  # No procesa la celda actual
                        pila.append((f + i, c + j))
        else:
            tablero_visible[f][c] = str(valor)
    
    return True


# =====================================================================
# PARTE 8: FUNCIÓN PARA VERIFICAR VICTORIA
# =====================================================================
def verificar_victoria(tablero_visible):
    """
    Verifica si el jugador ha ganado.
    Gana cuando todas las celdas sin mina están descubiertas.
    
    Args:
        tablero_visible (list): El tablero que ve el jugador
    
    Returns:
        bool: True si ganó, False si aún hay celdas por descubrir
    """
    celdas_cubiertas = 0
    
    # Cuenta cuántas celdas siguen cubiertas
    for fila in tablero_visible:
        for celda in fila:
            if celda == '#':
                celdas_cubiertas += 1
    
    # Si solo quedan cubiertas las celdas con minas, el jugador gana
    return celdas_cubiertas == NUM_MINAS


# =====================================================================
# PARTE 9: FUNCIÓN PARA MOSTRAR TODAS LAS MINAS
# =====================================================================
def mostrar_minas(tablero, tablero_visible):
    """
    Muestra todas las minas en el tablero visible.
    Se usa cuando el jugador pierde para mostrarle dónde estaban las minas.
    
    Args:
        tablero (list): El tablero real con minas
        tablero_visible (list): El tablero que ve el jugador
    """
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if tablero[fila][columna] == -1:
                tablero_visible[fila][columna] = '*'  # '*' representa una mina


# =====================================================================
# PARTE 9B: FUNCIONES AUXILIARES
# =====================================================================
def proteger_primera_jugada(tablero, fila, columna):
    """
    Asegura que la primera jugada nunca sea una mina.
    Si hay una mina en la posición seleccionada, la mueve a otra posición.
    
    Args:
        tablero (list): El tablero real con minas
        fila (int): Fila de la primera jugada
        columna (int): Columna de la primera jugada
    """
    if tablero[fila][columna] == -1:
        # La primera jugada es una mina, la movemos a otra posición
        tablero[fila][columna] = 0
        
        # Busca una nueva posición para la mina
        while True:
            nueva_fila = random.randint(0, FILAS - 1)
            nueva_columna = random.randint(0, COLUMNAS - 1)
            
            # Asegura que no sea la posición inicial ni ya tenga una mina
            if (nueva_fila != fila or nueva_columna != columna) and tablero[nueva_fila][nueva_columna] != -1:
                tablero[nueva_fila][nueva_columna] = -1
                break
        
        # Recalcula los números después de mover la mina
        calcular_numeros(tablero)


def cargar_puntuaciones():
    """
    Carga las puntuaciones (mejores tiempos) desde el archivo JSON.
    
    Returns:
        dict: Diccionario con las mejores puntuaciones por dificultad
    """
    if os.path.exists(ARCHIVO_PUNTUACIONES):
        try:
            with open(ARCHIVO_PUNTUACIONES, 'r') as f:
                return json.load(f)
        except:
            return {}
    return {}


def guardar_puntuacion(nombre_dificultad, tiempo):
    """
    Guarda una nueva puntuación si es mejor que la anterior.
    
    Args:
        nombre_dificultad (str): Nombre del nivel de dificultad
        tiempo (float): Tiempo en segundos que tardó el jugador
    
    Returns:
        bool: True si es un nuevo récord, False si no
    """
    puntuaciones = cargar_puntuaciones()
    
    es_record = False
    # Redondea el tiempo a 2 decimales para mejor legibilidad
    tiempo_redondeado = round(tiempo, 2)
    if nombre_dificultad not in puntuaciones or tiempo_redondeado < puntuaciones[nombre_dificultad]:
        puntuaciones[nombre_dificultad] = tiempo_redondeado
        es_record = True
        
        try:
            with open(ARCHIVO_PUNTUACIONES, 'w', encoding='utf-8') as f:
                json.dump(puntuaciones, f, indent=4, ensure_ascii=False)
        except:
            pass
    
    return es_record


def mostrar_ayuda():
    """
    Muestra la ayuda del juego con todos los comandos disponibles.
    """
    print("\n" + "=" * 50)
    print(f"{Colores.AMARILLO}{Colores.BOLD}     📚 AYUDA DEL JUEGO{Colores.RESET}")
    print("=" * 50)
    print(f"\n{Colores.CIAN}Comandos disponibles:{Colores.RESET}")
    print(f"  • {Colores.VERDE}Números{Colores.RESET}: Introduce fila y columna para descubrir")
    print(f"  • {Colores.VERDE}'ayuda'{Colores.RESET}: Muestra esta ayuda")
    print(f"  • {Colores.VERDE}'pista'{Colores.RESET}: Revela una celda segura aleatoria")
    print(f"  • {Colores.VERDE}'rendirse'{Colores.RESET}: Termina el juego actual")
    print(f"  • {Colores.VERDE}'salir'{Colores.RESET}: Sale del juego completamente")
    print(f"\n{Colores.CIAN}Símbolos en el tablero:{Colores.RESET}")
    print(f"  • {Colores.GRIS}#{Colores.RESET} = Celda cubierta")
    print(f"  • {Colores.AZUL}1-8{Colores.RESET} = Número de minas adyacentes")
    print(f"  • {Colores.BLANCO} {Colores.RESET} = Celda vacía (sin minas cerca)")
    print(f"  • {Colores.BG_ROJO}*{Colores.RESET} = Mina (solo visible al perder)")
    print("=" * 50 + "\n")


def obtener_celda_segura(tablero, tablero_visible):
    """
    Encuentra una celda segura (sin mina) que aún no ha sido descubierta.
    
    Args:
        tablero (list): El tablero real con minas
        tablero_visible (list): El tablero que ve el jugador
    
    Returns:
        tuple: (fila, columna) de una celda segura, o None si no hay
    """
    celdas_seguras = []
    
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            # Si la celda está cubierta y no tiene mina
            if tablero_visible[fila][columna] == '#' and tablero[fila][columna] != -1:
                celdas_seguras.append((fila, columna))
    
    if celdas_seguras:
        return random.choice(celdas_seguras)
    return None


# =====================================================================
# PARTE 10: FUNCIÓN PARA MOSTRAR MENÚ DE DIFICULTAD
# =====================================================================
def menu_dificultad():
    """
    Muestra el menú de selección de dificultad y retorna la configuración elegida.
    
    Returns:
        dict: Configuración del nivel elegido (filas, columnas, minas)
    """
    print("\n" + "=" * 50)
    print("     🎮 BUSCAMINAS - SELECCIÓN DE DIFICULTAD")
    print("=" * 50)
    print("\n📊 Elige tu nivel de dificultad:\n")
    print("  1️⃣  FÁCIL    -  Tablero 6x6   -  5 minas")
    print("  2️⃣  MEDIO    -  Tablero 8x8   - 10 minas")
    print("  3️⃣  DIFÍCIL  -  Tablero 12x12 - 20 minas")
    print("\n" + "-" * 50)
    print(f"{Colores.AMARILLO}📌 COMANDOS DURANTE EL JUEGO:{Colores.RESET}")
    print(f"  • {Colores.VERDE}'ayuda'{Colores.RESET}    → Ver todos los comandos y símbolos")
    print(f"  • {Colores.VERDE}'pista'{Colores.RESET}    → Revelar una celda segura")
    print(f"  • {Colores.VERDE}'rendirse'{Colores.RESET} → Abandonar la partida actual")
    print(f"  • {Colores.VERDE}'salir'{Colores.RESET}    → Cerrar el juego completamente")
    print("-" * 50)
    print(f"{Colores.CIAN}💡 Introduce fila y columna para descubrir celdas{Colores.RESET}")
    print("=" * 50)
    
    while True:
        opcion = input("\n👉 Selecciona (1/2/3): ").strip()
        
        if opcion in DIFICULTADES:
            config = DIFICULTADES[opcion]
            print(f"\n✅ Has elegido: {config['nombre']}")
            print(f"   Tablero: {config['filas']}x{config['columnas']}")
            print(f"   Minas: {config['minas']}\n")
            return config
        else:
            print("❌ Opción inválida. Por favor, elige 1, 2 o 3.")


# =====================================================================
# PARTE 11: FUNCIÓN PRINCIPAL DEL JUEGO
# =====================================================================
def jugar(filas, columnas, num_minas, nombre_dificultad):
    """
    Función principal que ejecuta el juego de Buscaminas (MEJORADA).
    Controla el flujo del juego: inicialización, turnos y fin del juego.
    Incluye: cronómetro, protección primera jugada, comandos especiales y puntuaciones.
    
    Args:
        filas (int): Número de filas del tablero
        columnas (int): Número de columnas del tablero
        num_minas (int): Número de minas a colocar
        nombre_dificultad (str): Nombre del nivel de dificultad
    """
    # Actualiza las variables globales con la configuración elegida
    global FILAS, COLUMNAS, NUM_MINAS
    FILAS = filas
    COLUMNAS = columnas
    NUM_MINAS = num_minas
    
    # Muestra las mejores puntuaciones si existen
    puntuaciones = cargar_puntuaciones()
    
    print("\n" + "=" * 50)
    print(f"{Colores.AMARILLO}{Colores.BOLD}     🎯 BUSCAMINAS - JUEGO EN CONSOLA{Colores.RESET}")
    print("=" * 50)
    print(f"{Colores.CIAN}Dificultad:{Colores.RESET} {Colores.BOLD}{nombre_dificultad}{Colores.RESET}")
    print(f"{Colores.CIAN}Tablero:{Colores.RESET} {FILAS}x{COLUMNAS}")
    print(f"{Colores.CIAN}Número de minas:{Colores.RESET} {Colores.ROJO}{NUM_MINAS}{Colores.RESET}")
    
    if nombre_dificultad in puntuaciones:
        mejor_tiempo = puntuaciones[nombre_dificultad]
        minutos = int(mejor_tiempo // 60)
        segundos = int(mejor_tiempo % 60)
        print(f"{Colores.VERDE}🏆 Mejor tiempo:{Colores.RESET} {minutos:02d}:{segundos:02d}")
    
    print(f"\n{Colores.AMARILLO}💡 Escribe 'ayuda' para ver todos los comandos{Colores.RESET}")
    print("=" * 50)
    
    # INICIALIZACIÓN DEL JUEGO
    tablero = crear_tablero()                    # Crea tablero vacío
    colocar_minas(tablero, NUM_MINAS)           # Coloca las minas
    calcular_numeros(tablero)                    # Calcula números adyacentes
    tablero_visible = crear_tablero_visible()    # Crea tablero visible al jugador
    
    juego_activo = True
    primera_jugada = True
    tiempo_inicio = time.time()  # Inicia el cronómetro
    
    # BUCLE PRINCIPAL DEL JUEGO
    while juego_activo:
        mostrar_tablero(tablero_visible)
        
        # Muestra el tiempo transcurrido
        tiempo_actual = time.time() - tiempo_inicio
        minutos = int(tiempo_actual // 60)
        segundos = int(tiempo_actual % 60)
        print(f"{Colores.CIAN}⏱️  Tiempo: {minutos:02d}:{segundos:02d}{Colores.RESET}\n")
        
        # Solicita entrada del jugador
        try:
            entrada = input(f"{Colores.VERDE}Introduce fila (0-{FILAS-1}) o comando: {Colores.RESET}").strip().lower()
            
            # Procesa comandos especiales
            if entrada == 'ayuda':
                mostrar_ayuda()
                continue
            elif entrada == 'pista':
                celda_segura = obtener_celda_segura(tablero, tablero_visible)
                if celda_segura:
                    fila, columna = celda_segura
                    print(f"\n{Colores.VERDE}💡 Pista: La celda ({fila}, {columna}) es segura{Colores.RESET}\n")
                    # Descubre automáticamente la celda
                    if primera_jugada:
                        primera_jugada = False
                    descubrir_celda(tablero, tablero_visible, fila, columna)
                    
                    # Verifica si ganó después de usar la pista
                    if verificar_victoria(tablero_visible):
                        tiempo_final = time.time() - tiempo_inicio
                        print("\n" + "=" * 40)
                        print(f"{Colores.VERDE}{Colores.BOLD}     🎉 ¡FELICIDADES!{Colores.RESET}")
                        print("=" * 40)
                        mostrar_tablero(tablero_visible)
                        
                        minutos = int(tiempo_final // 60)
                        segundos = int(tiempo_final % 60)
                        print(f"{Colores.VERDE}✅ ¡Has ganado! Encontraste todas las celdas seguras.{Colores.RESET}")
                        print(f"{Colores.CIAN}⏱️  Tiempo final: {minutos:02d}:{segundos:02d}{Colores.RESET}")
                        
                        # Guarda la puntuación
                        es_record = guardar_puntuacion(nombre_dificultad, tiempo_final)
                        if es_record:
                            print(f"{Colores.AMARILLO}{Colores.BOLD}🏆 ¡NUEVO RÉCORD! ¡Felicidades!{Colores.RESET}\n")
                        else:
                            print()
                        
                        juego_activo = False
                        break
                else:
                    print(f"\n{Colores.AMARILLO}⚠️  No hay más celdas seguras disponibles{Colores.RESET}\n")
                continue
            elif entrada == 'rendirse':
                print(f"\n{Colores.AMARILLO}😔 Te has rendido. Aquí está el tablero completo:{Colores.RESET}")
                mostrar_minas(tablero, tablero_visible)
                mostrar_tablero(tablero_visible)
                juego_activo = False
                break
            elif entrada == 'salir':
                print(f"\n{Colores.CIAN}👋 ¡Hasta luego!{Colores.RESET}\n")
                return
            
            # Procesa entrada numérica (fila)
            fila = int(entrada)
            columna = int(input(f"{Colores.VERDE}Introduce columna (0-{COLUMNAS-1}): {Colores.RESET}").strip())
            
            # Valida que la entrada esté dentro del rango
            if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
                print(f"\n{Colores.ROJO}❌ Posición fuera del tablero. Intenta de nuevo.{Colores.RESET}\n")
                continue
            
            # Verifica si la celda ya está descubierta
            if tablero_visible[fila][columna] != '#':
                print(f"\n{Colores.AMARILLO}⚠️  Esta celda ya está descubierta. Elige otra.{Colores.RESET}\n")
                continue
            
            # Protección de primera jugada: asegura que no sea una mina
            if primera_jugada:
                proteger_primera_jugada(tablero, fila, columna)
                primera_jugada = False
            
            # Descubre la celda seleccionada
            exito = descubrir_celda(tablero, tablero_visible, fila, columna)
            
            # Si pisó una mina, pierde
            if not exito:
                tiempo_final = time.time() - tiempo_inicio
                print("\n" + "=" * 40)
                print(f"{Colores.ROJO}{Colores.BOLD}     💣 ¡BOOM! Has pisado una mina{Colores.RESET}")
                print("=" * 40)
                mostrar_minas(tablero, tablero_visible)
                mostrar_tablero(tablero_visible)
                
                minutos = int(tiempo_final // 60)
                segundos = int(tiempo_final % 60)
                print(f"{Colores.ROJO}❌ ¡GAME OVER! Has perdido.{Colores.RESET}")
                print(f"{Colores.CIAN}⏱️  Tiempo de juego: {minutos:02d}:{segundos:02d}{Colores.RESET}\n")
                juego_activo = False
            
            # Verifica si ganó
            elif verificar_victoria(tablero_visible):
                tiempo_final = time.time() - tiempo_inicio
                print("\n" + "=" * 40)
                print(f"{Colores.VERDE}{Colores.BOLD}     🎉 ¡FELICIDADES!{Colores.RESET}")
                print("=" * 40)
                mostrar_tablero(tablero_visible)
                
                minutos = int(tiempo_final // 60)
                segundos = int(tiempo_final % 60)
                print(f"{Colores.VERDE}✅ ¡Has ganado! Encontraste todas las celdas seguras.{Colores.RESET}")
                print(f"{Colores.CIAN}⏱️  Tiempo final: {minutos:02d}:{segundos:02d}{Colores.RESET}")
                
                # Guarda la puntuación
                es_record = guardar_puntuacion(nombre_dificultad, tiempo_final)
                if es_record:
                    print(f"{Colores.AMARILLO}{Colores.BOLD}🏆 ¡NUEVO RÉCORD! ¡Felicidades!{Colores.RESET}\n")
                else:
                    print()
                
                juego_activo = False
        
        except ValueError:
            print(f"\n{Colores.ROJO}❌ Entrada inválida. Introduce números o comandos válidos.{Colores.RESET}\n")
    
    # Pregunta si quiere jugar de nuevo
    jugar_otra = input(f"\n{Colores.VERDE}¿Quieres jugar otra vez? (s/n): {Colores.RESET}").strip().lower()
    if jugar_otra == 's':
        # Permite elegir dificultad de nuevo
        config = menu_dificultad()
        jugar(config['filas'], config['columnas'], config['minas'], config['nombre'])


# =====================================================================
# PARTE 12: PUNTO DE ENTRADA DEL PROGRAMA
# =====================================================================
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo cuando el archivo se ejecuta directamente.
    Muestra el menú de dificultad y luego inicia el juego.
    """
    # Muestra el menú y obtiene la configuración elegida
    configuracion = menu_dificultad()
    
    # Inicia el juego con la configuración elegida
    jugar(configuracion['filas'], 
          configuracion['columnas'], 
          configuracion['minas'], 
          configuracion['nombre'])
