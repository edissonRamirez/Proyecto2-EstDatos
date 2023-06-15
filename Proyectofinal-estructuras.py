from tkinter import *
import networkx as nx



def seleccionar_origen(opcion):
    GUI.guardar_origen(GUI,opcion)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
def seleccionar_destino(opcion):
    GUI.guardar_destino(GUI,opcion)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
def seleccionar_color(color):
    GUI.guardar_color(GUI,color)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta


    

class GUI:
    def __init__(self):
        self.grafo = nx.Graph()
        self.lista_Nombres=[]
        self.lista_Cambiar=[]
        self.lista_Nombres_Trayectos=[]
        self.duracion = 0
        self.distancia = 0    
        self.circulos=[]# lista donde se guardan los circulos del cambas
        self.lineas=[ ]#lista donde se guardan las lineas del cambas
        self.Textos=[]#Guarda los textos de los aeropuertos
        self.ventana = Tk()# ventana principal
        self.ventana.title("Círculo")
        self.ventana.geometry("1000x500")# tamaño de la ventana

        self.canvas_width = 1000
        self.canvas_height = 400
        self.canvas = Canvas(self.ventana, width=self.canvas_width, height=self.canvas_height)# lugar donde se muestran los circulos y las lineas
        self.canvas.pack(fill='both', expand=True)
        scrollbar = Scrollbar(self.ventana, orient='vertical', command=self.canvas.yview)
        scrollbar.pack(side='right', fill="y")
        self.canvas.config(yscrollcommand=scrollbar.set)

        #aero puerto inicial
        color = "blue"
        pos_x = self.canvas_width // 2
        pos_y = self.canvas_height // 2
        texto1 = "Aerop 1"
        
        self.crear_circulo(pos_x, pos_y, color, texto1)
        
        color = "orange"
        pos_x =300
        pos_y = 100
        texto2 = "Aero 2"
        
        self.crear_circulo(pos_x, pos_y, color, texto2)
        
        color = "black"
        pos_x = 302
        pos_y = 302
        texto3 = "Aero 3"
        self.crear_circulo(pos_x, pos_y, color, texto3)
        
        color = "black"
        pos_x = 700
        pos_y = 103
        texto4 = "Aero 4"
        self.crear_circulo(pos_x, pos_y, color, texto4)
        
        color = "black"
        pos_x = 701
        pos_y = 303
        texto5 = "Aero 5"
        self.crear_circulo(pos_x, pos_y, color, texto5)
        
        self.crear_linea(texto1,texto2,300.0,40.0)
        self.crear_linea(texto2,texto3,300.0,40.0)
        self.crear_linea(texto3,texto1,300.0,40.0)
        self.crear_linea(texto4,texto2,300.0,40.0)
        self.crear_linea(texto1,texto4,300.0,40.0)
        self.crear_linea(texto5,texto3,300.0,40.0)
        
        CrearA= Button(self.ventana, text="Agregar Aeropuerto", command=self.open_form)
        CrearA.pack(side='left', padx=5)
        BuscarA= Button(self.ventana, text="Buscar Aeropuerto", command=self.Buscar_Aero)
        BuscarA.pack(side='left', padx=5)
        EliminarA= Button(self.ventana, text="Eliminar Aeropuerto", command=self.formulario_eliminar)
        EliminarA.pack(side='left', padx=5)
        EditarA= Button(self.ventana, text="Editar Aeropuerto",command=self.formulario_editar_aero)
        EditarA.pack(side='left', padx=5)
        CrearT= Button(self.ventana, text="Crear Trayecto", command=self.open_trayecto)
        CrearT.pack(side='left', padx=5)
        BuscarT= Button(self.ventana, text="Buscar Trayecto", command=self.Buscar_Trayecto)
        BuscarT.pack(side='left', padx=5)
        EliminarT= Button(self.ventana, text="Eliminar Trayecto",command=self.formulario_eliminar_trayecto)
        EliminarT.pack(side='left', padx=5)
        Editart= Button(self.ventana, text="Editar trayecto", command=self.formulario_editar_trayecto)
        Editart.pack(side='left', padx=5)

        self.ventana.mainloop()
        
    def guardar_origen(self,name):#guarda el origen del trayecto seleccionado en open_trayecto
        self.nombre_origen=name
    def guardar_destino(self,name):#guarda el destino del trayecto selleccionado en open_trayecto
        self.nombre_destino=name
        
    def guardar_color(self,color):#guarda el color del aeropuerto seleccionado en open_trayecto
        self.color=color

    def Buscar_Aero(self):
        self.panel = Toplevel(self.ventana)
        self.panel.title("Buscar Aeropuerto")
        lista=self.lista_Nombres# lista de los nombres de las aero lineas
        
        letrero = Label(self.panel, text="Aeropuertos existentes")
        letrero.pack()
        
        opciones = StringVar(self.panel)
        opciones.set(lista[0])
        opcion_menu = OptionMenu(self.panel, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        submit_button = Button(self.panel, text="señalar", command=self.Señalar_Aero)
        submit_button.pack(padx=5)
        submit_button = Button(self.panel, text="cerrar", command=self.cerrar)
        submit_button.pack(padx=5)
    
    def Buscar_Trayecto(self):#Abre una ventada donde se ven las rutas
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres# lista de los nombres de las aero lineas
        
        letrero = Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        letrero2 = Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set("ninguno")# primera opcion
    
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_destino)# menu de opciones de destino
        opcion_menu.pack()
        
        submit_button = Button(self.formulario, text="Señalar", command=self.ruta_mejor)
        submit_button.pack()
        submit_button = Button(self.formulario, text="Cerrar", command=self.cerrar_trayecto)
        submit_button.pack()
    
    def Señalar_Aero(self):# cambia el color del aeropuerto para asi encontrarlo visualmente
        nombre=self.nombre_origen
        if nombre in self.grafo:
            x = self.grafo.nodes[nombre]['x']
            self.cambiar_color(x)
            letrero = Label(self.panel, text="Posion en x")
            letrero.pack(side='left')
            letrero = Label(self.panel, text=self.grafo.nodes[nombre]['x'])
            letrero.pack(side='left')
            letrero = Label(self.panel, text="Pocion en y")
            letrero.pack(side='left')
            letrero = Label(self.panel, text=self.grafo.nodes[nombre]['y'])
            letrero.pack(side='left')
        else:
            self.show_error_window("El aeropuerto no existe")
    def ruta_mejor (self):
        origen=self.nombre_origen
        origen1=self.nombre_origen
        destino1=self.nombre_destino
        destino2=self.nombre_destino
        self.señalar_trayecto(origen,origen1,destino1,destino2)
        letrero3= Label(self.formulario, text="Duracion")
        letrero3.pack()
        letrero3= Label(self.formulario, text=self.duracion)
        letrero3.pack()
        letrero3= Label(self.formulario, text="Distancia")
        letrero3.pack()
        letrero3= Label(self.formulario, text=self.distancia)
        letrero3.pack()
        
    def contenido(self, nombre1, nombre2):
        if nombre1 in self.grafo:
            x1 = int(self.grafo.nodes[nombre1]['x'])
            y1 = int(self.grafo.nodes[nombre1]['y'])
        if nombre2 in self.grafo:
            x2 =int(self.grafo.nodes[nombre2]['x'])
            y2 =int(self.grafo.nodes[nombre2]['y'])
        self.cambiar_color_trayecto(x2,x1,y2,y1)
    def suma (self,duracion, distancia):
        duracion=int(duracion)
        distancia=int(distancia)
        x=int(self.duracion)
        z=int(self.distancia)
        self.duracion=x+duracion
        self.distancia=z+distancia
    def señalar_trayecto(self,origen,origen1,destino, final):# cambia el color de la linea de trayecto para asi identificarla
        valor=True
        if self.grafo.has_edge(origen, destino)==False:
            trayectos = [(origen, destino1) for destino1 in self.grafo.neighbors(origen)]
            for trayecto in trayectos:
                for trayecto1 in trayectos:
                    if self.grafo.has_edge(trayecto1[1], final):
                        self.contenido(trayecto1[1], final)
                        datos_arista = self.grafo.get_edge_data(trayecto1[1], final)
                        self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                        self.contenido(trayecto1[0],trayecto1[1])
                        datos_arista = self.grafo.get_edge_data(trayecto1[0],trayecto1[1])
                        self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                        valor=False
                        return None
                if(valor):
                    trayectos2 = [(trayecto[1], destino2) for destino2 in self.grafo.neighbors(trayecto[1])]
                    for trayecto2 in trayectos2:
                        for trayecto4 in trayectos2:
                            if self.grafo.has_edge(trayecto4[1], final):
                                self.contenido(trayecto4[1], final)
                                datos_arista = self.grafo.get_edge_data(trayecto4[1], final)
                                self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                                self.contenido(trayecto4[0],trayecto4[1])
                                datos_arista = self.grafo.get_edge_data(trayecto4[0],trayecto2[1])
                                self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                                self.contenido(trayecto[0],trayecto[1])
                                datos_arista = self.grafo.get_edge_data(trayecto[0],trayecto[1])
                                self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                                valor=False
                                return None
                        if(trayecto2[1]==final and valor):
                            self.contenido(trayecto2[0],trayecto2[1])
                            datos_arista = self.grafo.get_edge_data(trayecto2[0],trayecto2[1])
                            self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                            return trayecto2[0]
                        else:
                            if(trayecto2[0]!=origen and trayecto2[1]!=origen and trayecto2[0]!=origen1 and trayecto2[1]!=origen1 ):
                                trayecto3=self.señalar_trayecto(trayecto2[1],origen1,final,final)
                                if self.grafo.has_edge(origen1, trayecto3):
                                    self.contenido(origen1,trayecto3)
                                    datos_arista = self.grafo.get_edge_data(origen1,trayecto3)
                                    self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
                                    return None
                                else:
                                    self.contenido(trayecto2[0],trayecto2[1])
                                    datos_arista = self.grafo.get_edge_data(trayecto2[0],trayecto2[1])
                                    self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
            self.contenido(trayecto[0],trayecto[1])
            datos_arista = self.grafo.get_edge_data(trayecto[0],trayecto[1])
            self.suma(int(datos_arista['duracion']), datos_arista['distancia'])
        else:
            self.contenido(origen, destino)
            datos_arista = self.grafo.get_edge_data(origen, destino)
            self.suma(int(datos_arista['duracion']), datos_arista['distancia'])

    def cerrar(self):#cierra el panel ademas de volver el aero puerto a su color original
        self.canvas.itemconfig(self.numero, fill=self.color_original)
        self.panel.destroy()

    def cerrar_trayecto(self):#cierra el panel ademas de volver el trayecto a su color original
        for linea in self.lista_Cambiar:
            self.canvas.itemconfig(linea, fill="black")
            self.duracion=0
            self.distancia=0
            self.formulario.destroy()
            

    def cambiar_color(self, x):
        x1=int(x-30)
        for circulo  in self.circulos:
           if(self.canvas.coords(circulo)[0]==x1):
                self.numero=circulo
                self.color_original = self.canvas.itemcget(circulo, "fill")
                self.canvas.itemconfig(circulo, fill="red")
    def cambiar_color_trayecto(self, x1,x2, y1,y2):
         for linea in self.lineas:
            if (self.canvas.coords(linea)[0]==x1 and self.canvas.coords(linea)[2]==x2 and self.canvas.coords(linea)[1]==y1 and self.canvas.coords(linea)[3]==y2):
                self.lista_Cambiar.append(linea)
                self.numero=linea
                self.color_original = self.canvas.itemcget(linea, "fill")
                self.canvas.itemconfig(linea, fill="red")
                break
            else:
                 if (self.canvas.coords(linea)[0]==x2 and self.canvas.coords(linea)[2]==x1 and self.canvas.coords(linea)[1]==y2 and self.canvas.coords(linea)[3]==y1):
                        self.lista_Cambiar.append(linea)
                        self.numero=linea
                        self.color_original = self.canvas.itemcget(linea, "fill")
                        self.canvas.itemconfig(linea, fill="red")
            
    def formulario_eliminar(self):#Formulario que aparece para elejir que aeropuerto que se va alterar
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Eliminar aeropuerto")
        lista=self.lista_Nombres# lista de los nombres de las aero lineas
        
        letrero = Label(self.formulario, text="Seleccione el Aeropuerto")
        letrero.pack()
        
        self.aeropuerto_seleccionado = StringVar(self.formulario)
        self.aeropuerto_seleccionado.set(lista[0])  # primera opción
        opcion_menu = OptionMenu(self.formulario, self.aeropuerto_seleccionado, *lista,command=seleccionar_origen)
        opcion_menu.pack()

        submit_button = Button(self.formulario, text="Eliminar", command=self.eliminar_aero)
        submit_button.pack(side='bottom')

    def formulario_eliminar_trayecto(self):#Formulario que aparece para elejir que aeropuerto que se va alterar
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Eliminar aeropuerto")
        lista=self.lista_Nombres# lista de los nombres de las aero lineas
        
        letrero = Label(self.formulario, text="seleccione el origen")
        letrero.pack()
        
        self.origen_seleccionado = StringVar(self.formulario)
        self.origen_seleccionado.set(lista[0])  # primera opción
        opcion_menu_origen = OptionMenu(self.formulario, self.origen_seleccionado, *lista, command=seleccionar_origen)
        opcion_menu_origen.pack()
        
        letrero = Label(self.formulario, text="seleccione el destino")
        letrero.pack() 

        self.destino_seleccionado = StringVar(self.formulario)
        self.destino_seleccionado.set(lista[0])  # primera opción
        opcion_menu_destino = OptionMenu(self.formulario, self.destino_seleccionado, *lista, command=seleccionar_destino)
        opcion_menu_destino.pack()

        submit_button = Button(self.formulario, text="Eliminar", command=self.eliminar_lineas)
        submit_button.pack(side='bottom')
        
         
    def eliminar_aero(self):
        nombre = self.nombre_origen
        # Obtener la posición x del aeropuerto seleccionado
        x = self.grafo.nodes[nombre]['x']   # Reemplaza None con el valor correcto de la posición x
        # Eliminar las aristas relacionadas con el aeropuerto
        trayectos_eliminar = [(nombre, destino) for destino in self.grafo.neighbors(nombre)]
        # Eliminar el vértice correspondiente al aeropuerto
        self.grafo.remove_edges_from(trayectos_eliminar)
        if nombre in self.grafo:
            self.grafo.remove_node(nombre)
        
        # Buscar las coordenadas del aeropuerto en self.lista
        if x is not None:
            self.eliminar_circulos(x, nombre)
  
    
    def eliminar_circulos(self, ubicacion, nombre):
        x =int(ubicacion-30)
        x1=ubicacion
        for circulo in self.circulos:
            if self.canvas.coords(circulo)[0] == x:
                self.canvas.delete(circulo)
                self.circulos.remove(circulo)
        
        for texto in self.Textos:
            if self.canvas.itemcget(texto, "text") == nombre:
                self.canvas.delete(texto)
                self.Textos.remove(texto)
        for linea in self.lineas:
            if self.canvas.coords(linea)[0] == x1 or self.canvas.coords(linea)[2] == x1:
                self.canvas.delete(linea)
                self.lineas.remove(linea)
        self.formulario.destroy()

    def eliminar_lineas(self):
        origen = self.nombre_origen
        destino = self.nombre_destino
        x1 = int(self.grafo.nodes[origen]['x']) 
        x2 = int(self.grafo.nodes[destino]['x'])  
        trayectos_eliminar = [(origen, destino) for destino in self.grafo.neighbors(origen)]
        # Eliminar el vértice correspondiente al aeropuerto
        self.grafo.remove_edges_from(trayectos_eliminar)
        for linea in self.lineas:
            print(self.canvas.coords(linea)[0],x1,self.canvas.coords(linea)[2],x2)
            if self.canvas.coords(linea)[0] == x1 and self.canvas.coords(linea)[2] == x2:
                self.canvas.delete(linea)
                self.lineas.remove(linea)
        
        self.formulario.destroy()
        
    def open_trayecto(self):# formulario de creacion de trayectos
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres# lista de los nombres de las aero lineas
        
        letrero = Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones_origen = StringVar(self.formulario)
        opciones_origen.set(lista[0])
        opcion_menu_origen = OptionMenu(self.formulario, opciones_origen, *lista, command=seleccionar_origen)  # menú de opciones de origen
        opcion_menu_origen.pack()  # primera opción
        
        letrero2 = Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones_destino = StringVar(self.formulario)
        opciones_destino.set(lista[0])  # primera opción
    
        opcion_menu_destino = OptionMenu(self.formulario, opciones_destino, *lista, command=seleccionar_destino)# menu de opciones de destino
        opcion_menu_destino.pack()
        
        letrero3= Label(self.formulario, text="Duracion")
        letrero3.pack()
        self.duracion = Entry(self.formulario)# entrada de duracion
        self.duracion.pack()
        
        letrero4= Label(self.formulario, text="Distancia")
        letrero4.pack()
        self.distancia = Entry(self.formulario)# entrada de distancia
        self.distancia.pack()
        
        submit_button = Button(self.formulario, text="crear", command=self.add_trayecto)
        submit_button.pack()
        
    def add_trayecto(self):# es donde se comparan los datos a ver si son correctos
        origen=self.nombre_origen
        destino=self.nombre_destino
        duracion = int(self.duracion.get())
        distancia = int(self.duracion.get())

        if(origen==destino or duracion=='' or distancia==''):
            self.show_error_window("Llene el formulario correctamente")# abre la ventada de error con el mensaje que tiene dentro
        else:
            if self.grafo.has_edge(origen, destino):
                self.show_error_window("Ya existe un trayecto entre los aeropuertos seleccionados")  # muestra error si el trayecto ya existe en el grafo
            else:
                duracion=int(duracion)
                distancia= int(distancia)
                self.crear_linea(origen, destino, duracion, distancia)
                self.formulario.destroy()
    
    def open_form(self):# formulario para crear un aero puerto
        self.form_window = Toplevel(self.ventana)
        self.form_window.title("Agregar círculo")

        name_label = Label(self.form_window, text="Nombre:")
        name_label.pack()
        self.name_entry = Entry(self.form_window)  # guarda el nombre del aeropuerto
        self.name_entry.pack()

        pos_x_label = Label(self.form_window, text="Posición X:")
        pos_x_label.pack()
        self.pos_x_entry = Entry(self.form_window)  # guarda la posición en x del aeropuerto
        self.pos_x_entry.pack()

        pos_y_label = Label(self.form_window, text="Posición Y:")
        pos_y_label.pack()
        self.pos_y_entry = Entry(self.form_window)  # guarda la posición en y del aeropuerto
        self.pos_y_entry.pack()

        color_label = Label(self.form_window, text="Color:")
        color_label.pack()
        Colores = ["blue", "yellow", "orange", "purple", "green", "grey", "black"]  # lista de colores que puede utilizar el usuario
        self.color = StringVar(self.form_window)
        self.color.set(Colores[0])  # primera opción
        opcion_color = OptionMenu(self.form_window, self.color, *Colores)
        opcion_color.pack()

        submit_button = Button(self.form_window, text="Crear", command=self.add_circle)
        submit_button.pack()
        
    def add_circle(self):# compara los datos seleccionado en open_form para ver si son correctos
        name = self.name_entry.get()
        color = self.color.get()
        pos_y = self.pos_y_entry.get()
        pos_x = self.pos_x_entry.get()

        if name == '' or color == "ninguno" or pos_x == '' or pos_y == '':
            self.show_error_window("llena los datos faltantes")# abre una ventada de error si se cumple alguna de las condiciones
        else:
            x=int(self.pos_x_entry.get())
            y=int(self.pos_y_entry.get())

            if self.comprobar(x, y, name): # mira que los aeropuertos no choquen entre sí
                self.grafo.add_node(name, x=x, y=y) # Agregar el aeropuerto como un nodo en el grafo
                self.crear_circulo(x, y, color, name) # crea el área que va a ocupar el aeropuerto
            self.form_window.destroy()

    def show_error_window(self, text):# crea la ventana de error
        error_window = Toplevel(self.ventana)
        error_window.title("Error")

        error_label = Label(error_window, text=text)
        error_label.pack()

        ok_button = Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

    def crear_circulo(self, x, y, color, name ):# crea el area de los aero puertos
        radius = 30
        circulo=self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,fill=color)
        Text=self.canvas.create_text(x, y, text=name, fill="white")
        self.circulos.append(circulo)
        self.Textos.append(Text) # se añaden los datos del aeropuertoa a la lista contenido
        self.grafo.add_node(name)# primero se tenia que crear el nodo pa
        self.grafo.nodes[name]['x'] = x  # Guardar la posición X del aeropuerto en el atributo 'x' del nodo correspondiente en el grafo
        self.grafo.nodes[name]['y'] = y  # Guardar la posición Y del aeropuerto en el atributo 'y' del nodo correspondiente en el grafo
        self.lista_Nombres.append(name)
    def crear_linea(self,origen, destino, duracion, distancia):
        # crea las lineas de trayecto
        if not isinstance(duracion, float) or not isinstance(distancia, float):
            raise TypeError('La duración y la distancia deben ser datos numéricos de tipo Float')
        x = self.grafo.nodes[origen]['x']
        y = self.grafo.nodes[origen]['y']
        x2 = self.grafo.nodes[destino]['x']
        y2 = self.grafo.nodes[destino]['y']
        linea = self.canvas.create_line(x, y, x2, y2, fill="black")
        x=int(duracion)
        y=int(distancia)
        self.grafo.add_edge(origen, destino, duracion=x, distancia=y)#Agregar una arista entre los nodos de origen y destino en el grafo
        self.grafo.add_edge(destino, origen, duracion=x, distancia=y)
        self.lineas.append(linea)
        nombre_trayecto=origen+"-"+destino
        self.lista_Nombres_Trayectos.append(nombre_trayecto)
        
    def comprobar(self,x,y,name):# funcion  que devuelve un boolen si la informacion no esta repetida
        existe= True
        for node in self.grafo.nodes:
            if self.grafo.nodes[node]['x'] is not None and self.grafo.nodes[node]['y'] is not None:
                tamañox1 = self.grafo.nodes[node]['x'] + 30
                tamañox2 = self.grafo.nodes[node]['x'] - 30
                tamañoy1 = self.grafo.nodes[node]['y'] + 30
                tamañoy2 = self.grafo.nodes[node]['y'] - 30
                if (tamañox1 >= x+30 and tamañox2 <= x-30) or (tamañoy1 >= y+30 and tamañoy2 <= y-30) or name == node:
                    self.show_error_window("Este aeropuerto ya existe o choca con otro aeropuerto")
                    existe = False
        return existe
    def editar_aeropuerto(self):

        aeropuerto=self.nombre_origen
        
        # De x hasta y uno son los colores que debe tomar el circulo para formarse
        x=int(self.pos_x_entry.get())-30
        y=int(self.pos_y_entry.get())-30
        x1=int(self.pos_x_entry.get())+30
        y1=int(self.pos_y_entry.get())+30

        if aeropuerto in self.grafo:
        # Busca el primer punto en x del circulo anterior

            x0 = self.grafo.nodes[aeropuerto]['x']
            self.grafo.nodes[aeropuerto]['x'] = int(self.pos_x_entry.get())
            self.grafo.nodes[aeropuerto]['y'] = int(self.pos_y_entry.get())

        #busca el circulo con ese mismo punto inicial en x
        for circulo in self.circulos:
            if(self.canvas.coords(circulo)[0]==x0-30):
                self.canvas.coords(circulo,x,y,x1,y1)
        #busca el texto con ese mismo punto inicial en x
        for texto in self.Textos:
            if(self.canvas.itemcget(texto, "text")==aeropuerto):
                self.canvas.coords(texto, self.pos_x_entry.get(),self.pos_y_entry.get())
                self.formulario.destroy()
        for linea in self.lineas:
            x3=self.canvas.coords(linea)[0]
            y3=self.canvas.coords(linea)[1]
            x2=self.canvas.coords(linea)[2]
            y2=self.canvas.coords(linea)[3]
            print(self.canvas.coords(linea)[0],x1)
            print(self.canvas.coords(linea)[2],x2)
            if(self.canvas.coords(linea)[0]==x0):
                self.canvas.coords(linea,x+30,y+30,x2,y2)
                self.formulario.destroy()
            if(self.canvas.coords(linea)[2]==x0):
                self.canvas.coords(linea,x3,y3,x+30,y+30)
                self.formulario.destroy()

    def editar_trayecto(self):
        origen = self.nombre_origen
        destino = self.nombre_destino
        # nuevo_destino = self.destino_entry.get()
        nueva_duracion = self.duracion.get()
        nueva_distancia = self.distancia.get()

        if self.grafo.has_edge(origen, destino):
            datos_arista = self.grafo.get_edge_data(origen, destino)
            datos_arista['duracion']==nueva_duracion
            datos_arista['distancia']==nueva_distancia
        else:
            self.show_error_window("ruta no existe")

        self.formulario.destroy()

    def formulario_editar_aero(self):# formulario para editar la posicion de un aeropuerto
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Editar aeropuerto")

        lista=self.lista_Nombres# lista de los nombres de los aeropuertos
        letrero = Label(self.formulario, text="Aeropuerto")
        letrero.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set('Ninguno')
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        pos_x_label = Label(self.formulario, text="Posición X:")
        pos_x_label.pack()
        self.pos_x_entry = Entry(self.formulario)#guarda la posicion en x del aeropuerto
        self.pos_x_entry.pack()

        pos_y_label = Label(self.formulario, text="Posición Y:")
        pos_y_label.pack()
        self.pos_y_entry = Entry(self.formulario)#guarda la posicion en y del aeropuerto
        self.pos_y_entry.pack()
        submit_button = Button(self.formulario, text="Editar", command=self.editar_aeropuerto)
        submit_button.pack()

    def formulario_editar_trayecto(self):
        self.formulario = Toplevel(self.ventana)
        self.formulario.title("Editar trayecto")

        lista=self.lista_Nombres # lista de los nombres de las rutas

        letrero = Label(self.formulario, text="Trayecto")
        letrero.pack()
        opciones = StringVar(self.formulario)
        opciones.set('Ninguno') # primera opcion formulario origenes
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)# menu de opciones del los aeropuertos de origen disponibles
        opcion_menu.pack()
        
        opciones = StringVar(self.formulario)
        opciones.set('ninguno')#primera opcion formulario destinos
        opcion_menu = OptionMenu(self.formulario, opciones, *lista, command=seleccionar_destino)# menu de opciones de los aeropuertos de destino disponibles
        opcion_menu.pack()

        pos_x_label = Label(self.formulario, text="Duración")
        pos_x_label.pack()
        self.duracion = Entry(self.formulario)#guarda la duraccion del trayecto especificado
        self.duracion.pack()

        pos_y_label = Label(self.formulario, text="Distancia:")
        pos_y_label.pack()
        self.distancia = Entry(self.formulario)#guarda la la distancia del trayecto
        self.distancia.pack()
        submit_button = Button(self.formulario, text="Editar", command=self.editar_trayecto)
        submit_button.pack()


gui = GUI()