import random


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
                
                
    def es_valido(self, longitud, fila, columna, orientacion):
        #Comprobar si se sale del tablero
        if orientacion == "H":
            if columna + longitud > 10:
                return False
            elif orientacion == "V":
                if fila + longitud > 10:
                    return False
        
        #Comprobar si choca con otro barco
        if orientacion == "H":
            for i in range (longitud):
                if self.celdas[fila][columna + i] != "~":
                    return False
        elif orientacion == "V":
            for i in range (longitud):
                if self.celdas[fila + i][columna] != "~":
                    return False
                
        #Si ha pasado todas las pruebas es valido
        return True
    
    def colocar_aleatorio(self, longitud):
        while True:
            #Se eligen coordenadas y orientacion al azar
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(["H", "V"])
            
            #Si el sitio es valido creamos el barco y lo ponemos
            if self.es_valido(longitud, fila, columna, orientacion):
                barco = barco(longitud)
                self.colocar_barco(barco, fila, columna, orientacion)
                #Terminar el bucle
                break                
                
    
                
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
        






#Prueba de IA
cpu = Jugador()
#Lista de barcos tipicos
flota = [5, 4, 3, 3, 2]
print("Generando flota enemiga...")
for longitud in flota:
    cpu.tablero_propio.colocar_aleatorio(longitud)
    print("Tablero CPU")
    for fila in cpu.tablero_propio.celdas:
        print(fila)











#ZONA DE JUEGO#
#jugador1 = Jugador()
#jugador1.tablero_propio.colocar_barco(Barco(3), 0, 0,"H")

#print("Tablero del jugador")
#for fila in jugador1.tablero_propio.celdas:
  #  print (fila)
    
#print ("Disparo")
#jugador1.tablero_propio.disparar(0, 0)
#print ("Despues del disparo")
#for fila in jugador1.tablero_propio.celdas:
#    print(fila)

