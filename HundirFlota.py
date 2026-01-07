
"""
PROYECTO: HUNDIR LA FLOTA EN CONSOLA
Autores: Pablo Calderón, Hugo, Miguel, Alejandro e Íñigo
Curso: 2º ASIR
Descripción: Juego de Hundir la Flota sin interfaz gráfica, solo por consola

=================================================
Juego por turnos contra la CPU en tablero 10x10.

Clases:
    - Barco: Representa un barco con longitud y estado
    - Tablero: Gestiona el tablero 10x10 y disparos
    - Jugador: Contiene tablero propio y registro de disparos
"""

import random


# ==================== CONSTANTES ====================

TAMANO_TABLERO = 10
FLOTA_BARCOS = [5, 4, 3, 3, 2]  # Portaaviones, Acorazado, Crucero, Submarino, Destructor

# Símbolos del tablero
SIMBOLO_AGUA = '~'
SIMBOLO_BARCO = 'B'
SIMBOLO_TOCADO = 'X'
SIMBOLO_FALLO = '0'

# Orientaciones
HORIZONTAL = 'H'
VERTICAL = 'V'

# Letras para coordenadas (A-J)
LETRAS_COLUMNAS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]


# ==================== CLASES ====================

class Barco:
    """
    Representa un barco en el juego.
    
    Atributos:
        longitud (int): Número de celdas que ocupa el barco
        tocados (int): Número de impactos recibidos
    """
    
    def __init__(self, longitud):
        """Inicializa un barco con la longitud especificada."""
        self.longitud = longitud
        self.tocados = 0
        
    def esta_hundido(self):
        """
        Verifica si el barco está hundido.
        
        Returns:
            bool: True si tocados == longitud
        """
        if self.tocados == self.longitud:
            return True
        else:
            return False


# ------------------------------------------------

class Tablero:
    """
    Gestiona el tablero de juego 10x10.
    
    Atributos:
        celdas (list): Matriz 10x10 con el estado de cada celda
        letras (list): Mapeo A-J para traducir coordenadas
    """
    
    def __init__(self):
        """Crea un tablero 10x10 lleno de agua."""
        self.celdas = []  # Lista vacía
        
        # Creamos 10 filas
        for i in range(TAMANO_TABLERO):
            # Cada vuelta se añade una fila de agua
            self.celdas.append([SIMBOLO_AGUA] * TAMANO_TABLERO)
        
        # Herramienta de traducción de coordenadas
        self.letras = LETRAS_COLUMNAS
        
    def colocar_barco(self, barco, fila, columna, orientacion):
        """
        Coloca un barco en el tablero.
        
        Args:
            barco (Barco): Instancia del barco a colocar
            fila (int): Fila inicial (0-9)
            columna (int): Columna inicial (0-9)
            orientacion (str): 'H' horizontal, 'V' vertical
        """
        # En caso de horizontal sumamos columna
        if orientacion == HORIZONTAL:
            for i in range(barco.longitud):
                self.celdas[fila][columna + i] = SIMBOLO_BARCO
                
        # En caso vertical sumamos filas
        elif orientacion == VERTICAL:
            for i in range(barco.longitud):
                self.celdas[fila + i][columna] = SIMBOLO_BARCO
                
    def es_valido(self, longitud, fila, columna, orientacion):
        """
        Verifica si una posición es válida para colocar un barco.
        
        Args:
            longitud (int): Tamaño del barco
            fila (int): Fila inicial (0-9)
            columna (int): Columna inicial (0-9)
            orientacion (str): 'H' horizontal, 'V' vertical
        
        Returns:
            bool: True si la posición es válida
        """
        # Comprobar si se sale del tablero
        if orientacion == HORIZONTAL:
            if columna + longitud > TAMANO_TABLERO:
                return False
        elif orientacion == VERTICAL:
            if fila + longitud > TAMANO_TABLERO:
                return False
        
        # Comprobar si choca con otro barco
        if orientacion == HORIZONTAL:
            for i in range(longitud):
                if self.celdas[fila][columna + i] != SIMBOLO_AGUA:
                    return False
        elif orientacion == VERTICAL:
            for i in range(longitud):
                if self.celdas[fila + i][columna] != SIMBOLO_AGUA:
                    return False
                
        # Si ha pasado todas las pruebas es válido
        return True
    
    def colocar_aleatorio(self, longitud):
        """
        Coloca un barco en una posición aleatoria válida.
        
        Args:
            longitud (int): Tamaño del barco a colocar
        """
        while True:
            # Se eligen coordenadas y orientación al azar
            fila = random.randint(0, TAMANO_TABLERO - 1)
            columna = random.randint(0, TAMANO_TABLERO - 1)
            orientacion = random.choice([HORIZONTAL, VERTICAL])
            
            # Si el sitio es válido creamos el barco y lo ponemos
            if self.es_valido(longitud, fila, columna, orientacion):
                barco = Barco(longitud)
                self.colocar_barco(barco, fila, columna, orientacion)
                # Terminar el bucle
                break  
        
    def hay_barcos(self):
        """
        Verifica si quedan barcos en el tablero.
        
        Returns:
            bool: True si hay al menos un barco ('B') en el tablero
        """
        for fila in self.celdas:
            if SIMBOLO_BARCO in fila:
                return True
        return False              
                
    def disparar(self, fila, columna):
        """
        Procesa un disparo en las coordenadas dadas.
        
        Args:
            fila (int): Fila del disparo (0-9)
            columna (int): Columna del disparo (0-9)
        
        Returns:
            str: "Tocado", "Agua" o "Repetido"
        """
        # Cuando toquemos un barco
        if self.celdas[fila][columna] == SIMBOLO_BARCO:
            print("¡Tocado!")
            self.celdas[fila][columna] = SIMBOLO_TOCADO
            return "Tocado"
            
        elif self.celdas[fila][columna] == SIMBOLO_AGUA:
            print("¡Agua!")
            self.celdas[fila][columna] = SIMBOLO_FALLO
            return "Agua"
        
        else:
            print("¡Ya habías disparado aquí parguela!")
            return "Repetido"


# ------------------------------------------------

class Jugador:
    """
    Representa a un jugador (usuario o CPU).
    
    Atributos:
        tablero_propio (Tablero): Donde están sus barcos
        tablero_rival (Tablero): Registro de sus disparos al enemigo
    """
    
    def __init__(self):
        """Crea un jugador con dos tableros vacíos."""
        self.tablero_propio = Tablero()
        self.tablero_rival = Tablero()


# ==================== FUNCIÓN PRINCIPAL ====================

def jugar():
    """
    Función principal del juego.
    
    Secuencia de ejecución:
        1. PREPARACIÓN: Crear jugadores (usuario y CPU)
        2. COLOCACIÓN: Situar barcos aleatoriamente en ambos tableros
        3. BATALLA: Bucle de turnos alternados hasta victoria o derrota
    """
    
    # ========== FASE 1: PREPARACIÓN ==========
    print("===INICIANDO JUEGO===")
    usuario = Jugador()
    cpu = Jugador()
    
    # ========== FASE 2: COLOCACIÓN DE FLOTA ==========
    print("===COLOCANDO BARCOS===")
    for longitud in FLOTA_BARCOS:
        usuario.tablero_propio.colocar_aleatorio(longitud)
        cpu.tablero_propio.colocar_aleatorio(longitud)
        
    # ========== FASE 3: BATALLA ==========
    turno_usuario = True
    
    while True:
        if turno_usuario:
            # --- Turno del usuario ---
            print("===ES TU TURNO===")
            print("TUS DISPAROS:")
            for fila in usuario.tablero_rival.celdas:
                print(fila)
            
            # Pedimos coordenadas
            coord = input("INTRODUCE TUS COORDENADAS:").upper()
            
            try:
                fila = usuario.tablero_propio.letras.index(coord[0])
                columna = int(coord[1:]) - 1
                resultado = cpu.tablero_propio.disparar(fila, columna)
                
                if resultado == "Tocado":
                    usuario.tablero_rival.celdas[fila][columna] = SIMBOLO_TOCADO
                    print("🔥🔥🔥LE HAS DADO🔥🔥🔥")
                
                elif resultado == "Agua":
                    usuario.tablero_rival.celdas[fila][columna] = SIMBOLO_FALLO
                    print("🌊🌊🌊AGUA🌊🌊🌊")
                
                elif resultado == "Repetido":
                    print("Ya habías disparado ahí")
                    
                # Comprobar victoria
                if cpu.tablero_propio.hay_barcos() == False:
                    print("🏆🏆🏆¡VICTORIA, HAS HUNDIDO TODOS LOS BARCOS!🏆🏆🏆")
                    break
                    
            except:
                print("¡Coordenada no válida! (D1,A3...)")
                continue
            
        else:
            # --- Turno de la CPU ---
            print("===TURNO DEL RIVAL===")
            
            fila_cpu = random.randint(0, TAMANO_TABLERO - 1)
            col_cpu = random.randint(0, TAMANO_TABLERO - 1)
            print(f"LA CPU DISPARA A: {fila_cpu},{col_cpu}")
            resultado = usuario.tablero_propio.disparar(fila_cpu, col_cpu)
            
            if resultado == "Tocado":
                print("🔥🔥🔥TE HAN DADO🔥🔥🔥")
            else:
                print("🌊🌊🌊LA IA HA FALLADO🌊🌊🌊")
                
            # Comprobar derrota
            if usuario.tablero_propio.hay_barcos() == False:
                print("☠️☠️☠️DERROTA, LA IA HA HUNDIDO TODOS TUS BARCOS☠️☠️☠️")
                break
        
        # Cambiamos de turno
        turno_usuario = not turno_usuario


# ==================== PUNTO DE ENTRADA ====================

if __name__ == "__main__":
    print("***Hundir la Flota***")
    jugar()
