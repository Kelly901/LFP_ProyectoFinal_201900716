from tkinter import filedialog as FileDialog
from Descomponer import Descomponer
descomponer=Descomponer()
from GuardarDatos import GuardarDatos
guarda=GuardarDatos()

class Archivo:


    def texto(self):
        fichero=FileDialog.askopenfilename(title="Abrir un fichero")
        fi=open(fichero,mode='r')
        mensaje=fi.read()
        print(mensaje)
        lista_datos=[]
        '''for i in mensaje:
            lista_datos.append(i.strip("\n"))
            
        print(lista_datos)'''

        lista=mensaje.split("*")
        print("Lista......")
        print(lista)
        print("________")
        cadena=""
        print("lista1",lista[0],"\n")
        print("lista 2",lista[1])

        #
      
        #For para descomponer la cadena
        for i in lista:
            if i!="":
                lista2=i.split("\n")
                for j in lista2:
                    if j=="":
                        lista2.remove(j)
                #print(lista2)
                lista3=lista2[1].split(";")
                #print(lista3)
                print(lista2)
                cadena1=""
                for k in range(2,len(lista2)):
                    print(lista2[k])
                    cadena1+=lista2[k]+","
                guarda.guardarDatos(lista2[0],lista3[0],lista3[1],lista3[2],cadena1)
                cadena1=""
        guarda.imprimir()
            
            
                



    '''ruta = filedialog.askopenfilename(title="Seleccione un archivo", 
        filetypes = (("glc files","*.glc"),("all files","*.*")))'''