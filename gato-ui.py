import tkinter as tk
from tkinter import messagebox

def crear_tablero():
    return [[' ' for _ in range(3)] for _ in range(3)]

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

def reiniciar_juego():
    global tablero
    tablero = crear_tablero()

    for i in range(3):
        for j in range(3):
            botones[i][j].config(text=' ')
    jugador_actual[0] = 'X'
    etiqueta_turno.config(text=f"Turno de {jugador_actual[0]}")

def manejar_click(row, col):

    if tablero[row][col] != ' ':
        return

    tablero[row][col] = jugador_actual[0]
    botones[row][col].config(text=jugador_actual[0])

    if verificar_ganador(tablero, jugador_actual[0]):
        messagebox.showinfo("Ganador", f"Gana {jugador_actual[0]}")
        reiniciar_juego()
        return
    
    if tablero_lleno(tablero):
        messagebox.showinfo("Empate", "Es un empate")
        reiniciar_juego()
        return
    
    jugador_actual[0] = 'O' if jugador_actual[0] == 'X' else 'X'
    etiqueta_turno.config(text=f"Turno de {jugador_actual[0]}")

def crear_interfaz():
    global botones, etiqueta_turno
    root = tk.Tk()
    root.title("Triki")

    etiqueta_turno = tk.Label(root, text=f"Turno de {jugador_actual[0]}", font=("Arial", 16))
    etiqueta_turno.pack()

    frame = tk.Frame(root)
    frame.pack()

    botones = [[None for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            boton = tk.Button(frame, text=' ', width=5, height=2, font=("Arial", 20), command=lambda i=i, j=j: manejar_click(i, j))
            boton.grid(row=i, column=j)
            botones[i][j] = boton

    root.mainloop()

if __name__ == "__main__":
    tablero = crear_tablero()
    jugador_actual = ['X']
    crear_interfaz()