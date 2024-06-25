import turtle
import time

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
        self.ventana.setup(width=650, height=900)
        timestamp = time.strftime("%Y%m%d-%H%M%S")  # Obtener marca de tiempo
        self.archivo = open(f"escribiendo_{timestamp}.txt", "a+")  # Usar la marca de tiempo en el nombre del archivo
        self.ventana.title("Juego del Gato")
        self.ventana.bgcolor("black")
        
        self.turno = 0  # Inicializa el contador de turnos
        self.tablero = [['' for _ in range(3)] for _ in range(3)]  # Matriz para el REGISTRO DE MOVIMIENTOS Y ASIGNACION 

        self.crear_tablero()
        self.botonera()
        self.espectacular()
        self.ventana.onscreenclick(self.convertir_coordenadas_a_seccion)
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

    def convertir_coordenadas_a_seccion(self, x, y):
        # Mapear las coordenadas a secciones del tablero
        if -100 < x < 100 and -410 < y < -360:
            self.cerrar_ventana()
            print("¡Muchas gracias por jugar!")

        if -300 < x < -100:
            col = 1
        elif -100 < x < 100:
            col = 2
        elif 100 < x < 300:
            col = 3
        else:
            return None

        if 100 < y < 300:
            fila = 1
        elif -100 < y < 100:
            fila = 2
        elif -300 < y < -100:
            fila = 3
        else:
            return None

        return (fila - 1) * 3 + col

    def detectar_click(self, x, y):
        seccion = self.convertir_coordenadas_a_seccion(x, y)
        self.jugada(seccion)

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
                    self.tablero[fila][columna] = "O"

                    self.jugador1 = self.jugador1[:seccion-1] + "O" + self.jugador1[seccion:]   # Insertar aqui los el control de co
                    self.archivo.write(f"Jugador 1: {self.jugador1}\n")
                else:
                    self.crear_tacha(x, y)  # Dibuja una tacha
                    self.tablero[fila][columna] = "X"
                    self.jugador2 = self.jugador2[:seccion-1] + "X" + self.jugador2[seccion:]     # Insertar aqui los el control de co
                    self.archivo.write(f"Jugador 2: {self.jugador2}\n")

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
        if self.jugador1 in self.ganador:  # Comprueba si hay una línea ganadora
            print("jugador1 gano")
            return False

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

    def botonera(self):
        self.t.penup()
        self.t.goto(100, -360)
        self.t.pendown()
        self.t.color("red")
        self.t.begin_fill()
        self.t.forward(50)
        self.t.right(90)
        self.t.forward(200)
        self.t.right(90)
        self.t.forward(50)
        self.t.right(90)
        self.t.forward(200)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(25, -398)
        self.t.right(180)
        self.t.down()
        self.t.color("white")
        self.t.write('EXIT', align="RIGHT", font=("Arial", 16, "bold"))
        self.t.penup()

    def espectacular(self):
        self.t.goto(0, 350)
        self.t.pendown()
        self.t.write('Juego del Gato', align="center", font=("Arial", 48, "bold"))
        self.t.penup()

    def accionBoton(self, x, y):
        if -100 < x < 100 and -410 < y < -360:
            self.cerrar_ventana()
            print("¡Muchas gracias por jugar!")

juego = JuegoGato()
