#Ejemplo de import gracias 
import BuscaMinas
print("Iniciando pruebas")
BuscaMinas.FILAS = 5        # type: ignore
BuscaMinas.COLUMNAS = 5     # type: ignore
BuscaMinas.NUM_MINAS = 5    # type: ignore
mi_matriz = BuscaMinas.crear_tablero()

print("Tablero creado de 5 x 5 con exito:")
for fila in mi_matriz:
    print(fila)

"""
Como tenemos diefinidas variable globales, al poner otro numero de filas, columnas y minas
el programa se ejecutará correctamente, pero nos aparecerá una linea roja debajo del numero de filas, columnas y minas
avisandonos de que, oye esto es una variable global que tiene un valor definido en el codigo original.
Para solventar este aviso, debemos usar el comando # type: ignore.  
"""
