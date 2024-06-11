import turtle

class Tablero:
    # ________________________________________________ Atributos de la tortuga (Velocidad, abrir ventana y asignacion)
    def __init__(self, tortuga):
        if tortuga is None:
            self.t = turtle.Turtle()
        else:
            self.t = tortuga
        self.ventana = turtle.Screen()
        self.ventana.setup(width=600, height=600)

    def cerrar_ventana(self):
        self.ventana.bye()

    def crear_tablero(self):
        self.t.penup()
        self.t.goto(-300, 100)
        self.t.pendown()
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

# class Cuadro:
#     def __init__(self, tortuga):
#         if tortuga is None:
#             self.t = turtle.Turtle()
#         else:
#             self.t = tortuga

    def dibujar(self, lado):
        for i in range(4):
            self.t.forward(lado)
            self.t.right(90)

class Triangulo:
    def __init__(self, tortuga, lado, coord_x = 0, coord_y = 0):
        if tortuga is None:
            self.t = turtle.Turtle()
        else:
            self.t = tortuga

        self.lado = lado
        self.coord_x = coord_x
        self.coord_y = coord_y

    def dibujar(self):
        self.t.penup()
        self.t.goto(self.coord_x, self.coord_y)
        self.t.pendown()
        for i in range(3):
            self.t.forward(self.lado)
            self.t.right(120)

class Circulo:
    def __init__(self, tortuga, radio, coord_x = 0, coord_y = 0):
        if tortuga is None:
            self.t = turtle.Turtle()
        else:
            self.t = tortuga

        self.radio = radio
        self.coord_x = coord_x
        self.coord_y = coord_y

    def dibujar(self):
        self.t.penup()
        self.t.goto(self.coord_x, self.coord_y)
        self.t.pendown()
        self.t.circle(self.radio)

class Jugador():

    def __init__(self, ficha):
        if ficha == "x":
            self.ficha = True
        else:
            self.ficha = False

class JuegoGato():

    def __init__(self, jugador1, jugador2):
        self.tortu = turtle.Turtle()
        self.tablero = Tablero(self.tortu)
        self.tablero.crear_tablero()
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.quiensigue = True

    def nohayganador(self):
        return True

    def jugada(self,columna, fila):
        coordenada_fila = 30 * fila
        coordenada_columna = 30 * columna

        self.quiensigue = not self.quiensigue

        if self.quiensigue:
            jugada_1 = Circulo(self.tortu, 60,coordenada_columna,coordenada_fila)
        else:
            jugada_1 = Triangulo(self.tortu, 60,coordenada_columna,coordenada_fila)
        
        jugada_1.dibujar()


# Ejemplo de uso
if __name__ == "__main__":
    jugador1 = Jugador("x")
    jugador2 = Jugador("o")
    juego = JuegoGato(jugador1, jugador2)
    while(juego.nohayganador()):
        columna = input("dame la columna")
        fila = input("dame la fila")

        juego.jugada(int(columna),int(fila))
    juego.jugada(-1,-1)
    juego.jugada(-1,0)
