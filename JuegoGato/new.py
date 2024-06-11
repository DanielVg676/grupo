import turtle

class JuegoGato:

    ganador = [
        ["xxx      "],
        ["   xxx   "],
        ["      xxx"],
        ["x  x  x  "],
        [" x  x  x "],
        ["  x  x  x"],
        ["x   x   x"],
        ["  x x x  "],
        ]

    def __init__(self, tortuga=None):
        if tortuga is None:
            self.t = turtle.Turtle()
        else:
            self.t = tortuga

        self.jugador1 = "         "
        self.jugador2 = "         "
        
        self.ventana = turtle.Screen()
        self.ventana.setup(width=600, height=600)
        self.ventana.title("Juego del Gato")
        self.ventana.bgcolor("black")
        
        self.turno = 0  # Inicializa el contador de turnos
        self.tablero = [['' for _ in range(3)] for _ in range(3)]  # Matriz para el REGISTRO DE MOVIMIENTOS Y ASIGNACION 

        self.crear_tablero()
        self.ventana.onscreenclick(self.detectar_click)
        self.ventana.mainloop()

    def cerrar_ventana(self):
        self.ventana.bye()

    def crear_tablero(self):
        self.t.speed(0)
        self.t.penup()
        self.t.goto(-300, 100)
        self.t.pendown()
        self.t.pensize(10)
        self.t.color("white")
        self.t.forward(600)

        self.t.penup()
        self.t.goto(-300, -100)
        self.t.pendown()
        self.t.forward(600)

        self.t.penup()
        self.t.goto(-100, 300)
        self.t.right(90)
        self.t.pendown()
        self.t.forward(600)

        self.t.penup()
        self.t.goto(100, 300)
        self.t.pendown()
        self.t.forward(600)

    def crear_circulo(self, x, y, radio):
        self.t.penup()
        self.t.goto(x, y - radio)
        self.t.setheading(0)
        self.t.pendown()
        self.t.color("blue")  # Color de la línea del círculo
        self.t.begin_fill()
        self.t.circle(radio)
        self.t.end_fill()
        self.t.penup()

    def crear_tacha(self, x, y):
        self.t.color("red")  # Color de la línea de la tacha
        self.t.penup()
        self.t.goto(x - 50, y + 50)
        self.t.pendown()
        self.t.setheading(-45)
        self.t.forward(141)  # 100 * sqrt(2) ≈ 141
        self.t.penup()
        self.t.goto(x - 50, y - 50)
        self.t.pendown()
        self.t.setheading(45)
        self.t.forward(141)
        self.t.penup()
        self.t.setheading(0)

    def detectar_click(self, x, y):
        seccion = self.convertir_coordenadas_a_seccion(x, y)
        self.jugada(seccion)

    def convertir_coordenadas_a_seccion(self, x, y):
        # Mapear las coordenadas a secciones del tablero
        if -300 < x < -100:
            col = 1
        elif -100 < x < 100:
            col = 2
        elif 100 < x < 300:
            col = 3
        else:
            return None

        if 100 < y < 300:
            row = 1
        elif -100 < y < 100:
            row = 2
        elif -300 < y < -100:
            row = 3
        else:
            return None

        return (row - 1) * 3 + col

    def jugada(self, seccion):
        coordenadas = {
            1: (-200, 200),
            2: (0, 200),
            3: (200, 200),
            4: (-200, 0),
            5: (0, 0),
            6: (200, 0),
            7: (-200, -200),
            8: (0, -200),
            9: (200, -200),
        }

        if seccion is not None and seccion in coordenadas:
            x, y = coordenadas[seccion]
            fila = (seccion - 1) // 3
            columna = (seccion - 1) % 3
            if self.tablero[fila][columna] == '':
                self.t.penup()
                self.t.goto(x, y)
                self.t.pendown()
                
                if self.turno % 2 == 0:
                    self.crear_circulo(x, y, 50)  # Dibuja un círculo
                    self.tablero[fila][columna] = 'O'

                    self.jugador1 = self.jugador1[:seccion-1] + "O" + self.jugador1[seccion:]
                else:
                    self.crear_tacha(x, y)  # Dibuja una tacha
                    self.tablero[fila][columna] = 'X'
                    
                    self.jugador2 = self.jugador2[:seccion-1] + "X" + self.jugador2[seccion:]
                self.turno += 1
                print(self.jugador1)
                print(self.jugador2)
                if not self.nohayganador():
                    self.ventana.bye()
            else:
                print("Sección ya ocupada. Elija otra sección.")
        else:
            print("Sección inválida. Por favor, ingrese un número entre 1 y 9.")

    def nohayganador(self):
        if self.jugador1 in self.ganador:
            print("jugador1 gano")
        for fila in self.tablero:
            if fila[0] == fila[1] == fila[2] != '':
                print(f"El jugador {fila[0]} ha ganado!")
                return False

        for col in range(3):
            if self.tablero[0][col] == self.tablero[1][col] == self.tablero[2][col] != '':
                print(f"El jugador {self.tablero[0][col]} ha ganado!")
                return False

        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != '':
            print(f"El jugador {self.tablero[0][0]} ha ganado!")
            return False

        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != '':
            print(f"El jugador {self.tablero[0][2]} ha ganado!")
            return False

        tablero_lleno = True
        for fila in self.tablero:
            for celda in fila:
                if celda == '':
                    tablero_lleno = False
                    break

        if tablero_lleno:
            print("El juego es un empate!")
            return False

        return True

if __name__ == "__main__":
    juego = JuegoGato()
