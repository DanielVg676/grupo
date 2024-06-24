class MiClase:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    def mi_metodo(self):
        print("Este es un método de la clase")
    


objeto = MiClase("valor1", "valor2")
print(objeto.atributo1)  # Salida: valor1
objeto.mi_metodo()  # Salida: Este es un método de la clase



class MiClase:
    atributo_de_clase = "Soy un atributo de clase"

    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1  # Atributo de instancia
        self.atributo2 = atributo2  # Atributo de instancia

# Acceder a los atributos de clase
print(MiClase.atributo_de_clase)  # Salida: Soy un atributo de clase

# Crear una instancia y acceder a los atributos de instancia
objeto = MiClase("valor1", "valor2")
print(objeto.atributo1)  # Salida: valor1
print(objeto.atributo2)  # Salida: valor2






class SuperClase:
    def __init__(self, atributo):
        self.atributo = atributo

    def metodo_super(self):
        print("Método de la superclase")

class SubClase(SuperClase):
    def __init__(self, atributo, atributo_sub):
        super().__init__(atributo)
        self.atributo_sub = atributo_sub

    def metodo_sub(self):
        print("Método de la subclase")

# Crear instancia de la subclase
sub_objeto = SubClase("valor_super", "valor_sub")
sub_objeto.metodo_super()  # Salida: Método de la superclase
sub_objeto.metodo_sub()    # Salida: Método de la subclase



if condicion:
    # Bloque de código si la condición es verdadera
elif otra_condicion:
    # Bloque de código si la otra condición es verdadera
else:
    # Bloque de código si ninguna condición es verdadera



for elemento in secuencia:
    # Bloque de código a ejecutar para cada elemento


while condicion:
    # Bloque de código a ejecutar mientras la condición sea verdadera




# Convertir a Mayúsculas/Minúsculas:

cadena = "Hola Mundo"
print(cadena.upper())  # Salida: HOLA MUNDO
print(cadena.lower())  # Salida: hola mundo

# Reemplazar Subcadena:

cadena = "Hola Mundo"
nueva_cadena = cadena.replace("Mundo", "Python")
print(nueva_cadena)  # Salida: Hola Python


# Dividir Cadena:

cadena = "Hola, Mundo, Python"
lista_palabras = cadena.split(", ")
print(lista_palabras)  # Salida: ['Hola', 'Mundo', 'Python']


# Concatenar Cadenas:

cadena1 = "Hola"
cadena2 = "Mundo"
cadena_concatenada = cadena1 + " " + cadena2
print(cadena_concatenada)  # Salida: Hola Mundo





# Convertir Cadena a Entero:

cadena_numero = "123"
numero = int(cadena_numero)
print(numero)  # Salida: 123

# Convertir Entero a Cadena:

numero = 123
cadena_numero = str(numero)
print(cadena_numero)  # Salida: '123'


# Convertir Cadena a Flotante:

cadena_flotante = "123.45"
numero_flotante = float(cadena_flotante)
print(numero_flotante)  # Salida: 123.45


# Convertir Flotante a Cadena:

numero_flotante = 123.45
cadena_flotante = str(numero_flotante)
print(cadena_flotante)  # Salida: '123.45'
