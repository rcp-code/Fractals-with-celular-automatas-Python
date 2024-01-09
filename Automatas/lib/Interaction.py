from tkinter import *


class Ventana(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        # widget puede tomar toda la ventana
        self.pack(fill=BOTH, expand=1)

        # crea un botón enlazado a clickExitButton()
        botonSalida = Button(self, text="Salir", command=self.clickBotonSalida)

        # pone el botón en (0,0)
        botonSalida.place(x=0, y=0)

    def clickBotonSalida(self):
        exit()


root = Tk()
app = Ventana(root)
root.wm_title("Prueba de botón - Tkinter")
root.geometry("320x320")
root.mainloop()
