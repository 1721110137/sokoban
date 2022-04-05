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
  ]

  #Posicion inicial del muñeco en el mapa
  muneco_fila = 2
  muneco_columna = 2

  def imprimirMapa(self):
    """Imprime el mapa completo
    """
    file = open("lvl1.txt","r")
    for fila in file:
      print(fila)
      for c in file:
        print(c)

  def moverDerecha(self):
    """Controla el movimiento del muñeco a la derecha
    """
    #00 - Muñeco, camino -> [2,3] -> [3,2]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
      self.muneco_columna += 1

  def moverIzquierda(self):
    """Controla el movimiento del muñeco a la derecha
    """
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.muneco_columna -= 1

  def moverAbajo(self):
    """Controla el movimiento del muñeco hacia abajo
    00 -> [3]
    [2] -> [3]
    [3] -> [2]
    """
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.muneco_fila += 1

  def moverArriba(self):
    
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
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
