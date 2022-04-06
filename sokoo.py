class Sokoban:
  """
  Definimos los componentes

  0 - Muñeco
  1 - Espacio
  2 - Caja
  3 - Pared
  4 - Meta
  5 - Muñeco_meta
  6 - Caja_meta

  Reglas validas para moverse (Arriba, Derecha, Abajo, Izquierda)

  00 - Muñeco, camino -> [0,1] -> [1,0]
  01 - Muñeco, camino
  02 - Muñeco, caja, camino
  03 - Muñeco, caja, meta
  04 - Muñeco, caja_meta, camino
  05 - Muñeco, caja_meta, meta

  06 - Muñeco_meta, camino
  07 - Muñeco_meta, camino
  08 - Muñeco_meta, caja, camino
  09 - Muñeco_meta, caja, meta
  10 - Muñeco_meta, caja_meta, camino
  11 - Muñeco_meta, caja_meta, meta

  Derecha -> muneco_columna + 1
  Izquierda -> muneco_columna -1
  Abajo -> muneco_fila + 1
  Arriba -> muneco_fila - 1

  """
  mapa = [
      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
      [1,3,3,3,1,1,1,1,1,3,3,3,1,1,1,1,1,1,1,1],
      [1,3,0,3,1,1,1,1,1,3,1,3,3,3,3,3,3,1,1,1],
      [1,3,1,3,3,3,3,3,3,3,1,1,3,1,1,3,3,1,1,1],
      [1,3,1,3,1,1,1,1,1,1,1,1,3,2,1,3,3,3,3,1],
      [1,3,1,1,4,1,2,1,1,3,3,3,3,1,1,3,3,3,3,1],
      [1,3,1,1,1,1,3,3,1,1,1,1,1,1,1,1,3,3,3,3],
      [1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,1,1,4,3],
      [1,3,1,1,1,1,1,1,1,3,3,3,3,1,1,1,1,1,4,4],
      [1,3,1,2,1,1,1,1,1,1,1,1,1,1,1,3,1,1,4,4],
      [1,3,1,1,1,1,1,1,1,3,1,1,1,1,1,3,3,3,3,4],
      [1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,1,1,1],
  ]

  #Posicion inicial del muñeco en el mapa
  muneco_fila = 2
  muneco_columna = 2

  def imprimirMapa(self):
    """Imprime el mapa completo
    """
    for fila in self.mapa:
        print(fila)

  def moverDerecha(self):
    """Controla el movimiento del muñeco a la derecha
    """
    #00 - Muñeco, camino -> [0,1] -> [1,0]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
            self.muneco_columna += 1
      
    #01 - Muñeco, meta -> [0,4] -> [1,5]        
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
            self.muneco_columna += 1
      
    #02 - Muñeco_meta, espacoio -> [0, 4] -> [1, 5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
            self.muneco_columna += 1

    #03 - Muñeco_meta, meta [5, 4] -> [4, 5]


  def moverIzquierda(self):
    """Controla el movimiento del muñeco a la derecha
    """
    #00 - Muñeco, espacio [1, 0] <- [0,1]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.muneco_columna -= 1
      
    #01 - Muñeco, meta [4, 0] <- [5,1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
            self.muneco_columna -= 1
      
    #02 - Muñeco_meta, espacio [1, 5] <- [0, 4]    
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 1:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
            self.muneco_columna -= 1

      
  def moverAbajo(self):
    """Controla el movimiento del muñeco hacia abajo
    00 -> [3]
    [2] -> [3]
    [3] -> [2]
    """
    #00 - Muñeco, espacio [0, 1] ab [1, 0]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.muneco_fila += 1

    #01 - Muñeco, meta [0, 4] ab [1,5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
            self.muneco_fila += 1
      
    #02 - Muñeco_meta, espacio [5, 1] ab [4, 0]    
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 1:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
            self.muneco_fila += 1

    #03- Muñeco_meta, meta [5, 4] ab [4, 5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila +1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
            self.muneco_fila += 1
      
  def moverArriba(self):
    
    #00 - Muñeco, espacio [1, 0] arr [0, 1]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.muneco_fila -= 1
      
    #01 - Muñeco, meta [4, 0] arr [5,1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 1
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
            self.muneco_fila -= 1
      
    #02 - Muñeco_meta, espacio [1, 5] arr [0, 4]  
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 1:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
            self.muneco_fila -= 1
      
    #03- Muñeco_meta, meta [4, 5] arr [ 5, 4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 4:
            self.mapa[self.muneco_fila][self.muneco_columna] = 4
            self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
            self.muneco_fila -= 1
      
  def jugar(self):
    """Controla el flujo del juego
    """
    while True:
      self.imprimirMapa()
      opciones = "d-Derecha, s-Abajo, a-Izquierda, w-Arriba- q-Salir"
      print(opciones)
      movimiento = input("Mover a: ")
      if movimiento == "d":
        self.moverDerecha()
      elif movimiento == "s":
        self.moverAbajo()
      elif movimiento == "a":
        self.moverIzquierda()
      elif movimiento == "w":
        self.moverArriba()
      elif movimiento == "q":
        break

juego = Sokoban()
juego.jugar()
