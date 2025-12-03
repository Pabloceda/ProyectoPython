📚 Explicación de lo que hace cada parte del código:
🎯 Conceptos Clave:
Tablero Real (tablero):
Contiene las minas (-1) y números (cantidad de minas adyacentes)
Tablero Visible (tablero_visible):
Lo que ve el jugador (# = cubierto, números = descubierto)
🔧 Funciones Principales:
Función	Qué hace
crear_tablero()
Crea matriz 8x8 llena de ceros
colocar_minas()
Coloca 10 minas aleatoriamente (-1)
calcular_numeros()
Cuenta minas vecinas para cada celda
descubrir_celda()
Revela una celda y vecinos si es necesario
verificar_victoria()
Verifica si solo quedan minas por descubrir
jugar()
Función principal que controla el juego
💡 Lógica del Juego:
Inicialización: Crea tablero → Coloca minas → Calcula números
Bucle de juego: Muestra tablero → Lee entrada → Descubre celda → Verifica victoria/derrota
Fin: Muestra resultado y pregunta si quiere jugar otra vez
🎮 Características:
✅ Descubre automáticamente celdas vacías vecinas
✅ Valida entradas del usuario
✅ Muestra todas las minas al perder
✅ Emojis y formato visual claro
✅ Opción para jugar de nuevo

📋 Estructura del Código (11 Partes)
Parte 1: Configuración
Define el tamaño del tablero (8x8) y número de minas (10)
Parte 2: Crear Tablero
Crea una matriz vacía llena de ceros
Parte 3: Colocar Minas
Coloca minas aleatoriamente usando -1 para representarlas
Parte 4: Calcular Números
Cuenta las minas adyacentes para cada celda (los números que ves en el juego)
Parte 5: Tablero Visible
Crea el tablero que ve el jugador (con # para celdas cubiertas)
Parte 6: Mostrar Tablero
Imprime el tablero en consola con formato bonito
Parte 7: Descubrir Celda
Descubre celdas y si hay 0 minas cerca, descubre vecinos automáticamente
Parte 8: Verificar Victoria
Comprueba si solo quedan las minas por descubrir (victoria)
Parte 9: Mostrar Minas
Muestra todas las minas cuando pierdes
Parte 10: Función Principal
Controla todo el flujo del juego
Parte 11: Punto de Entrada
Inicia el programa
🎮 Cómo Funciona el Juego
Se crea un tablero de 8x8
Se colocan 10 minas aleatoriamente
El jugador introduce fila y columna
Si pisa una mina (💣) → PIERDE
Si descubre todas las celdas seguras → GANA