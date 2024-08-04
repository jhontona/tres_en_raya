def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

def imprimir_tablero(tablero):
    for fila in tablero:
        print('|'.join(fila))
        print('-' * 5)

def verificar_ganador(tablero, jugador):
    for fila in tablero:
        if all(celda == jugador for celda in fila):
            return True
        
    for col in range(3):
        if all(fila[col] == jugador for fila in tablero):
            return True
        
    if all(tablero[i][i] == jugador for i in range(3)) or all(tablero[i][2-i] == jugador for i in range(3)):
        return True
    return False

def tablero_lleno(tablero):
    return all(celda != ' ' for fila in tablero for celda in fila)

def jugar():
    tablero = crear_tablero()
    jugador_actual = 'X'

    while True:
        imprimir_tablero(tablero)
        print(f"Turno {jugador_actual}")

        fila = int(input("Fila (0,1,2): "))
        columna = int(input("Columna (0,1,2): "))

        if tablero[fila][columna] != ' ':
            print("Movimiento no valido, intente de nuevo")
            continue

        tablero[fila][columna] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            imprimir_tablero(tablero)
            print(f"Gano {jugador_actual}")
            break

        if tablero_lleno(tablero):
            imprimir_tablero(tablero)
            print("Hay empate")
            break

        jugador_actual = 'O' if jugador_actual == 'X' else 'X'

if __name__ == "__main__":
    jugar()
