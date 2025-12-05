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
        if orientacion == 'H':
            if columna + longitud > 10:
                return False
        elif orientacion == 'V':
                if fila + longitud > 10:
                    return False
        
        #Comprobar si choca con otro barco
        if orientacion == 'H':
            for i in range(longitud):
                if self.celdas[fila][columna + i] != "~":
                    return False
        elif orientacion == 'V':
            for i in range(longitud):
                if self.celdas[fila + i][columna] != "~":
                    return False
                
        #Si ha pasado todas las pruebas es valido
        return True
    
    def colocar_aleatorio(self, longitud):
        while True:
            #Se eligen coordenadas y orientacion al azar
            fila = random.randint(0, 9)
            columna = random.randint(0, 9)
            orientacion = random.choice(['H', 'V'])
            
            #Si el sitio es valido creamos el barco y lo ponemos
            if self.es_valido(longitud, fila, columna, orientacion):
                barco = Barco(longitud)
                self.colocar_barco(barco, fila, columna, orientacion)
                #Terminar el bucle
                break  
            
        
    def hay_barcos(self):
        for fila in self.celdas:
            if "B" in fila:
                return True
        return False              
                
    
                
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
        


def jugar():
    #1 Preparativos
    print("===INICIANDO JUEGO===")
    usuario = Jugador()
    cpu = Jugador()
    
    #2 Colocacion de barcos
    flota = [5, 4, 3, 3, 2]
    print("===COLOCANDO BARCOS===")
    for longitud in flota:
        usuario.tablero_propio.colocar_aleatorio(longitud)
        cpu.tablero_propio.colocar_aleatorio(longitud)
        
    #3 Empieza la batalla
    turno_usuario = True
    while True:
        if turno_usuario:
            print("===ES TU TURNO===")
            print("TUS DISPAROS:")
            for fila in usuario.tablero_rival.celdas:
                print (fila)
            
            #Pedimos coordenadas
            coord = input("INTRODUCE TUS COORDENADAS:").upper()
            
            try:
                fila = usuario.tablero_propio.letras.index(coord[0])
                columna = int(coord[1:]) - 1
                resultado = cpu.tablero_propio.disparar(fila, columna)
                if resultado == "Tocado":
                    usuario.tablero_rival.celdas[fila][columna] = "X"
                    print("🔥🔥🔥LE HAS DADO🔥🔥🔥")
                
                elif resultado == "Agua":
                    usuario.tablero_rival.celdas[fila][columna] = "0"
                    print("🌊🌊🌊AGUA🌊🌊🌊")
                
                elif resultado == "Repetido":
                    print("Ya habías disparado ahí")
                    
                if cpu.tablero_propio.hay_barcos() == False:
                    print("🏆🏆🏆¡VICTORIA, HAS HUNDIDO TODOS LOS BARCOS!🏆🏆🏆")
                    break
                    
            
            except:
                print("¡Coordenada no válida! (D1,A3...)")
                continue
            
            
            
        else:
            print("===TURNO DEL RIVAL===")
            
            fila_cpu = random.randint(0, 9)
            col_cpu = random.randint(0, 9)
            print (f"LA CPU DISPARA A: {fila_cpu},{col_cpu}")
            resultado = usuario.tablero_propio.disparar(fila_cpu, col_cpu)
            
            if resultado == "Tocado":
                print("🔥🔥🔥TE HAN DADO🔥🔥🔥")
            
            else:
                print("🌊🌊🌊LA IA HA FALLADO🌊🌊🌊")
                
            if usuario.tablero_propio.hay_barcos() == False:
                print("☠️☠️☠️DERROTA, LA IA HA HUNDIDO TODOS TUS BARCOS☠️☠️☠️")
        
        # Cambiamos de turno
        turno_usuario = not turno_usuario
        
#EMPIEZA EL JUEGO
jugar()





















#Prueba de IA
#cpu = Jugador()
#Lista de barcos tipicos
#flota = [5, 4, 3, 3, 2]
#print("Generando flota enemiga...")
#for longitud in flota:
#    cpu.tablero_propio.colocar_aleatorio(longitud)
#    
#print("Tablero CPU")
#for fila in cpu.tablero_propio.celdas:
#    print(fila)











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

