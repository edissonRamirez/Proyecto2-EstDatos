import tkinter as tk
import networkx as nx



def seleccionar_origen(opcion):
    gui.guardar_origen(opcion)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
def seleccionar_destino(opcion):
    gui.guardar_destino(opcion)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta
def seleccionar_color(color):
    gui.guardar_color(color)#guarda la opcion seleccionada y la manda a la clase gui para que se pueda usar en esta


    

class GUI:
    def __init__(self):
        self.grafo = nx.Graph()

        self.circulos=[]# lista donde se guardan los circulos del cambas
        self.lineas=[ ]#lista donde se guardan las lineas del cambas
        self.Textos=[]#Guarda los textos de los aeropuertos
        self.ventana = tk() # ventana principal
        self.ventana.title("Círculo")
        self.ventana.geometry("1000x500")# tamaño de la ventana

        self.canvas_width = 1000
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.ventana, width=self.canvas_width, height=self.canvas_height)# lugar donde se muestran los circulos y las lineas
        self.canvas.pack(fill='both', expand=True)
        scrollbar = tk.Scrollbar(self.ventana, orient='vertical', command=self.canvas.yview)
        scrollbar.pack(side='right', fill="y")
        self.canvas.config(yscrollcommand=scrollbar.set)

        #aero puerto inicial
        color = "blue"
        pos_x = self.canvas_width // 2
        pos_y = self.canvas_height // 2
        texto = "Aeropuerto 1"
        
        self.crear_circulo(pos_x, pos_y, color, texto)

        CrearA= tk.Button(self.ventana, text="Agregar Aeropuerto", command=self.open_form)
        CrearA.pack(side='left', padx=5)
        BuscarA= tk.Button(self.ventana, text="Buscar Aeropuerto", command=self.Buscar_Aero)
        BuscarA.pack(side='left', padx=5)
        EliminarA= tk.Button(self.ventana, text="Eliminar Aeropuerto", command=self.formulario_eliminar)
        EliminarA.pack(side='left', padx=5)
        EditarA= tk.Button(self.ventana, text="Editar Aeropuerto")
        EditarA.pack(side='left', padx=5)
        CrearT= tk.Button(self.ventana, text="Crear Trayecto", command=self.open_trayecto)
        CrearT.pack(side='left', padx=5)
        BuscarT= tk.Button(self.ventana, text="Buscar Trayecto", command=self.Buscar_Trayecto)
        BuscarT.pack(side='left', padx=5)
        EliminarT= tk.Button(self.ventana, text="Eliminar Trayecto",command=self.formulario_eliminar_trayecto)
        EliminarT.pack(side='left', padx=5)
        Editart= tk.Button(self.ventana, text="Editar trayecto")
        Editart.pack(side='left', padx=5)

        self.ventana.mainloop()
        
    def guardar_origen(self,name):#guarda el origen del trayecto seleccionado en open_trayecto
        self.nombre_origen=name
    def guardar_destino(self,name):#guarda el destino del trayecto selleccionado en open_trayecto
        self.nombre_destino=name
        
    def guardar_color(self,color):#guarda el color del aeropuerto seleccionado en open_trayecto
        self.color=color

    def Buscar_Aero(self):
        self.panel = tk.Toplevel(self.ventana)
        self.panel.title("Buscar Aeropuerto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = tk.Label(self.panel, text="Aeropuertos existentes")
        letrero.pack()
        
        opciones = tk.StringVar(self.panel)
        opciones.set(lista[0])
        opcion_menu = tk.OptionMenu(self.panel, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        submit_button = tk.Button(self.panel, text="señalar", command=self.Señalar_Aero)
        submit_button.pack(padx=5)
        submit_button = tk.Button(self.panel, text="cerrar", command=self.cerrar)
        submit_button.pack(padx=5)
    
    def Buscar_Trayecto(self):#Abre una ventada donde se ven las rutas
        self.formulario = tk.Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = tk.Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones = tk.StringVar(self.formulario)
        opciones.set("ninguno")
        opcion_menu = tk.OptionMenu(self.formulario, opciones, *lista, command=seleccionar_origen)# menu de opciones de origen
        opcion_menu.pack()#primera opcion
        
        letrero2 = tk.Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones = tk.StringVar(self.formulario)
        opciones.set("ninguno")# primera opcion
    
        opcion_menu = tk.OptionMenu(self.formulario, opciones, *lista, command=seleccionar_destino)# menu de opciones de destino
        opcion_menu.pack()
        
        submit_button = tk.Button(self.formulario, text="Señalar", command=self.señalar_trayecto)
        submit_button.pack()
        submit_button = tk.Button(self.formulario, text="Cerrar", command=self.cerrar_trayecto)
        submit_button.pack()
    
    def Señalar_Aero(self):# cambia el color del aeropuerto para asi encontrarlo visualmente
        nombre=self.nombre_origen
        estado = False  # Inicializar estado como False

        for lista in self.lista:
            if(lista[0]==nombre):
                self.color_original=lista[1]
                lista[1]="red"
                estado= True
                self.cambiar_color(lista, estado)
                letrero = tk.Label(self.panel, text="Posion en x")
                letrero.pack(side='left')
                letrero = tk.Label(self.panel, text=lista[2])
                letrero.pack(side='left')
                letrero = tk.Label(self.panel, text="Pocion en y")
                letrero.pack(side='left')
                letrero = tk.Label(self.panel, text=lista[3])
                letrero.pack(side='left')

        if not estado:
            self.show_error_window("El aeropuerto no existe")

    def señalar_trayecto(self):# cambia el color de la linea de trayecto para asi identificarla
        origen=self.nombre_origen
        destino=self.nombre_destino
        datos=[]
        Trayectos= self.lista_Nombres_Trayectos()
        direccion=origen+"-"+destino
        estado = False  # Inicializar estado como False

        for trayecto in Trayectos:
            if(direccion==trayecto):
                estado=True
                break

        if estado:
            for lista in self.lista:
                if lista[0] == origen:
                    datos.append(lista)
                if lista[0] == destino:
                    datos.append(lista)
            estado = False
            self.cambiar_color(datos, estado)
        else:
            self.show_error_window("El trayecto no existe")

    def cerrar(self):#cierra el panel ademas de volver el aero puerto a su color original
        nombre=self.nombre_origen
        for lista in self.lista:
            if(lista[0]==nombre):
                lista[1]=self.color_original
                estado= True
                self.cambiar_color(lista,estado)
        self.panel.destroy()

    def cerrar_trayecto(self):#cierra el panel ademas de volver el trayecto a su color original
        self.cambiar_color(None,False)
        self.formulario.destroy()

    def cambiar_color(self, listas, Estado):
        if Estado:
            radius = 30
            x = int(listas[2])
            y = int(listas[3])

            self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=listas[1])
            self.canvas.create_text(x, y, text=listas[0], fill="white")
        else:
            self.x = None  # Valor predeterminado para self.x
            self.y = None  # Valor predeterminado para self.y
            self.x2 = None  # Valor predeterminado para self.x2
            self.y2 = None  # Valor predeterminado para self.y2

            for lista in listas:
                if lista[0] == self.nombre_origen:
                    self.x = lista[2]
                    self.y = lista[3]
                elif lista[0] == self.nombre_destino:
                    self.x2 = lista[2]
                    self.y2 = lista[3]

            if self.x is not None and self.y is not None and self.x2 is not None and self.y2 is not None:
                self.canvas.create_line(self.x, self.y, self.x2, self.y2, fill="red")
            else:
                self.canvas.create_line(self.x, self.y, self.x2, self.y2, fill="black")


    def formulario_eliminar(self):#Formulario que aparece para elejir que aeropuerto que se va alterar
        self.formulario = tk.Toplevel(self.ventana)
        self.formulario.title("Eliminar aeropuerto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = tk.Label(self.formulario, text="Seleccione el Aeropuerto")
        letrero.pack()
        
        self.aeropuerto_seleccionado = tk.StringVar(self.formulario)
        self.aeropuerto_seleccionado.set(lista[0])  # primera opción
        opcion_menu = tk.OptionMenu(self.formulario, self.aeropuerto_seleccionado, *lista)
        opcion_menu.pack()

        submit_button = tk.Button(self.formulario, text="Eliminar", command=self.eliminar_aero)
        submit_button.pack(side='bottom')

    def formulario_eliminar_trayecto(self):#Formulario que aparece para elejir que aeropuerto que se va alterar
        self.formulario = tk.Toplevel(self.ventana)
        self.formulario.title("Eliminar aeropuerto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = tk.Label(self.formulario, text="seleccione el origen")
        letrero.pack()
        
        self.origen_seleccionado = tk.StringVar(self.formulario)
        self.origen_seleccionado.set(lista[0])  # primera opción
        opcion_menu_origen = tk.OptionMenu(self.formulario, self.origen_seleccionado, *lista, command=seleccionar_origen)
        opcion_menu_origen.pack()
        
        letrero = tk.Label(self.formulario, text="seleccione el destino")
        letrero.pack() 

        self.destino_seleccionado = tk.StringVar(self.formulario)
        self.destino_seleccionado.set(lista[0])  # primera opción
        opcion_menu_destino = tk.OptionMenu(self.formulario, self.destino_seleccionado, *lista, command=seleccionar_destino)
        opcion_menu_destino.pack()

        submit_button = tk.Button(self.formulario, text="Eliminar", command=self.eliminar_lineas)
        submit_button.pack(side='bottom')
        
         
    def eliminar_aero(self):
        nombre = self.aeropuerto_seleccionado.get()

        # Obtener la posición x del aeropuerto seleccionado
        x = None  # Reemplaza None con el valor correcto de la posición x

        # Eliminar el vértice correspondiente al aeropuerto
        if nombre in self.grafo:
            self.grafo.remove_node(nombre)

        # Eliminar las aristas relacionadas con el aeropuerto
        trayectos_eliminar = [(nombre, destino) for destino in self.grafo.neighbors(nombre)]
        self.grafo.remove_edges_from(trayectos_eliminar)

        # Buscar las coordenadas del aeropuerto en self.lista
        x = None
        for lista in self.lista:
            if lista[0] == nombre:
                x = lista[2]
                break
        
        if x is not None:
            self.eliminar_circulos(x, nombre)
  
    
    def eliminar_circulos(self, x, nombre):
        for circulo in self.circulos:
            if self.canvas.coords(circulo)[0] == x:
                self.canvas.delete(circulo)
        
        for texto in self.Textos:
            if self.canvas.itemcget(texto, "text") == nombre:
                self.canvas.delete(texto)
        
        self.formulario.destroy()

    def eliminar_lineas(self):
        origen = self.nombre_origen
        destino = self.nombre_destino
        print(origen, destino)
        for lista in self.lista:
            if lista[0] == origen:
                x1 = lista[2]
            if lista[0] == destino:
                x2 = lista[2]
        
        nuevos_trayectos = []
        for trayecto in self.lista_trayectos:
            if trayecto[0] != origen or trayecto[1] != destino:
                nuevos_trayectos.append(trayecto)
        
        self.lista_trayectos = nuevos_trayectos
        
        for linea in self.lineas:
            if self.canvas.coords(linea)[0] == x1 and self.canvas.coords(linea)[2] == x2:
                self.canvas.delete(linea)
        
        self.formulario.destroy()
        
                
                
        
    def open_trayecto(self):# formulario de creacion de trayectos
        self.formulario = tk.Toplevel(self.ventana)
        self.formulario.title("Crear trayecto")
        lista=self.lista_Nombres()# lista de los nombres de las aero lineas
        
        letrero = tk.Label(self.formulario, text="origen")
        letrero.pack()
        
        opciones_origen = tk.StringVar(self.formulario)
        opciones_origen.set(lista[0])
        opcion_menu_origen = tk.OptionMenu(self.formulario, opciones_origen, *lista, command=seleccionar_origen)  # menú de opciones de origen
        opcion_menu_origen.pack()  # primera opción
        
        letrero2 = tk.Label(self.formulario,text="Destino")
        letrero2.pack()
        
        opciones_destino = tk.StringVar(self.formulario)
        opciones_destino.set(lista[0])  # primera opción
    
        opcion_menu_destino = tk.OptionMenu(self.formulario, opciones_destino, *lista, command=seleccionar_destino)# menu de opciones de destino
        opcion_menu_destino.pack()
        
        letrero3= tk.Label(self.formulario, text="Duracion")
        letrero3.pack()
        self.duracion = tk.Entry(self.formulario)# entrada de duracion
        self.duracion.pack()
        
        letrero4= tk.Label(self.formulario, text="Distancia")
        letrero4.pack()
        self.distancia = tk.Entry(self.formulario)# entrada de distancia
        self.distancia.pack()
        
        submit_button = tk.Button(self.formulario, text="crear", command=self.add_trayecto)
        submit_button.pack()
        
    def add_trayecto(self):# es donde se comparan los datos a ver si son correctos
        origen=self.nombre_origen
        destino=self.nombre_destino
        duracion = self.duracion.get()
        distancia = self.duracion.get()

        if(origen==destino or duracion=='' or distancia==''):
            self.show_error_window("Llene el formulario correctamente")# abre la ventada de error con el mensaje que tiene dentro
        else:
            if self.grafo.has_edge(origen, destino):
                self.show_error_window("Ya existe un trayecto entre los aeropuertos seleccionados")  # muestra error si el trayecto ya existe en el grafo
            else:
                self.grafo.add_edge(origen, destino, duracion=duracion, distancia=distancia)  # agregar una arista entre los nodos de origen y destino en el grafo
                self.crear_linea(origen, destino, duracion, distancia)
                self.formulario.destroy()
    
    def open_form(self):# formulario para crear un aero puerto
        self.form_window = tk.Toplevel(self.ventana)
        self.form_window.title("Agregar círculo")

        name_label = tk.Label(self.form_window, text="Nombre:")
        name_label.pack()
        self.name_entry = tk.Entry(self.form_window)  # guarda el nombre del aeropuerto
        self.name_entry.pack()

        pos_x_label = tk.Label(self.form_window, text="Posición X:")
        pos_x_label.pack()
        self.pos_x_entry = tk.Entry(self.form_window)  # guarda la posición en x del aeropuerto
        self.pos_x_entry.pack()

        pos_y_label = tk.Label(self.form_window, text="Posición Y:")
        pos_y_label.pack()
        self.pos_y_entry = tk.Entry(self.form_window)  # guarda la posición en y del aeropuerto
        self.pos_y_entry.pack()

        color_label = tk.Label(self.form_window, text="Color:")
        color_label.pack()
        Colores = ["blue", "yellow", "orange", "purple", "green", "grey", "black"]  # lista de colores que puede utilizar el usuario
        self.color = tk.StringVar(self.form_window)
        self.color.set(Colores[0])  # primera opción
        opcion_color = tk.OptionMenu(self.form_window, self.color, *Colores)
        opcion_color.pack()

        submit_button = tk.Button(self.form_window, text="Crear", command=self.add_circle)
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
        error_window = tk.Toplevel(self.ventana)
        error_window.title("Error")

        error_label = tk.Label(error_window, text=text)
        error_label.pack()

        ok_button = tk.Button(error_window, text="OK", command=error_window.destroy)
        ok_button.pack()

    def crear_circulo(self, x, y, color, name ):# crea el area de los aero puertos
        radius = 30
        circulo=self.canvas.create_oval(x-radius, y-radius, x+radius, y+radius,fill=color)
        Text=self.canvas.create_text(x, y, text=name, fill="white")
        self.circulos.append(circulo)
        self.Textos.append(Text) # se añaden los datos del aeropuertoa a la lista contenido

        self.grafo.nodes[name]['x'] = x  # Guardar la posición X del aeropuerto en el atributo 'x' del nodo correspondiente en el grafo
        self.grafo.nodes[name]['y'] = y  # Guardar la posición Y del aeropuerto en el atributo 'y' del nodo correspondiente en el grafo
    def crear_linea(self,origen, destino, duracion, distancia):# crea las lineas de trayecto

        x = self.grafo.nodes[origen]['x']
        y = self.grafo.nodes[origen]['y']
        x2 = self.grafo.nodes[destino]['x']
        y2 = self.grafo.nodes[destino]['y']
        linea = self.canvas.create_line(x, y, x2, y2, fill="black")
        self.grafo.add_edge(origen, destino, duracion=duracion, distancia=distancia)  # Agregar una arista entre los nodos de origen y destino en el grafo
        self.lineas.append(linea)
        
    def comprobar(self,x,y,name):# funcion  que devuelve un boolen si la informacion no esta repetida
        existe= True
        for node in self.grafo.nodes:
            if self.grafo.nodes[node]['x'] is not None and self.grafo.nodes[node]['y'] is not None:
                tamañox1 = self.grafo.nodes[node]['x'] + 30
                tamañox2 = self.grafo.nodes[node]['x'] - 30
                tamañoy1 = self.grafo.nodes[node]['y'] + 30
                tamañoy2 = self.grafo.nodes[node]['y'] - 30
                if (tamañox1 >= x and tamañox2 <= x) or (tamañoy1 >= y and tamañoy2 <= y) or name == node:
                    self.show_error_window("Este aeropuerto ya existe o choca con otro aeropuerto")
                    existe = False
        return existe
    
    def lista_Nombres(self):# crea una lista con los nombres de los aero puertos
        Nombres=[]
        for lista in self.lista:
            Nombres.append(lista[0])
        return Nombres
    def lista_Nombres_Trayectos(self):
        Trayectos=[]
        for lista in self.lista_trayectos:
            Trayectos.append(lista[0]+"-"+lista[1])
        return Trayectos
    def formulario_editar_aero(self):
        self.formulario = tk.Toplevel(self.ventana)
        self.formulario.title("Editar Trayecto")
        lista=self.lista_Nombres()# lista de los nombres de lasaero lineas
        
        
gui = GUI()
