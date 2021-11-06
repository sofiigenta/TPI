from Socios import socios
import sys

class Menu:
    #Mostrar un menú y responder a las opciones

    def __init__(self):
        self.planilla = socios()
        self.opciones= {
            "1": self.mostrar_socios,
            "2": self.buscar_socio,
            "3": self.nuevo_socio,
            "4": self.modificar_socio,
            "5": self.eliminar_socio,
            "6": self.mostrar_vips,
            "7": self.salir
        }

    def mostrar_menu(self):
        #Muestra el menú de opciones
        print("""
Menú del anotador:
1. Mostrar todos los socios
2. Buscar socios por dni/numero
3. Agregar socio
4. Modificar cuota de socio
5. Eliminar socio
6. Mostrar socios VIPS
7. Salir
""")

    def ejecutar(self):
        #Mostrar el menu y responder a las opciones.
        while True:
            self.mostrar_menu()
            opcion = input("Ingresar una opción: ")
            accion = self.opciones.get(opcion)
            if accion:
                accion()
            else:
                print("{0} no es una opción válida".format(opcion))
    
    def mostrar_socios(self,socios=None):
        if socios:
            for socio in socios:
                print(socio)
        else:
            for socio in self.planilla.socios:
                print(socio)


    def buscar_socio(self):
        filtro = input('Ingrese un Numero de socio o un numero del DNI: ')
        socios = self.planilla.buscar_socio(filtro)
        if socios:
            self.mostrar_socios(socios)
        else:
            print('Ningun socio coincide')
    
    def nuevo_socio(self):
        VIP = input('Tipee "si" si desea ingresar un socio VIP, de lo contrario ingrese "no": ')
        Nombre = input('Ingrese el nombre del socio: ')
        Apellido = input('Ingrese el apellido del socio: ')
        DNI = int(input('Ingrese su DNI: '))
        ultimacuotapagada = input('Ingrese el mes de la ultima cuota paga: ')
        condicion = input('Ingrese la condicion: ')
        socios = self.planilla.agregar_socio(Nombre,Apellido,DNI,ultimacuotapagada,condicion,VIP)

    def modificar_socio(self):
        NumeroDeSocio = int(input('Ingrese el numero de socio que desea modificar: '))
        ultimacuotapaga = input('Ingrese la ultima cuota paga: ')
        self.planilla.modificar_cuota(NumeroDeSocio,ultimacuotapaga)
        print('Cuota modificada')
        
    def eliminar_socio(self):
        NumeroDeSocio = int(input('Ingrese el numero de socio que desea eliminar: '))
        self.planilla.eliminar_socio(NumeroDeSocio)
        print('Socio eliminado')

    def mostrar_vips(self):
        VIP = 'si'
        socios = self.planilla.mostrar_vips(VIP)
        if socios:
            self.mostrar_socios(socios)
        else:
            print('No hay socios vips')
    
    def salir(self):
        sys.exit(0)





if __name__ == "__main__":
    Menu().ejecutar()
