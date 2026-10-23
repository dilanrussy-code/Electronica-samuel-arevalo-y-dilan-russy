
class Componente:
    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad

    def mostrar(self):
        print("Codigo:", self.codigo)
        print("Nombre:", self.nombre)
        print("Cantidad disponible:", self.cantidad)


class Inventario:
    def __init__(self):
        self.componentes = []
        self.cargar()

        if len(self.componentes) == 0:
            self.componentes.append(Componente("C001", "Resistencias 220 ohm", 100))
            self.componentes.append(Componente("C002", "Resistencias 330 ohm", 100))
            self.componentes.append(Componente("C003", "LED rojo", 50))
            self.componentes.append(Componente("C004", "Protoboard", 15))
            self.componentes.append(Componente("C005", "Cables jumper", 100))
            self.componentes.append(Componente("C006", "Integrado 74HC08", 20))
            self.componentes.append(Componente("C007", "Display 7 segmentos", 20))
            self.guardar()

    def agregar(self):
        codigo = input("Digite el codigo: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                print("Ese codigo ya existe")
                return

        nombre = input("Digite el nombre: ")
        cantidad = int(input("Digite la cantidad: "))

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero")
            return

        componente = Componente(codigo, nombre, cantidad)
        self.componentes.append(componente)
        self.guardar()

        print("Componente agregado")

    def mostrar(self):
        if len(self.componentes) == 0:
            print("No hay componentes")
        else:
            print("\nINVENTARIO DE ELECTRONICA")

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
                    componente.cantidad -= 1
                    self.guardar()
                    print("Componente prestado")
                else:
                    print("No hay unidades disponibles")
                return

        print("Componente no encontrado")

    def devolver(self):
        codigo = input("Digite el codigo del componente: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                componente.cantidad += 1
                self.guardar()
                print("Componente devuelto")
                return

        print("Componente no encontrado")

    def eliminar(self):
        codigo = input("Digite el codigo del componente: ")

        for componente in self.componentes:
            if componente.codigo == codigo:
                self.componentes.remove(componente)
                self.guardar()
                print("Componente eliminado")
                return

        print("Componente no encontrado")

    def guardar(self):
        archivo = open("inventario.txt", "w")

        for componente in self.componentes:
            archivo.write(
                componente.codigo + ","
                + componente.nombre + ","
                + str(componente.cantidad) + "\n"
            )

        archivo.close()

    def cargar(self):
        try:
            archivo = open("inventario.txt", "r")

            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) == 3:
                    componente = Componente(
                        datos[0],
                        datos[1],
                        int(datos[2])
                    )
                    self.componentes.append(componente)

            archivo.close()

        except FileNotFoundError:
            pass


class Usuario:
    def __init__(self, nombre, documento, contrasena, rol):
        self.nombre = nombre
        self.documento = documento
        self.contrasena = contrasena
        self.rol = rol


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.cargar_usuarios()
        self.inventario = Inventario()

    def cargar_usuarios(self):
        try:
            archivo = open("usuarios.txt", "r")

            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) == 4:
                    usuario = Usuario(
                        datos[0], datos[1], datos[2], datos[3]
                    )
                    self.usuarios.append(usuario)

            archivo.close()

        except FileNotFoundError:
            pass

    def guardar_usuarios(self):
        archivo = open("usuarios.txt", "w")

        for usuario in self.usuarios:
            archivo.write(
                usuario.nombre + ","
                + usuario.documento + ","
                + usuario.contrasena + ","
                + usuario.rol + "\n"
            )

        archivo.close()

    def registrar(self):
        print("\nCREAR CUENTA")

        nombre = input("Digite su nombre completo: ")
        documento = input("Digite su numero de documento: ")

        for usuario in self.usuarios:
            if usuario.documento == documento:
                print("Ya existe una cuenta con ese documento")
                return

        contrasena = input("Cree una contrasena: ")

        print("\nSeleccione su rol:")
        print("1. Estudiante")
        print("2. Profesor")

        opcion = input("Digite una opcion: ")

        if opcion == "1":
            rol = "estudiante"

        elif opcion == "2":
            clave = input("Clave de autorizacion para profesor: ")

            if clave == "PROFE2026":
                rol = "profesor"
            else:
                print("Clave incorrecta. No se creo la cuenta.")
                return

        else:
            print("Opcion no valida")
            return

        usuario = Usuario(nombre, documento, contrasena, rol)
        self.usuarios.append(usuario)
        self.guardar_usuarios()

        print("Cuenta creada correctamente")

    def iniciar_sesion(self):
        print("\nINICIO DE SESION")

        documento = input("Numero de documento: ")
        contrasena = input("Contrasena: ")

        for usuario in self.usuarios:
            if (usuario.documento == documento
                    and usuario.contrasena == contrasena):

                print("\nBienvenido", usuario.nombre)
                print("Rol:", usuario.rol)

                self.menu(usuario)
                return

        print("Documento o contrasena incorrectos")

    def menu(self, usuario):
        opcion = ""

        while opcion != "7":
            print("\nINVENTARIO DE LA UNIVERSIDAD")
            print("Usuario:", usuario.nombre)
            print("Rol:", usuario.rol)
            print("1. Mostrar componentes")
            print("2. Buscar componente")
            print("3. Prestar componente")
            print("4. Devolver componente")

            if usuario.rol == "profesor":
                print("5. Agregar componente")
                print("6. Eliminar componente")

            print("7. Cerrar sesion")

            opcion = input("Digite una opcion: ")

            if opcion == "1":
                self.inventario.mostrar()

            elif opcion == "2":
                self.inventario.buscar()

            elif opcion == "3":
                self.inventario.prestar()

            elif opcion == "4":
                self.inventario.devolver()

            elif opcion == "5":
                if usuario.rol == "profesor":
                    self.inventario.agregar()
                else:
                    print("No tiene permiso para esta opcion")

            elif opcion == "6":
                if usuario.rol == "profesor":
                    self.inventario.eliminar()
                else:
                    print("No tiene permiso para esta opcion")

            elif opcion == "7":
                print("Sesion cerrada")

            else:
                print("Opcion no valida")


sistema = Sistema()

opcion = ""

while opcion != "3":
    print("\nINVENTARIO DE ELECTRONICA")
    print("UNIVERSIDAD UPN")
    print("1. Iniciar sesion")
    print("2. Crear cuenta")
    print("3. Salir")

    opcion = input("Digite una opcion: ")

    if opcion == "1":
        sistema.iniciar_sesion()

    elif opcion == "2":
        sistema.registrar()

    elif opcion == "3":
        print("Programa terminado")

    else:
        print("Opcion no valida")
