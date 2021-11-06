# Hacemos las querys
# Importamos clases 

from SocioVip import SocioVIP
from Modulo_ultversion import Modulo
from IngresoYCondicion_sociosvip import Ingreso


class query(Modulo):


#Mostrar toda la tabla
    def get_all(self):
        query = "SELECT numero, nombre, apellido, dni, cuota, condicion, vip FROM socios"
        results = self.cursor.execute(query).fetchall()

        
        socios = []
        for result in results:
            if result[6] == 'si':                
                s = SocioVIP(result[1], result[2], result[3], result[4], result[5], result[6], result[0])
                s.ccondicion()
                socios.append(s)
            else:
                s = Ingreso(result[1], result[2], result[3], result[4], result[5], result[6], result[0])
                s.ccondicion()
                socios.append(s)
        
        return socios

#crear socio    
    def store(self, socio):
        try:
            query = "INSERT INTO socios (numero,nombre,apellido,dni,cuota,condicion, vip) VALUES (?, ?, ?, ?, ?, ?, ?)"
            self.cursor.execute(query, [socio.NumeroDeSocio, socio.Nombre, socio.Apellido, socio.DNI, socio.ultimacuotapagada, socio.condicion, socio.VIP])
            self.bd.commit()
            return True
        except:
            self.bd.rollback()
            return False
    
    #Elimina socios
    def delete(self,socio):
        try:
            query = "DELETE FROM socios WHERE numero = ?"
            self.cursor.execute(query, [socio.NumeroDeSocio])

            c = self.cursor.rowcount
            if c == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False

#Modificacion socios
    
    def update(self, socio):
        try:
            query = "UPDATE socios SET cuota = ? WHERE numero = ?"
            result = self.cursor.execute(query, [socio.ultimacuotapagada, socio.NumeroDeSocio])
            if result.rowcount == 0:
                self.bd.rollback()
                return False
            else:
                self.bd.commit()
                return True
        except:
            self.bd.rollback()
            return False
