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
  mapa = []
  muneco_fila = 0
  muneco_columna = 0
  file = open("lvl1.txt","r")

  def __init__(self):
        pass

  def cargarMapa(self):
        for ghy in self.file:
            columna = []
            for digito in ghy:
              if digito == "\n":
                  continue
              columna.append(int(digito))
            self.mapa.append(columna)

  def imprimirMapa(self):
        for fila in self.mapa:
            print(fila)
          
  def munlug(self):
        for fila in range(len(self.mapa)):
            for columna in range (len(self.mapa[fila])):
                if self.mapa[fila][columna] == 0:
                    self.muneco_columna = columna
                    self.muneco_fila = fila
                  
  def cajasmapa(self):
        caj = []
        for fila in self.mapa:
            caj2 = fila.count(2)
            caj.append(caj2)
        if sum(caj) == 0:
            print ("Nivel finalizado...")
            self.completo = True
        else:
            pass

  def moverDerecha(self):
    """Controla el movimiento del muñeco a la derecha"""
    #00 - Muñeco, espacio -> [0,1] -> [1,0]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
      self.muneco_columna += 1
      print("Personaje, espacio, derecha")
      
    #01 - Muñeco, meta -> [0,4] -> [1,5]        
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
      self.muneco_columna += 1
      print("Personaje, meta, derecha")

    #02 - Muñeco_meta, espacio -> [0, 4] -> [1, 5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 0
      self.muneco_columna += 1
      print("Personaje_meta, espacio, derecha")

    #03 - Muñeco_meta, meta [5, 4] -> [4, 5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna + 1] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna + 1] = 5
      self.muneco_columna += 1
      print("Personaje_meta, meta, derecha")

    #04 - Muñeco, caja, espacio [0, 2, 1] -> [1, 0, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 2
      self.muneco_columna += 1
      print("Personaje, caja, espacio, derecha")

    #05 - Muñeco, caja, meta [0, 2, 4] -> [1, 0, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
      self.muneco_columna += 1
      print("Personaje, caja, meta, derecha")

    #06 - Muñeco, caja_meta, espacio [0, 6, 1] -> [1, 5, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 2
      self.muneco_columna += 1
      print("Personaje, caja_meta, espacio, derecha")

    #07 - Muñeco, caja_meta, meta [0, 6, 4] -> [1, 5, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
      self.muneco_columna += 1
      print("Personaje, caja_meta, meta, derecha")

    #08 - Muñeco_meta, caja, espacio [5, 2, 1] -> [4, 0, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 2
      self.muneco_columna += 1
      print("Personaje_meta, caja, espacio, derecha")

    #09 - Muñeco_meta, caja, meta [5, 2, 4] -> [4, 0, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
      self.muneco_columna += 1
      print("Personaje_meta, caja, mwta, derecha")

      #10 - Muñeco_meta, caja_meta, espacio [5, 6, 1] -> [4, 5, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 2
      self.muneco_columna += 1
      print("Personaje_meta, caja_meta, espacio, derecha")

    #11 - Muñeco_meta, caja_meta, meta [5, 6, 4] -> [4, 5, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna +1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna +2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna +1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna +2] = 6
      self.muneco_columna += 1
      print("Personaje_meta, caja_meta, meta, derecha")
 
  def moverIzquierda(self):
    """Controla el movimiento del muñeco a la izquierda"""
    
    #00 - Muñeco, espacio [1, 0] <- [0,1]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.muneco_columna -= 1
      print("Personaje, espacio, izquierda")
      
    #01 - Muñeco, meta [4, 0] <- [5,1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
      self.muneco_columna -= 1
      print("Personaje, meta, izquierda")
      
    #02 - Muñeco_meta, espacio [1, 5] <- [0, 4]    
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.muneco_columna -= 1
      print("Personaje_meta, espacio, izquierda")

    #03 - Muñeco_meta, meta [4, 5] <- [5, 4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
      self.muneco_columna -= 1
      print("Personaje_meta, meta, izquierda")

    #04 - Muñeco, caja, espacio [1, 2, 0] <- [2, 0, 1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 2
      self.muneco_columna -= 1
      print("Personaje, caja, espacio, izquierda")

    #05 - Muñeco, caja, meta [4, 2, 0] <- [6, 0, 1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna- 2] = 6
      self.muneco_columna -= 1
      print("Personaje, caja, meta, izquierda")

    #06 - Muñeco, caja_meta, espacio [1, 6, 0] <- [2, 5, 1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 2
      self.muneco_columna -= 1
      print("Personaje, caja_meta, espacio, izquierda")

    #07 - Muñeco, caja_meta, meta [4, 6, 0] <- [6, 5, 1]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 6
      self.muneco_columna -= 1
      print("Personaje, caja_meta, meta, izquierda")

    #08 - Muñeco_meta, caja, espacio [1, 2, 5] <- [2, 0, 4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 2
      self.muneco_columna -= 1
      print("Personaje_meta, caja, espacio, izquierda")

    #09 - Muñeco_meta, caja, meta [4, 2, 5] <- [6, 0, 4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 2 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 0
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 6
      self.muneco_columna -= 1
      print("Personaje_meta, caja, meta, izquierda")

    #10 - Muñeco_meta, caja_meta, espacio [1, 6, 5] <- [2, 5, 4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 2
      self.muneco_columna -= 1
      print("Personaje_meta, caja_meta, espacio, izquierda")

    #11 - Muñeco_meta, caja_meta, meta [4, 6, 5] <- [6, 5, 4]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila][self.muneco_columna - 1] == 6 and self.mapa[self.muneco_fila][self.muneco_columna - 2] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila][self.muneco_columna - 1] = 5
      self.mapa[self.muneco_fila][self.muneco_columna - 2] = 6
      self.muneco_columna -= 1
      print("Personaje_meta, caja_meta, meta, izquierda")

  def moverAbajo(self):
    """Controla el movimiento del muñeco hacia abajo"""
    
    #00 - Muñeco, espacio [0, 1] ab [1, 0]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.muneco_fila += 1
      print("Personaje, espacio, abajo")

    #01 - Muñeco, meta [0, 4] ab [1,5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
      self.muneco_fila += 1
      print("Personaje, meta, abajo")
      
    #02 - Muñeco_meta, espacio [5, 1] ab [4, 0]    
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.muneco_fila += 1
      print("Personaje_meta, espacio, abajo")

    #03- Muñeco_meta, meta [5, 4] ab [4, 5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila +1][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
      self.muneco_fila += 1
      print("Personaje_meta, meta, abajo")

    #04 - Muñeco, caja, espacio [0, 2, 1] ab [1, 0, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 2
      self.muneco_fila += 1
      print("Personaje, caja, espacio, abajo")

    #05 - Muñeco, caja, meta [0, 2, 4] ab [1, 0, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 6
      self.muneco_fila += 1
      print("Personaje, caja, meta, abajo")

    #06 - Muñeco, caja_meta, espacio [0, 6, 1] ab [1, 5, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 2
      self.muneco_fila += 1
      print("Personaje, caja_meta, espacio, abajo")

    #07 - Muñeco, caja_meta, meta [0, 6, 4] ab [1, 5, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 6
      self.muneco_fila += 1
      print("Personaje, caja_meta, meta, abajo")

    #08 - Muñeco_meta, caja, espacio [5, 2, 1] ab [4, 0, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 2
      self.muneco_fila += 1
      print("Personaje_meta, caja, espacio, abajo")

    #09 - Muñeco_meta, caja, meta [5, 2, 4] ab [4, 0, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 6
      self.muneco_fila += 1
      print("Personaje_meta, caja, meta, abajo")

    #10 - Muñeco_meta, caja_meta, espacio [5, 6, 1] ab [4, 5, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 2
      self.muneco_fila += 1
      print("Personaje_meta, caja_meta, espacio, abajo")

    #11 - Muñeco_meta, caja_meta, meta [5, 6, 4] ab [4, 5, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila + 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila + 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila + 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila + 2][self.muneco_columna] = 6
      self.muneco_fila += 1
      print("Personaje_meta, caja_meta, meta, abajo")

  def moverArriba(self):
    """Controla el movimiento del muñeco hacia arriba"""
    
    #00 - Muñeco, espacio [0, 1] arr [1, 0]
    if self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.muneco_fila -= 1
      print("Personaje, espacio, arriba")
      
    #01 - Muñeco, meta [4, 0] arr [1,5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
      self.muneco_fila -= 1
      print("Personaje, meta, arriba")
      
    #02 - Muñeco_meta, espacio [5, 1] arr [4, ]  
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.muneco_fila -= 1
      print("Personaje_meta, espacio, arriba")
      
    #03- Muñeco_meta, meta [5, 4] arr [ 4, 5]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
      self.muneco_fila -= 1
      print("Personaje_meta, meta, arriba")

    #04 - Muñeco, caja, espacio [0, 2, 1] ab [1, 0, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 2
      self.muneco_fila -= 1
      print("Personaje, caja, espacio, arriba")

    #05 - Muñeco, caja, meta [0, 2, 4] ab [1, 0, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 6
      self.muneco_fila -= 1
      print("Personaje, caja, meta, arriba")

    #06 - Muñeco, caja_meta, espacio [0, 6, 1] ab [1, 5, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 2
      self.muneco_fila -= 1
      print("Personaje, caja_meta, espacio, arriba")

    #07 - Muñeco, caja_meta, meta [0, 6, 4] ab [1, 5, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 0 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 1
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 6
      self.muneco_fila -= 1
      print("Personaje, caja_meta, meta, arriba")

    #08 - Muñeco_meta, caja, espacio [5, 2, 1] ab [4, 0, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 2
      self.muneco_fila -= 1
      print("Personaje_meta, caja, espacio, arriba")

    #09 - Muñeco_meta, caja, meta [5, 2, 4] ab [4, 0, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 2 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 0
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 6
      self.muneco_fila -= 1
      print("Personaje_meta, caja, meta, arriba")

    #10 - Muñeco_meta, caja_meta, espacio [5, 6, 1] ab [4, 5, 2]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 1:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 2
      self.muneco_fila -= 1
      print("Personaje_meta, caja_meta, espacio, arriba")

    #11 - Muñeco_meta, caja_meta, meta [5, 6, 4] ab [4, 5, 6]
    elif self.mapa[self.muneco_fila][self.muneco_columna] == 5 and self.mapa[self.muneco_fila - 1][self.muneco_columna] == 6 and self.mapa[self.muneco_fila - 2][self.muneco_columna] == 4:
      self.mapa[self.muneco_fila][self.muneco_columna] = 4
      self.mapa[self.muneco_fila - 1][self.muneco_columna] = 5
      self.mapa[self.muneco_fila - 2][self.muneco_columna] = 6
      self.muneco_fila -= 1
      print("Personaje_meta, caja_meta, meta, arriba")
      
  def jugar(self):
    """Controla el flujo del juego
    """
    while True:
      self.cargarMapa()
      self.munlug()
      self.imprimirMapa()
      self.cajasmapa()
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
