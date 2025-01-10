class TicTacToe:
    def __init__(self):
        # Inicializar el tablero como una matriz vacía
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.jugador_actual = "X"

    def mostrar_tablero(self):
        print("\n")
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 9)

    def realizar_movimiento(self, fila, columna):
        # Verifica si la posición es válida y no está ocupada
        if 0 <= fila < 3 and 0 <= columna < 3 and self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = self.jugador_actual
            return True
        else:
            print("Movimiento inválido. Intenta de nuevo.")
            return False

    def comprobar_ganador(self):
        # Comprobar filas, columnas y diagonales
        for fila in self.tablero:
            if all(celda == self.jugador_actual for celda in fila):
                return True

        for col in range(3):
            if all(self.tablero[fila][col] == self.jugador_actual for fila in range(3)):
                return True

        if all(self.tablero[i][i] == self.jugador_actual for i in range(3)) or \
           all(self.tablero[i][2 - i] == self.jugador_actual for i in range(3)):
            return True

        return False

    def tablero_lleno(self):
        # Verificar si todas las celdas están ocupadas
        return all(celda != " " for fila in self.tablero for celda in fila)

    def cambiar_turno(self):
        # Cambiar entre jugadores "X" y "O"
        self.jugador_actual = "O" if self.jugador_actual == "X" else "X"

    def jugar(self):
        print("Bienvenido a Tic-Tac-Toe!")
        self.mostrar_tablero()

        while True:
            print(f"\nTurno del jugador {self.jugador_actual}")
            try:
                fila = int(input("Ingresa la fila (0, 1, 2): "))
                columna = int(input("Ingresa la columna (0, 1, 2): "))
            except ValueError:
                print("Por favor, ingresa números válidos.")
                continue

            if self.realizar_movimiento(fila, columna):
                self.mostrar_tablero()

                if self.comprobar_ganador():
                    print(f"\n¡Felicidades! El jugador {self.jugador_actual} ha ganado.")
                    break

                if self.tablero_lleno():
                    print("\nEl juego terminó en empate.")
                    break

                self.cambiar_turno()


# Ejecutar el juego
if __name__ == "__main__":
    juego = TicTacToe()
    juego.jugar()
