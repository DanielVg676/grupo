import turtle


class JuegoGato:

    def __init__(self):
        self.t = turtle.Turtle()
        self.jugador1 = "         "
        self.jugador2 = "         "
        self.ventana = turtle.Screen()
        self.ventana.setup(width=650, height=900)
        self.ventana.title("Juego del Gato")
        self.ventana.bgcolor("black")

        self.crear_tablero()
        self.botonera()
        self.espectacular()
        self.ventana.onscreenclick(self.detectar_click)
        self.ventana.onscreenclick(self.accionBoton)
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
        self.t.forward(141)  # 100 * sqrt(2) = 141
        self.t.penup()
        self.t.goto(x - 50, y - 50)
        self.t.pendown()
        self.t.setheading(45)
        self.t.forward(141)
        self.t.penup()
        self.t.setheading(0)

    def botonera(self):
        self.t.penup()
        self.t.goto(100,-360)
        self.t.pendown()
        self.t.color("red")
        self.t.begin_fill()
        print("Ubicación esquina superior derecha:", self.t.pos())
        self.t.forward(50)
        self.t.right (90)
        print("Ubicación esquina inferior derecha:", self.t.pos())
        self.t.forward(200)
        self.t.right (90)
        print("Ubicación esquina inferior izquierda:", self.t.pos())
        self.t.forward(50)
        self.t.right (90)
        print("Ubicación esquina superior izquierda:", self.t.pos())
        self.t.forward(200)
        self.t.end_fill()
        self.t.penup()
        self.t.goto(25,-398)
        self.t.right(180)
        self.t.down()
        self.t.color("white")
        self.t.write('EXIT', align="RIGHT", font=("Arial", 16, "bold"))
        self.t.penup()

    def espectacular(self):
        self.t.goto(0, 350)
        self.t.pendown()
        self.t.write('Juego del Gato', align="center", font=("Arial", 48, "bold"))

    def accionBoton(self, x, y):
        if -100 < x < 100 and -410 < y < -360:
            self.cerrar_ventana()
            print("¡Muchas gracias por jugar!")
    
    def detectar_click(self,x,y):
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
            fila = 1
        elif -100 < y < 100:
            fila = 2
        elif -300 < y < -100:
            fila = 3
        else:
            return None

        # transformar a numero pa traducir en lista
        return (fila - 1) * 3 + col

    
juego=JuegoGato()
