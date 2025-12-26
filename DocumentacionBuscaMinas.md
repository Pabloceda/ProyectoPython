# 📚 DOCUMENTACIÓN BUSCAMINAS

## 🎯 Conceptos Clave

### Tablero Real (`tablero`)
Contiene las minas (`-1`) y números (cantidad de minas adyacentes)

### Tablero Visible (`tablero_visible`)
Lo que ve el jugador:
- `#` = celda cubierta (gris)
- Números `1-8` = minas adyacentes (cada número con su color)
- ` ` = celda vacía (sin minas cerca)
- `*` = mina (rojo, solo visible al perder)

---

## 🔧 Funciones Principales

| Función | Qué hace |
|---------|----------|
| `crear_tablero()` | Crea matriz dinámica llena de ceros |
| `colocar_minas()` | Coloca minas aleatoriamente (-1) |
| `calcular_numeros()` | Cuenta minas vecinas para cada celda |
| `descubrir_celda()` | Revela celda y vecinos (sin recursión) |
| `verificar_victoria()` | Verifica si solo quedan minas por descubrir |
| `mostrar_minas()` | Muestra todas las minas al perder |
| `proteger_primera_jugada()` | Asegura que la primera jugada no sea mina |
| `cargar_puntuaciones()` | Carga mejores tiempos desde JSON |
| `guardar_puntuacion()` | Guarda récord si es mejor tiempo |
| `mostrar_ayuda()` | Muestra todos los comandos disponibles |
| `obtener_celda_segura()` | Encuentra celda sin mina para pistas |
| `jugar()` verifica victoria post-pista | Detecta victoria después de usar pista |
| `menu_dificultad()` | Muestra menú de niveles |
| `jugar()` | Función principal con cronómetro y comandos |

---

## 🎨 Sistema de Colores ANSI

El juego usa **colores** para mejorar la experiencia visual:

| Elemento | Color | Descripción |
|----------|-------|-------------|
| **Número 1** | 🔵 Azul | Una mina cerca |
| **Número 2** | 🟢 Verde | Dos minas cerca |
| **Número 3** | 🔴 Rojo | Tres minas cerca |
| **Número 4** | 🟣 Magenta | Cuatro minas cerca |
| **Número 5** | 🟡 Amarillo | Cinco minas cerca |
| **Número 6** | 🔷 Cian | Seis minas cerca |
| **Números 7-8** | ⚪ Blanco/Gris | Siete u ocho minas |
| **Celda cubierta #** | ⚫ Gris | No descubierta |
| **Mina \*** | 🟥 Fondo Rojo | Mina revelada |
| **Coordenadas** | 🔷 Cian | Números de fila/columna |

---

## 🎮 Niveles de Dificultad

El juego incluye **3 niveles de dificultad**:

| Nivel | Tablero | Minas | Dificultad |
|-------|---------|-------|------------|
| 🟢 **Fácil** | 6x6 | 5 | Ideal para principiantes |
| 🟡 **Medio** | 8x8 | 10 | Desafío equilibrado |
| 🔴 **Difícil** | 12x12 | 20 | Para expertos |

---

## 💡 Lógica del Juego

1. **Selección de dificultad**: El jugador elige nivel y ve el récord actual
2. **Inicialización**: Crea tablero → Coloca minas → Calcula números → Inicia cronómetro
3. **Primera jugada protegida**: Garantiza que nunca sea una mina
4. **Bucle de juego**: Muestra tablero con tiempo → Lee entrada/comando → Descubre celda → Verifica victoria/derrota
5. **Fin**: Muestra resultado, tiempo final y si es récord nuevo
6. **Rejugabilidad**: Permite elegir otra dificultad

---

## 🎯 Comandos Especiales

Durante el juego, puedes usar estos comandos:

| Comando | Función |
|---------|---------|
| `ayuda` | Muestra la ayuda completa con todos los comandos |
| `pista` | Revela automáticamente una celda segura aleatoria |
| `rendirse` | Muestra todas las minas y termina el juego |
| `salir` | Sale del juego completamente |
| _números_ | Introduce fila y columna para descubrir |

---

## ✨ Características

### Características Básicas
✅ **Tres niveles de dificultad** con configuraciones dinámicas  
✅ Descubre automáticamente celdas vacías vecinas  
✅ Valida entradas del usuario  
✅ Muestra todas las minas al perder  
✅ Emojis y formato visual claro  
✅ Opción para jugar de nuevo con diferente dificultad  

### Tecnologías claves
🎨 **Sistema de colores ANSI** - Cada número tiene su color distintivo  
🛡️ **Protección de primera jugada** - Nunca pierdes en el primer movimiento  
⏱️ **Cronómetro en tiempo real** - Muestra tiempo transcurrido en formato MM:SS  
🏆 **Sistema de puntuaciones persistentes** - Guarda mejores tiempos en JSON  
💡 **Sistema de pistas** - Revela celdas seguras si necesitas ayuda  
⌨️ **Comandos especiales** - Ayuda, pistas, rendirse, salir  
🚀 **Algoritmo iterativo** - Sin límites de recursión, mejor rendimiento  
📊 **Visualización mejorada** - Mensajes con colores según contexto  

---

## 📋 Estructura del Código (13 Partes Actualizadas)

### Parte 1: Configuración y Colores
- Define las configuraciones de dificultad
- **Clase `Colores`** con códigos ANSI
- Diccionario `COLORES_NUMEROS` para mapeo
- Variable `ARCHIVO_PUNTUACIONES` para persistencia

### Parte 2: Crear Tablero
Crea una matriz vacía llena de ceros (tamaño dinámico)

### Parte 3: Colocar Minas
Coloca minas aleatoriamente usando `-1` para representarlas

### Parte 4: Calcular Números
Cuenta las minas adyacentes para cada celda

### Parte 5: Tablero Visible
Crea el tablero que ve el jugador (con `#` para celdas cubiertas)

### Parte 6: Mostrar Tablero
- Imprime el tablero con **colores ANSI**
- Números con colores distintivos
- Coordenadas resaltadas en cian
- Minas con fondo rojo

### Parte 7: Descubrir Celda
- **Algoritmo iterativo** usando pila en lugar de recursión
- Evita `RecursionError` en tableros grandes
- Más eficiente en memoria
- Mismo comportamiento, mejor rendimiento

### Parte 8: Verificar Victoria
Comprueba si solo quedan las minas por descubrir (victoria)

### Parte 9: Mostrar Minas
Muestra todas las minas cuando pierdes

### Parte 9B: Funciones Auxiliares
- **`proteger_primera_jugada()`**: Mueve mina si primera jugada la toca
- **`cargar_puntuaciones()`**: Lee mejores tiempos desde `puntuaciones.json`
- **`guardar_puntuacion()`**: Guarda nuevo récord (redondeado a 2 decimales) con codificación UTF-8
- **`mostrar_ayuda()`**: Muestra pantalla de ayuda completa
- **`obtener_celda_segura()`**: Encuentra celda sin mina para pistas

### Parte 10: Menú de Dificultad
Muestra opciones y permite seleccionar nivel de dificultad

### Parte 11: Función Principal
- **Cronómetro en tiempo real** con `time.time()`
- **Protección de primera jugada** automática
- **Procesamiento de comandos especiales** (ayuda, pista, rendirse, salir)
- **Mensajes con colores** según contexto
- **Sistema de puntuaciones** integrado
- **Detección de récords** y notificación

### Parte 12: Punto de Entrada
Inicia el programa mostrando el menú de dificultad

---

## 🎮 Cómo Funciona el Juego

### Flujo de Juego Completo

1. **Menú inicial**: 
   - Elige entre Fácil, Medio o Difícil
   - Muestra el récord actual si existe

2. **Pantalla de inicio**:
   - Muestra configuración del juego
   - Muestra mejor tiempo del nivel
   - Indica que puedes escribir 'ayuda'
   - Inicia el cronómetro

3. **Primera jugada**:
   - **Protegida**: Si hay mina, se mueve automáticamente
   - Siempre es segura

4. **Durante el juego**:
   - Tablero con colores
   - Cronómetro visible en cada turno
   - Introduce coordenadas o comandos especiales
   - Usa `pista` si necesitas ayuda
   - Usa `ayuda` para ver todos los comandos

5. **Resultados**:
   - Si pisa una mina (💣) → **PIERDE**
     - Muestra tiempo de juego
     - Revela todas las minas en rojo
   - Si descubre todas las celdas seguras → **GANA** 🎉
     - Muestra tiempo final
     - Guarda puntuación
     - Notifica si es nuevo récord 🏆

6. **Rejugabilidad**: 
   - Puede elegir otra dificultad
   - Los récords se guardan entre sesiones

---

## 📁 Archivos Generados

### `puntuaciones.json`
Almacena los mejores tiempos por dificultad (redondeados a 2 decimales, codificación UTF-8):
```json
{
    "Fácil": 45.23,
    "Medio": 123.67,
    "Difícil": 289.45
}
```

> **Nota**: Se usa `ensure_ascii=False` para que los nombres con tilde (Fácil, Difícil) se muestren correctamente en lugar de códigos escape como `F\u00e1cil`.

---

## 🐛 Problemas encontrados

### 1. Victoria No Detectada con Pistas 🔧
**Problema**: Al usar el comando `pista` para descubrir las últimas celdas seguras, el juego no detectaba la victoria automáticamente. El jugador tenía que introducir coordenadas y pisar una mina para terminar el juego.

**Causa**: La función `jugar()` llamaba a `descubrir_celda()` después de usar una pista, pero no verificaba si se había ganado el juego.

**Solución**: Se añadió la verificación `verificar_victoria()` después de descubrir una celda mediante pista, con el mismo flujo de victoria que las jugadas normales:
```python
if verificar_victoria(tablero_visible):
    # Muestra mensaje de victoria
    # Calcula tiempo final
    # Guarda puntuación
    # Notifica si es récord
    juego_activo = False
    break
```

**Resultado**: Ahora el juego detecta correctamente la victoria independientemente de si la última celda se descubre manualmente o mediante pista.

### 2. Desalineación de Tablero en Modos Fácil y Medio 🔧
**Problema**: En los modos Fácil (6x6) y Medio (8x8), las columnas no estaban alineadas correctamente con el encabezado.

**Causa**: El margen inicial del encabezado usaba un cálculo dinámico `" " * (ancho_fila + 1)` que daba 2 espacios en tableros pequeños, pero los números de fila usaban formato `:2d` + espacio = 3 caracteres.

**Solución**: Se cambió a un margen fijo de 3 espacios que coincide con el ancho de los números de fila:
```python
# ANTES: Margen dinámico (causaba desalineación)
print("\n" + Colores.CIAN + " " * (ancho_fila + 1), end="")

# DESPUÉS: Margen fijo de 3 espacios
print("\n" + Colores.CIAN + "   ", end="")
```

**Resultado**: Ahora todos los tableros están perfectamente alineados en todos los niveles de dificultad (Fácil, Medio, Difícil).

### 3. Precisión de Tiempos en JSON 🔧
**Problema**: Los tiempos se guardaban con muchos decimales (ej: `12.77432966232299`).

**Solución**: Se redondea a 2 decimales antes de guardar:
```python
tiempo_redondeado = round(tiempo, 2)
```

**Resultado**: Los tiempos ahora se muestran legibles (ej: `12.56`).

### 4. Codificación de Caracteres en JSON 🔧
**Problema**: Los nombres con tilde aparecían como códigos escape (ej: `F\u00e1cil` en lugar de `Fácil`).

**Solución**: Se añadió codificación UTF-8 y `ensure_ascii=False`:
```python
with open(ARCHIVO_PUNTUACIONES, 'w', encoding='utf-8') as f:
    json.dump(puntuaciones, f, indent=4, ensure_ascii=False)
```

**Resultado**: Los nombres se muestran correctamente con tildes (`Fácil`, `Difícil`).

---

## 🔧 Evolucion del código del juego

### 1. Algoritmo Iterativo vs Recursivo
**Antes**: Usaba recursión para expandir celdas vacías  
**Ahora**: Usa una pila (stack) para iteración  
**Beneficio**: Sin límites de profundidad, mejor rendimiento

### 2. Protección de Primera Jugada
**Problema Original**: Podías perder en el primer click  
**Solución**: Si la primera celda tiene mina, se mueve automáticamente  
**Resultado**: Experiencia más justa

### 3. Sistema de Colores
**Antes**: Todo en blanco y negro  
**Ahora**: Colores ANSI para mejor visualización  
**Mejora**: Más fácil identificar patrones

### 4. Persistencia de Datos
**Nuevo**: Sistema JSON para guardar récords  
**Ubicación**: `puntuaciones.json` en el mismo directorio  
**Beneficio**: Competición contra tus mejores tiempos

### 5. Alineación Perfecta del Tablero
**Mejora**: Margen fijo de 3 espacios en el encabezado  
**Implementación**: `print("\n" + Colores.CIAN + "   ", end="")` coincide con `:2d` + espacio  
**Resultado**: Alineación perfecta en todos los niveles (Fácil, Medio, Difícil)

### 6. Mejor Legibilidad de Puntuaciones
**Mejora**: Tiempos redondeados y caracteres UTF-8  
**Implementación**: `round(tiempo, 2)` + `ensure_ascii=False`  
**Resultado**: `"Fácil": 12.56` en lugar de `"F\u00e1cil": 12.77432966232299`

---

## 📊 Tabla comparativa

| Aspecto | Versión Original | Versión Mejorada |
|---------|------------------|------------------|
| **Interfaz** | Monocromática | 🎨 Colores ANSI |
| **Primera jugada** | Puede ser mina | 🛡️ Siempre segura |
| **Algoritmo expansión** | Recursivo | 🚀 Iterativo (pila) |
| **Cronómetro** | ❌ No | ⏱️ Sí (MM:SS) |
| **Puntuaciones** | ❌ No | 🏆 Sí (persistentes) |
| **Comandos extras** | ❌ No | ⌨️ 4 comandos |
| **Sistema pistas** | ❌ No | 💡 Sí |
| **Mensajes** | Simples | 📊 Con colores contextuales |
| **Rendimiento** | Limitado | 🚀 Optimizado |
