from Datos import Datos
from graphviz import Digraph
import webbrowser


class GuardarDatos:
    dato = []
    #Metodo para guardar las gramatcas en el arreglo de objetos
    def guardarDatos(self, nombre, no_terminales, terminales, dato_inicial, produccion):
        nuevo = Datos(nombre, dato_inicial)
        self.dato.append(nuevo)
        print(no_terminales)
        print(terminales)
        print("______produccion___")
        print(produccion)
        # Terminales
        terminal = terminales.split(",")
        for i in terminal:
            nuevo.terminales[i] = "terminales"
        # No Terminales
        no_Terminal = no_terminales.split(",")
        for j in no_Terminal:
            nuevo.no_terminales[j] = "no_terminales"
        # self.dato.append(Datos(nombre))

        # agregar las producciones
        produc = produccion.split(",")
        for i in range(0, len(produc)-1):

            # p=j.split("-")
            # print("___separar1_____")
            pr = produc[i].split("-")
            # print(pr)
            # print("____separar_____")
            pr2 = produc[i].split(">")

            pr3 = pr2[1].split(" ")
            # comparación de los datos si son terminales
            cont = 0
            '''for z in nuevo.terminales:
                
                for m in pr3:
                    diccionario={}
                    if z==m:
                        print(m,"terminal")
                        diccionario[m]="terminal"
                        
                    print(diccionario)
                    
                    cont+=1'''
            # For comparación de los datos si no son terminales
            nuevo.produccion.append([pr[0], pr3])
            print(":::::::::::::::")
            print(pr3)
            # nuevo.produccion.append(pr3)
            '''for k in nuevo.no_terminales:

                for m in pr3:
                    if k==m:
                        print(m,"no terminales")'''

            # Comparar si los datos son terminales o no terminales

            # print("_____pr3________")

            # nuevo.produccion.append(produc[i])
        print("Esto de es de los termianles")

        '''for i in self.dato:
        
            #i.terminales={"terminales":terminales}
            i.no_terminales["no_terminales"]=no_terminales'''
    #Metodo para imprimir
    def imprimir(self):

        for i in self.dato:
            print(i.nombre)
            print(i.terminales)
            print(i.no_terminales)
            print(i.produccion)
            print(i.dato_inicial)

    #Metodo para mostrar los nombres de las gramaticas
    def mostrar_nombres(self):
        print("")
        print("Listado de gramaticas \n")
        for i in self.dato:
            print(i.nombre)

        print("Escriba el nombre de la gramatica")
        nombre = input("->")
        self.nombre_gramatica(nombre)

    def nombre_gramatica(self, nombre):
        cadena = ""
        cadena1 = ""
        for i in self.dato:
            if i.nombre == nombre:
                print("Nombre de la gramatica: ", i.nombre)
                #
                for j in i.no_terminales:
                    cadena += j+","
                print("No Terminales= {"+cadena+"}")
                for k in i.terminales:
                    cadena1 += k+","
                print("Terminales= {"+cadena1+"}")

                print("No Terminal inicial= "+i.dato_inicial)
                print("producciones")

                for m in i.produccion:
                    cadena2 = ""
                    for z in m[1]:
                        cadena2 += z+" "

                    print(m[0]+"->"+cadena2)

    #Metodo para generar el archivo HTML
    def generarHtml(self, nombre):
        print("hola")
        cadena = ""
        nombreG=""
        #Genera el diagrama de transiciones
        g = Digraph('G', format='png')
        g.attr(rankdir='LR')
        g.node('i')
        g.node('p')
        g.node('q')
        g.node('f')
      
        g.edge('i', 'p', label="λ,λ;#")

        valorI = ""
        cadenaT = ""
        terminal=""
        alfabeto1=""
        alfabeto2=""
        alfabeto=""
        for i in self.dato:
            if nombre == i.nombre:

                valorI = "λ,λ;"+i.dato_inicial
                nombreG=i.nombre
                for k in i.terminales:
                    cadena += k+","+k+";λ\n"
                    terminal+=k+","
                    alfabeto1+=k+","
                for t in i.no_terminales:
                    alfabeto2+=t+","
                    
                for m in i.produccion:
                    cadena2 = ""
                    for z in m[1]:
                        cadena2 += z+" "
                        
                    cadena += "λ,"+m[0]+";"+cadena2+"\n"
        alfabeto=alfabeto1+alfabeto2
        g.edge('p', 'q', label=valorI)
        g.edge('q', 'q', label=cadena)

        g.edge('q', 'f', label="λ,#;λ")
        g.render('imagen')
        #
        #
        #Estructura HTML
        fi = open('Gramatica.html', 'w')

        cuerpo = """<!DOCTYPE html>
            <html lang="en">
            <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Gramatica</title>
    
            </head>
            <body>
            <style>
                #Titulo{
                    color: black;
                    margin: 50px;
                }
            </style>
            <style>
                h2{
                    margin: 20px;
                }
            </style>
            <style>
            #datos{
                width: 500px;
                height: 500px;
            }
            </style>
            <style>
            #imagenes{
                width: 500px;
                height: 500px;
                margin: -400px 550px;
            }
            </style>
            <style>
            #imagenes img{
                width: 600px;
            } 
            </style>
        <div id="datos">
        <h1 id="Titulo">Nombre: """+nombreG+"""</h1>
        <h2>Terminales={"""+terminal+"""}</h2>
        <h2>Alfabeto de Pila={"""+alfabeto+"""#}</h2>
        <h2>Estados={ i,p,q,f }</h2>
        <h2>Estado inicial={i}</h2>
        <h2>Estado de aceptación={f}</h2>
        </div>

        <div id="imagenes">
        <img src="imagen.png"" class="img">
        </div>

    
        </body>
        </html>"""
        fi.write(cuerpo)
        fi.close()
        webbrowser.open_new_tab('Gramatica.html')

#Automata de pila

    def automata(Self):

        cadena=""
        longitud=len(cadena)
        pila=[]
        estado='i'
        i=0
        while(i<longitud):

            if estado=="i":
                pila.append("#")
                estado="p"
            elif estado== "p":
                pila.append("valor Inicial")

                estado="q"
            elif estado=="q":

                for j in range(len(producciones)):
                    stack_top=pila[0]

                    if stack_top=="no termina" and :
                        pila.pop()
                        
                        

                