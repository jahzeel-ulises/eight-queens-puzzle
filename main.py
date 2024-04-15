import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
from src.motionGA import motionGA
from src.motionSA import motionSA


class Window():
    def __init__(self):
        #--------------------------Init window------------------------
        self.window=tk.Tk()
        self.window.title("8-Queen Puzzle")
        self.window.resizable(width=False,height=False)
        #------------Header------------------------------------
        #tamano_poblacion:int = 100, generaciones:int = 1000, prob_crossover:float = 0.8, prob_mutacion:float = 0.2,selection:int = 0, crossover:int=0
        self.labelframe1=ttk.LabelFrame(self.window, text="Algoritmo Genetico")
        self.labelframe1.grid(column=0, row=0, padx=10, pady=10)

        self.labelframe2=ttk.LabelFrame(self.window, text="Recocido simulado")
        self.labelframe2.grid(column=0, row=1, padx=10, pady=10)
        #----------------Add components------------------------
        self.add_components()
        self.add_menu()

        self.window.mainloop()

    def add_components(self)->None:
        """Add all main widgets to the main window.

        Args:
            None
        Returns:
            None
        """
        #--------------------ALGORITMO GENETICO-----------------------------
        #--------------------------Poblacion-------------------------
        self.label1=ttk.Label(self.labelframe1, text="Tamaño población:")
        self.label1.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.strPoblacion=tk.StringVar()
        self.combobox1=ttk.Entry(self.labelframe1, textvariable=self.strPoblacion)
        self.combobox1.grid(column=1, row=0, padx=5, pady=5)

        #--------------------------Generaciones-------------------------
        self.label2=ttk.Label(self.labelframe1, text="Número de generaciones:")
        self.label2.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.strGeneraciones=tk.StringVar()
        self.combobox2=ttk.Entry(self.labelframe1, textvariable=self.strGeneraciones)
        self.combobox2.grid(column=1, row=1, padx=5, pady=5)

        #------------------------Mutacion-----------------------------
        self.label2=ttk.Label(self.labelframe1, text="Probabilidad Mutación:")
        self.label2.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.strMutacion=tk.StringVar()
        self.combobox3=ttk.Entry(self.labelframe1, textvariable=self.strMutacion)
        self.combobox3.grid(column=1, row=2, padx=5, pady=5)

        #-----------------------Seleccion-----------------------------
        self.label2=ttk.Label(self.labelframe1, text="Seleccion:")
        self.label2.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.strSeleccion=tk.StringVar()
        self.combobox4=ttk.Combobox(self.labelframe1,state="readonly",values=["Ruleta","Torneo"], textvariable=self.strSeleccion)
        self.combobox4.grid(column=1, row=3, padx=5, pady=5)

        #----------------------Crossover-----------------------------
        self.label2=ttk.Label(self.labelframe1, text="Crossover:")
        self.label2.grid(column=0, row=4, padx=5, pady=5, sticky="e")
        self.strCrossover=tk.StringVar()
        self.combobox5=ttk.Combobox(self.labelframe1,state="readonly",values=["Uno","Dos"], textvariable=self.strCrossover)
        self.combobox5.grid(column=1, row=4, padx=5, pady=5)

        #------------------Go Button--------------------------------------
        self.boton1=ttk.Button(self.labelframe1, text="Animar", command=self.animateGA)
        self.boton1.grid(column=1, row=5, padx=5, pady=5, sticky="we")
        
        #
        #--------------------Recocido Simulado-----------------------------
        #-----------------------Iteraciones-------------------------------------
        self.label3=ttk.Label(self.labelframe2, text="Iteraciones:")
        self.label3.grid(column=0, row=0, padx=5, pady=5, sticky="e")
        self.strIteraciones=tk.StringVar()
        self.combobox6=ttk.Entry(self.labelframe2,textvariable=self.strIteraciones)
        self.combobox6.grid(column=1, row=0, padx=5, pady=5)

        #-------------------Temperatura Inicial----------------------
        self.label3=ttk.Label(self.labelframe2, text="Temperatura Inicial:")
        self.label3.grid(column=0, row=1, padx=5, pady=5, sticky="e")
        self.strTemperatura=tk.StringVar()
        self.combobox7=ttk.Entry(self.labelframe2,textvariable=self.strTemperatura)
        self.combobox7.grid(column=1, row=1, padx=5, pady=5)

        #-------------------Funcion de Probabilidad--------------------
        self.label2=ttk.Label(self.labelframe2, text="Funcion de probabilidad:")
        self.label2.grid(column=0, row=2, padx=5, pady=5, sticky="e")
        self.strFunc=tk.StringVar()
        self.combobox8=ttk.Combobox(self.labelframe2,state="readonly",values=["exponencial","lineal"], textvariable=self.strFunc)
        self.combobox8.grid(column=1, row=2, padx=5, pady=5)

        #------------------Factor de enfriamiento-----------------------------
        self.label3=ttk.Label(self.labelframe2, text="Factor de enfriamiento:")
        self.label3.grid(column=0, row=3, padx=5, pady=5, sticky="e")
        self.strFe=tk.StringVar()
        self.combobox7=ttk.Entry(self.labelframe2,textvariable=self.strFe)
        self.combobox7.grid(column=1, row=3, padx=5, pady=5)

        #------------------Go Button--------------------------------------
        self.boton1=ttk.Button(self.labelframe2, text="Animar", command=self.animateSA)
        self.boton1.grid(column=1, row=5, padx=5, pady=5, sticky="we")


    def add_menu(self):
        """Create the top menu.

        Args:
            None
        Returns:
            None
        """
        self.menubar1 = tk.Menu(self.window)
        self.window.config(menu=self.menubar1)
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.opciones1.add_command(label="Acerca de...", command=self.about)
        self.menubar1.add_cascade(label="Opciones", menu=self.opciones1)    

    def animateGA(self)->None:
        """Validate the entrys of the combobox and start the animation if they´re correct.

        Args:
            None
        Returns:
            None
        """
        selection = 0
        crossover = 0

        if self.strSeleccion.get() == "Torneo":
            selection = 0
        else:
            selection = 1
        
        if self.strCrossover.get() == "Dos":
            crossover = 1
        else:
            crossover = 0


        try:
            if float(self.strMutacion.get()) > 1 or float(self.strMutacion.get()) < 0:
                messagebox.showerror("Advertencia","La probabilidad de mutación es incorrecta")
                return
        
            if int(self.strPoblacion.get()) <= 0 or int(self.strGeneraciones.get()) <= 0:
                messagebox.showerror("Advertencia","La probabilidad de mutación es incorrecta")
                return
            
            motionGA(int(self.strPoblacion.get()),int(self.strGeneraciones.get()),float(self.strMutacion.get()),selection,crossover)
        except:
            messagebox.showerror("Advertencia","Algun hiperparametro es incorrecto")

    def animateSA(self)->None:
        """Validate the entrys of the combobox and start the animation if they´re correct.

        Args:
            None
        Returns:
            None
        """
        try:
            if int(self.strIteraciones.get()) <= 0:
                messagebox.showerror("Advertencia","Iteraciones incorrectas")
                return
            
            if int(self.strTemperatura.get()) <= 0:
                messagebox.showerror("Advertencia","Temperatura incorrecta")
                return
            
            if self.strFunc.get() =='':
                messagebox.showerror("Advertencia","Escoge una funcion de probabilidad")
                return
            
            if float(self.strFe.get()) <= 0 or float(self.strFe.get()) >=1:
                messagebox.showerror("Advertencia","Factor de enfriamiento no valido")
                return  
            
            motionSA(int(self.strTemperatura.get()),self.strFunc.get(),float(self.strFe.get()),int(self.strIteraciones.get()))

        except:
            messagebox.showerror("Advertencia","Algun hiperparametro es incorrecto")

        
    def about(self):
        messagebox.showinfo("Informacion", "Desarrollado por Jahzeel Ulises Mendez Diaz\nClase: Busqueda de Soluciones e Inferencia Bayesiana.")

Window()
