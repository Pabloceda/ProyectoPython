print("***Hundir la Flota***")

class Barco:
    def __init__(self, longitud):
        self.longitud = longitud
        self.tocados = 0
        
    def esta_hundido(self):
        #Si la cantidad de veces tocado es = a la longitud...
        if self.tocados == self.longitud:
            return True
        else:
            return False

class Tablero:
    def __init__(self):
        self.celdas = [] #Lista vacia
        
        #Creamos 10 filas
        for i in range (10):
            #Cada vuelta se añade una fila d agua
            self.celdas.append(['~'] * 10)
            
            #Herramienta de traducción
        self.letras = ["A","B","C","D","E","F","G","H","I","J"]
        
    def colocar_barco(self, barco, fila, columna, orientacion):
        #En caso de horizontal sumamos columna
        if orientacion == 'H':
            for i in range(barco.longitud):
                self.celdas[fila][columna + i] = "B"
                
        #En caso vertical sumamos filas
        elif orientacion == 'V':
            for i in range (barco.longitud):
                self.celdas[fila + i][columna] = "B"
                
    def disparar(self, fila, columna):
        # Cuando toquemos un barco
        if self.celdas[fila][columna] == "B":
            print("¡Tocado!")
            self.celdas[fila][columna] = "X"
            return "Tocado"
            
        elif self.celdas[fila][columna] == "~":
            print("¡Agua!")
            self.celdas[fila][columna] = "0"
            return "Agua"
        
        else:
            print("¡Ya habías disparado aquí parguela!")
            return "Repetido"

class Jugador:
    def __init__(self):
        self.tablero_propio = Tablero()
        self.tablero_rival = Tablero()
        

#ZONA DE JUEGO#
jugador1 = Jugador()
jugador1.tablero_propio.colocar_barco(Barco(3), 0, 0,"H")

print("Tablero del jugador")
for fila in jugador1.tablero_propio.celdas:
    print (fila)
    
print ("Disparo")
jugador1.tablero_propio.disparar(0, 0)
print ("Despues del disparo")
for fila in jugador1.tablero_propio.celdas:
    print(fila)

