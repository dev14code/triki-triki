
tablero=[" " for i in range(9)]
def imprimir_tablero():
    fila1= "| {} | {} | {} |".format(tablero[0], tablero[1], tablero[2])
    fila2= "| {} | {} | {} |".format(tablero[3], tablero[4], tablero[5])
    fila3= "| {} | {} | {} |".format(tablero[6], tablero[7], tablero[8])

    print()
    print(fila1)
    print(fila2)
    print(fila3)
    print()

def movimiento_jugador(ficha):
    if ficha=="X":
        numero=1
    elif ficha=="O":
        numero=2
    print("Turno del jugador {}".format(numero))

    try:
      selecion=int(input("Ingrese un numero del 1 al 9: "))
      if selecion<1 or selecion>9:
        print("Por favor ingrese un numero válido del 1 al 9")
        movimiento_jugador(ficha)
          
      elif tablero[selecion-1]==" ":
        tablero[selecion-1]=ficha
      else:
          print("Esa casilla esta ocupada, pierdes tu turno")
        

    except ValueError:
            print("Entrada incorrecta. Por favor, solo ingrese numeros.")
  
def victoria(ficha):
    if (tablero[0]==ficha and tablero[1]==ficha and tablero[2]==ficha) or \
       (tablero[3]==ficha and tablero[4]==ficha and tablero[5]==ficha) or \
       (tablero[6]==ficha and tablero[7]==ficha and tablero[8]==ficha) or \
       (tablero[0]==ficha and tablero[3]==ficha and tablero[6]==ficha) or \
       (tablero[1]==ficha and tablero[4]==ficha and tablero[7]==ficha) or \
       (tablero[2]==ficha and tablero[5]==ficha and tablero[8]==ficha) or \
       (tablero[0]==ficha and tablero[4]==ficha and tablero[8]==ficha) or \
       (tablero[2]==ficha and tablero[4]==ficha and tablero[6]==ficha):
        return True
    else:
        return False
  
def empate():
    if " " not in tablero:
        return True
    else:
        return False

while True:
    
    imprimir_tablero()
    movimiento_jugador("X")
    imprimir_tablero()
    if victoria("X"):
        print("Gano el jugador 1")
        break
    elif empate():
        print("Esto es empate")
        break
    
    movimiento_jugador("O")
    if victoria("O"):
        imprimir_tablero()
        print("Gano el jugador 2")
        break
    elif empate():
        print("Esto es empate")
        break
    
