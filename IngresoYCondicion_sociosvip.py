#Ingresamos socios y condicion
class Ingreso:
    def __init__(self,Nombre, Apellido, DNI, ultimacuotapagada, condicion=None, VIP=None, NumeroDeSocio=None):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.DNI = DNI
        self.ultimacuotapagada = ultimacuotapagada
        self.condicion = condicion
        self.VIP = VIP
        self.NumeroDeSocio = NumeroDeSocio
    
    def ccondicion(self):
        if self.ultimacuotapagada is None:
            self.condicion = 'Adeuda' 
        else:
            self.condicion = 'Al dia'
    
    def __str__(self):
        return 'Numero Socio: '+ str(self.NumeroDeSocio) + '    Nombre: ' + self.Nombre +'    Apellido: ' + self.Apellido + '    DNI: ' + str(self.DNI)+ '  Ultima cuota paga: '+ self.ultimacuotapagada + '    Condicion: '+ self.condicion + '    VIP: '+ self.VIP
        

#Recibe un filtro de busqueda
    def buscar_socio(self, filtro):
        if filtro in str (self.DNI) or filtro in str(self.NumeroDeSocio):
            return True
        else:
            return False
