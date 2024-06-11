import turtle

class TableroGato:

    def __init__(self, size=300):

        self.onscreenclick()
        self.size = size
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)

    def draw_board(self):
        # Primera línea horizontal
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, self.size // 6)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        # Segunda línea horizontal
        self.turtle.penup()
        self.turtle.goto(-self.size // 2, -self.size // 6)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        # Primera línea vertical
        self.turtle.penup()
        self.turtle.goto(-self.size // 6, self.size // 2)
        self.turtle.right(90)
        self.turtle.pendown()
        self.turtle.forward(self.size)
        
        # Segunda línea vertical
        self.turtle.penup()
        self.turtle.goto(self.size // 6, self.size // 2)
        self.turtle.pendown()
        self.turtle.forward(self.size)

    def draw_x(self, center_x, center_y):
        self.turtle.penup()
        self.turtle.goto(center_x - self.size // 6, center_y + self.size // 6)
        self.turtle.pendown()
        self.turtle.goto(center_x + self.size // 6, center_y - self.size // 6)
        self.turtle.penup()
        self.turtle.goto(center_x + self.size // 6, center_y + self.size // 6)
        self.turtle.pendown()
        self.turtle.goto(center_x - self.size // 6, center_y - self.size // 6)

    def draw_circle(self, center_x, center_y):
        self.turtle.penup()
        self.turtle.goto(center_x, center_y - self.size // 6)
        self.turtle.pendown()
        self.turtle.circle(self.size // 6)

    def display(self):
        screen = turtle.Screen()
        self.draw_board()
        
    #     # Dibuja una X en la esquina superior izquierda
    #     self.draw_x(-self.size // 3, self.size // 3)
        
    #     # Dibuja un círculo en la esquina inferior derecha
    #     self.draw_circle(self.size // 4.5, -self.size // 4.5)

    #     screen.mainloop()

# Uso de la clase para dibujar el tablero de gato con una X y un círculo
board = TableroGato(300)
board.display()
