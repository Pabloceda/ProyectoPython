# 📚 DOCUMENTACIÓN BUSCAMINAS

## 🎯 Conceptos Clave

### Tablero Real (`tablero`)
Contiene las minas (`-1`) y números (cantidad de minas adyacentes)

### Tablero Visible (`tablero_visible`)
Lo que ve el jugador (`#` = cubierto, números = descubierto)

---

## 🔧 Funciones Principales

| Función | Qué hace |
|---------|----------
| `crear_tablero()` | Crea matriz dinámica llena de ceros |
| `colocar_minas()` | Coloca minas aleatoriamente (-1) |
| `calcular_numeros()` | Cuenta minas vecinas para cada celda |
| `descubrir_celda()` | Revela una celda y vecinos si es necesario |
| `verificar_victoria()` | Verifica si solo quedan minas por descubrir |
| `menu_dificultad()` | **NUEVO** - Muestra menú de niveles |
| `jugar()` | Función principal que controla el juego |

---

## 🎮 Niveles de Dificultad

El juego ahora incluye **3 niveles de dificultad**:

| Nivel | Tablero | Minas | Dificultad |
|-------|---------|-------|------------|
| 🟢 **Fácil** | 6x6 | 5 | Ideal para principiantes |
| 🟡 **Medio** | 8x8 | 10 | Desafío equilibrado |
| 🔴 **Difícil** | 12x12 | 20 | Para expertos |

---

## 💡 Lógica del Juego

1. **Selección de dificultad**: El jugador elige nivel (Fácil/Medio/Difícil)
2. **Inicialización**: Crea tablero → Coloca minas → Calcula números
3. **Bucle de juego**: Muestra tablero → Lee entrada → Descubre celda → Verifica victoria/derrota
4. **Fin**: Muestra resultado y permite elegir otra dificultad

---

## ✨ Características

✅ **Tres niveles de dificultad** con configuraciones dinámicas  
✅ Descubre automáticamente celdas vacías vecinas  
✅ Valida entradas del usuario  
✅ Muestra todas las minas al perder  
✅ Emojis y formato visual claro  
✅ Opción para jugar de nuevo con diferente dificultad  

---

## 📋 Estructura del Código (12 Partes)

### Parte 1: Configuración
Define las configuraciones de dificultad en un diccionario

### Parte 2: Crear Tablero
Crea una matriz vacía llena de ceros (tamaño dinámico)

### Parte 3: Colocar Minas
Coloca minas aleatoriamente usando `-1` para representarlas

### Parte 4: Calcular Números
Cuenta las minas adyacentes para cada celda

### Parte 5: Tablero Visible
Crea el tablero que ve el jugador (con `#` para celdas cubiertas)

### Parte 6: Mostrar Tablero
Imprime el tablero en consola con formato bonito

### Parte 7: Descubrir Celda
Descubre celdas y si hay 0 minas cerca, descubre vecinos automáticamente

### Parte 8: Verificar Victoria
Comprueba si solo quedan las minas por descubrir (victoria)

### Parte 9: Mostrar Minas
Muestra todas las minas cuando pierdes

### Parte 10: Menú de Dificultad ⭐ NUEVO
Muestra opciones y permite seleccionar nivel de dificultad

### Parte 11: Función Principal
Controla todo el flujo del juego con parámetros dinámicos

### Parte 12: Punto de Entrada
Inicia el programa mostrando el menú de dificultad

---

## 🎮 Cómo Funciona el Juego

1. **Menú inicial**: Elige entre Fácil (6x6, 5 minas), Medio (8x8, 10 minas) o Difícil (12x12, 20 minas)
2. **Configuración**: Se crea un tablero del tamaño correspondiente
3. **Colocación**: Se colocan las minas aleatoriamente
4. **Jugabilidad**: El jugador introduce fila y columna
5. **Resultados**:
   - Si pisa una mina (💣) → **PIERDE**
   - Si descubre todas las celdas seguras → **GANA**
6. **Rejugabilidad**: Puede elegir otra dificultad y volver a jugar