<img width="435" height="607" alt="Captura de pantalla 2026-09-24 213726" src="https://github.com/user-attachments/assets/208333f6-090e-4820-8784-5b095071b1aa" />





class Componente:
    def __init__(self, codigo, nombre, cantidad, estado):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = estado

    def mostrar(self):
        print(self.codigo, self.nombre, self.cantidad, self.estado)


class Inventario:
    def __init__(self):
        self.componentes = []

    def agregar(self):
        codigo = input("Digite el codigo: ")
        nombre = input("Digite el nombre: ")
        cantidad = int(input("Digite la cantidad: "))
        estado = input("Digite el estado: ")

        componente = Componente(codigo, nombre, cantidad, estado)
        self.componentes.append(componente)

        print("Componente agregado")

    def mostrar(self):
        if len(self.componentes) == 0:
            print("No hay componentes")
        else:
            print("\nINVENTARIO")
            for componente in self.componentes:
                componente.mostrar()

    def buscar(self):
        codigo = input("Digite el codigo que busca: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                componente.mostrar()
                return

        print("Componente no encontrado")

    def prestar(self):
        codigo = input("Digite el codigo del componente: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                if componente.cantidad > 0:
                    componente.cantidad = componente.cantidad - 1
                    print("Componente prestado")
                else:
                    print("No hay unidades disponibles")
                return

        print("Componente no encontrado")

    def devolver(self):
        codigo = input("Digite el codigo del componente: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                componente.cantidad = componente.cantidad + 1
                print("Componente devuelto")
                return

        print("Componente no encontrado")

    def eliminar(self):
        codigo = input("Digite el codigo del componente: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                self.componentes.remove(componente)
                print("Componente eliminado")
                return

        print("Componente no encontrado")

    def guardar(self):
        archivo = open("inventario.txt", "w")

        for componente in self.componentes:
            archivo.write(componente.codigo + ",")
            archivo.write(componente.nombre + ",")
            archivo.write(str(componente.cantidad) + ",")
            archivo.write(componente.estado + "\n")

        archivo.close()
        print("Inventario guardado")

    def cargar(self):
        try:
            archivo = open("inventario.txt", "r")

            for linea in archivo:
                datos = linea.strip().split(",")

                codigo = datos[0]
                nombre = datos[1]
                cantidad = int(datos[2])
                estado = datos[3]

                componente = Componente(codigo, nombre, cantidad, estado)
                self.componentes.append(componente)

            archivo.close()

        except:
            pass


inventario = Inventario()
inventario.cargar()

opcion = 0

while opcion != 7:

    print("\nINVENTARIO DE ELECTRONICA")
    print("1. Agregar componente")
    print("2. Mostrar componentes")
    print("3. Buscar componente")
    print("4. Prestar componente")
    print("5. Devolver componente")
    print("6. Eliminar componente")
    print("7. Salir")

    opcion = int(input("Digite una opcion: "))

    if opcion == 1:
        inventario.agregar()

    if opcion == 2:
        inventario.mostrar()

    if opcion == 3:
        inventario.buscar()

    if opcion == 4:
        inventario.prestar()

    if opcion == 5:
        inventario.devolver()

    if opcion == 6:
        inventario.eliminar()

    if opcion == 7:
        inventario.guardar()
        print("Programa terminado")
