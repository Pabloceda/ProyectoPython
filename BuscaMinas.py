"""
PROYECTO: BUSCAMINAS EN CONSOLA
Autor: Estudiante ILERNA
Descripción: Juego de Buscaminas sin interfaz gráfica, solo por consola
"""

import random

# =====================================================================
# PARTE 1: CONFIGURACIÓN DEL JUEGO
# =====================================================================
# Estas variables definen el tamaño del tablero y la cantidad de minas
FILAS = 8          # Número de filas del tablero
COLUMNAS = 8       # Número de columnas del tablero
NUM_MINAS = 10     # Número de minas a colocar


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
    Muestra el tablero en la consola con formato legible.
    Incluye números de fila y columna para facilitar la jugada.
    
    Args:
        tablero_visible (list): El tablero que ve el jugador
    """
    print("\n   ", end="")
    # Muestra los números de columna
    for col in range(COLUMNAS):
        print(f"{col}  ", end="")
    print()
    
    # Muestra cada fila con su número
    for i, fila in enumerate(tablero_visible):
        print(f"{i}  ", end="")
        for celda in fila:
            print(f"{celda}  ", end="")
        print()
    print()


# =====================================================================
# PARTE 7: FUNCIÓN PARA DESCUBRIR CELDAS
# =====================================================================
def descubrir_celda(tablero, tablero_visible, fila, columna):
    """
    Descubre una celda en el tablero visible.
    Si la celda tiene 0 minas adyacentes, descubre también las celdas vecinas.
    
    Args:
        tablero (list): El tablero real con minas y números
        tablero_visible (list): El tablero que ve el jugador
        fila (int): Fila de la celda a descubrir
        columna (int): Columna de la celda a descubrir
    
    Returns:
        bool: True si se descubrió exitosamente, False si había una mina
    """
    # Verifica que la celda esté dentro del tablero
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        return True
    
    # Si la celda ya está descubierta, no hace nada
    if tablero_visible[fila][columna] != '#':
        return True
    
    # Si hay una mina, el jugador pierde
    if tablero[fila][columna] == -1:
        return False
    
    # Descubre la celda mostrando el número de minas adyacentes
    tablero_visible[fila][columna] = str(tablero[fila][columna])
    
    # Si no hay minas adyacentes, descubre automáticamente las celdas vecinas
    if tablero[fila][columna] == 0:
        tablero_visible[fila][columna] = ' '  # Muestra espacio vacío
        
        # Descubre las 8 celdas adyacentes recursivamente
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i != 0 or j != 0:  # No procesa la celda actual
                    descubrir_celda(tablero, tablero_visible, 
                                  fila + i, columna + j)
    
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
# PARTE 10: FUNCIÓN PRINCIPAL DEL JUEGO
# =====================================================================
def jugar():
    """
    Función principal que ejecuta el juego de Buscaminas.
    Controla el flujo del juego: inicialización, turnos y fin del juego.
    """
    print("=" * 40)
    print("     BUSCAMINAS - JUEGO EN CONSOLA")
    print("=" * 40)
    print(f"Tablero: {FILAS}x{COLUMNAS}")
    print(f"Número de minas: {NUM_MINAS}")
    print("\nInstrucciones:")
    print("- Introduce fila y columna para descubrir una celda")
    print("- '#' = celda cubierta")
    print("- Números = cantidad de minas adyacentes")
    print("- ' ' = celda vacía (sin minas cerca)")
    print("=" * 40)
    
    # INICIALIZACIÓN DEL JUEGO
    tablero = crear_tablero()                    # Crea tablero vacío
    colocar_minas(tablero, NUM_MINAS)           # Coloca las minas
    calcular_numeros(tablero)                    # Calcula números adyacentes
    tablero_visible = crear_tablero_visible()    # Crea tablero visible al jugador
    
    juego_activo = True
    
    # BUCLE PRINCIPAL DEL JUEGO
    while juego_activo:
        mostrar_tablero(tablero_visible)
        
        # Solicita entrada del jugador
        try:
            fila = int(input("Introduce fila (0-" + str(FILAS-1) + "): "))
            columna = int(input("Introduce columna (0-" + str(COLUMNAS-1) + "): "))
            
            # Valida que la entrada esté dentro del rango
            if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
                print("\n❌ Posición fuera del tablero. Intenta de nuevo.\n")
                continue
            
            # Verifica si la celda ya está descubierta
            if tablero_visible[fila][columna] != '#':
                print("\n⚠️  Esta celda ya está descubierta. Elige otra.\n")
                continue
            
            # Descubre la celda seleccionada
            exito = descubrir_celda(tablero, tablero_visible, fila, columna)
            
            # Si pisó una mina, pierde
            if not exito:
                print("\n" + "=" * 40)
                print("     💣 ¡BOOM! Has pisado una mina")
                print("=" * 40)
                mostrar_minas(tablero, tablero_visible)
                mostrar_tablero(tablero_visible)
                print("❌ ¡GAME OVER! Has perdido.\n")
                juego_activo = False
            
            # Verifica si ganó
            elif verificar_victoria(tablero_visible):
                print("\n" + "=" * 40)
                print("     🎉 ¡FELICIDADES!")
                print("=" * 40)
                mostrar_tablero(tablero_visible)
                print("✅ ¡Has ganado! Encontraste todas las celdas seguras.\n")
                juego_activo = False
        
        except ValueError:
            print("\n❌ Entrada inválida. Debes introducir números.\n")
    
    # Pregunta si quiere jugar de nuevo
    jugar_otra = input("¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra.lower() == 's':
        jugar()


# =====================================================================
# PARTE 11: PUNTO DE ENTRADA DEL PROGRAMA
# =====================================================================
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo cuando el archivo se ejecuta directamente.
    Inicia el juego llamando a la función jugar().
    """
    jugar()
