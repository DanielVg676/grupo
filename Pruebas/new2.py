import turtle
import os

class JuegoGato:
    ganador = [
        {0, 1, 2}, {3, 4, 5}, {6, 7, 8},  # Horizontales
        {0, 3, 6}, {1, 4, 7}, {2, 5, 8},  # Verticales
        {0, 4, 8}, {2, 4, 6}             # Diagonales
    ]

    def __init__(self, tortuga=None):
        if tortuga is None:
            self.t = turtle.Turtle()
        else:
            self.t = tortuga

        self.ventana = turtle.Screen()
        self.ventana.setup(width=600, height=600)
        self.ventana.title("Juego del Gato")
        self.ventana.bgcolor("black")

        self.turno = 0
        self.tablero = [['' for _ in range(3)] for _ in range(3)]
        self.marcas = []
        self.archivo_id = self.obtener_siguiente_id_archivo()
        self.archivo = open(f"datos_{self.archivo_id}.txt", "w")

        self.crear_tablero()
        self.ventana.onscreenclick(self.detectar_click)
        self.ventana.mainloop()

    def obtener_siguiente_id_archivo(self):
        files = [f for f in os.listdir() if f.startswith('datos_') and f.endswith('.txt')]
        if not files:
            return 1
        else:
            return max(int(f.split('_')[1].split('.')[0]) for f in files) + 1

    def cerrar_ventana(self):
        self.archivo.close()
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
        self.t.color("blue")
        self.t.begin_fill()
        self.t.circle(radio)
        self.t.end_fill()
        self.t.penup()

    def crear_tacha(self, x, y):
        self.t.color("red")
        self.t.penup()
        self.t.goto(x - 50, y + 50)
        self.t.pendown()
        self.t.setheading(-45)
        self.t.forward(141)
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
                self.tablero[fila][columna] = 'O' if self.turno % 2 == 0 else 'X'
                self.marcas.append((fila, columna, self.tablero[fila][columna]))
                dibujo = self.crear_circulo if self.turno % 2 == 0 else self.crear_tacha
                dibujo(x, y)

                self.archivo.write('\n'.join(''.join(row) for row in self.tablero) + '\n\n')
                self.turno += 1

                if not self.verificar_ganador():
                    self.cerrar_ventana()
            else:
                print("Sección ya ocupada. Elija otra sección.")
        else:
            print("Sección inválida. Por favor, ingrese un número entre 1 y 9.")

    def verificar_ganador(self):
        posiciones = {idx for idx, marca in enumerate(''.join(row) for row in self.tablero) if marca == ('O' if self.turno % 2 == 0 else 'X')}
        for combo in self.ganador:
            if combo.issubset(posiciones):
                print(f"El jugador {'O' if self.turno % 2 == 0 else 'X'} ha ganado!")
                return False
        if all(c != '' for row in self.tablero for c in row):
            print("El juego es un empate!")
            return False
        return True

if __name__ == "__main__":
    juego = JuegoGato()
