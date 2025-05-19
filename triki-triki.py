# Initialize the game board
tablero=[" " for i in range(9)]

# Function to print the game board
def imprimir_tablero():
    fila1= "| {} | {} | {} |".format(tablero[0], tablero[1], tablero[2])
    fila2= "| {} | {} | {} |".format(tablero[3], tablero[4], tablero[5])
    fila3= "| {} | {} | {} |".format(tablero[6], tablero[7], tablero[8])

    print()
    print(fila1)
    print(fila2)
    print(fila3)
    print()

# Function to handle player moves
def movimiento_jugador(ficha):
    if ficha=="X":
        numero=1
    elif ficha=="O":
        numero=2
    print("Turno del jugador {}".format(numero))

    while True:
        try:
            seleccion=int(input("Ingrese un numero del 1 al 9: "))
            if seleccion<1 or seleccion>9:
                print("Por favor ingrese un numero válido del 1 al 9")
            elif tablero[seleccion-1]==" ":
                tablero[seleccion-1]=ficha
                break
            else:
                print("Esa casilla esta ocupada, por favor elija otra")
        except ValueError:
            print("Entrada incorrecta. Por favor, solo ingrese numeros.")

# Function to check for victory conditions
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

# Function to check for a tie
def empate():
    if " " not in tablero:
        return True
    else:
        return False

# Main function to encapsulate the game loop
def main():
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

# Run the main function
if __name__ == "__main__":
    main()
