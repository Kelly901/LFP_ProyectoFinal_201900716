import time
from Archivo import Archivo
from GuardarDatos import GuardarDatos
archivo=Archivo()
gd=GuardarDatos()
class Menu:
    #Cuenta Regresiva
    
    def cuentaRegresiva(self):
        
        print("Kelly Mischel Herrera Espino \n201900716")

        print("El menu se mostrara en:")
        
        #numero=0
       
        #inicio=time.time()
        
        #tiempo=0.0
        #for i in range(0,5):
            #print(i)
            #print(5-i)
            #final=time.sleep(1.0)   
            #print(round(inicio-final,0))
        print("¡Bienvenido!")    
        self.menu()
    #Menu
    def menu(self):

        print(">>>>>Menu Principal<<<<<<<") 

        print("1.Carga de Archivo\n2.Mostrar información general de la Gramática\n3.Generar Autómata de Pila equivalente\n4.Reporte Recorrido\n5.Reporte en Tabla\n6.Salir")   
        opcion=input("Escriba el número de la opción:")   
        self.opciones(opcion)
    #Opciones    
    def opciones(self,opcion):
        if opcion=="1":
            print("Carga de Archivo")
            archivo.texto()
            print("\n____________________")
            self.menu()
        elif opcion=="2":
            print("Información general de la Gramática") 
            gd.mostrar_nombres()
            print("\n____________________")
            self.menu()   
        elif opcion=="3":
            print("Autómata de Pila equivalente")
            nombre=input("nombre")
            gd.generarHtml(nombre)
            print("\n____________________")
            self.menu()
        elif opcion=="4":
            print("Reporte Recorrido")  
            print("\n____________________")
            self.menu() 
        elif opcion=="5":
            print("Reporte en Tabla") 
            print("\n____________________")
            self.menu()   
        elif opcion=="6":
            print("Bye")
           
        else:
            print("La opción no existe.")  
            print("\n____________________")   
            self.menu()         
m=Menu()

m.cuentaRegresiva()

