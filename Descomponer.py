
class Descomponer:

    def descomponer(self,texto):

        estado=0

        longitud=len(texto)
        pos=0
        cadena=""
        caracter=""
       
        cadena=""
        while texto[pos]!="*":
            #caracter=ord(pos)
            cadena+=texto[pos]
            
            pos+=1
        return cadena   