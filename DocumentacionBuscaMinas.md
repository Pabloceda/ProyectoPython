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