#clase hija
from IngresoYCondicion_sociosvip import Ingreso

class SocioVIP(Ingreso):
    def __init__(self, Nombre, Apellido, DNI, ultimacuotapagada, condicion=None, VIP='si', NumeroDeSocio=None):
        self.VIP = VIP
        super().__init__(Nombre, Apellido, DNI, ultimacuotapagada, condicion, VIP, NumeroDeSocio)
    
    

      
