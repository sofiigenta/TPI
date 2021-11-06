
from SocioVip import SocioVIP
from Query import query
from IngresoYCondicion_sociosvip import Ingreso
#Clase socio con sus funciones

class socios:
    def __init__(self):
        self.querys = query()
        self.socios = self.querys.get_all()

    def agregar_socio(self,Nombre,Apellido,DNI,ultimacuotapagada,condicion,VIP):
        if VIP == 'si':
            socio = SocioVIP(Nombre, Apellido,DNI,ultimacuotapagada,condicion,VIP)
        else:
            socio = Ingreso(Nombre,Apellido,DNI,ultimacuotapagada,condicion,VIP)
        
        self.querys.store(socio)
        self.socios.append(socio)

    def buscar_por_numero(self,NumeroDeSocio):
        for socio in self.socios:
            if socio.NumeroDeSocio == NumeroDeSocio:
                return socio
        return None

    def eliminar_socio(self,NumeroDeSocio):
        socio = self.buscar_por_numero(NumeroDeSocio)
        if socio:
            self.querys.delete(socio)
            self.socios.remove(socio)
            return True
        return False

    def buscar_socio(self,filtro):
        socios = []
        for socio in self.socios:
            if socio.buscar_socio(filtro):
                socios.append(socio)
        return socios

    def modificar_cuota(self,NumeroDeSocio,ultimacuotapagada):
        socio = self.buscar_por_numero(NumeroDeSocio)
        if socio:
            socio.ultimacuotapagada = ultimacuotapagada
            self.querys.update(socio)
            return True
        return False

    def mostrar_vips(self, VIP):
        socios = []
        for socio in self.socios:
            if socio.VIP == VIP:
                socios.append(socio)
        return socios

    
