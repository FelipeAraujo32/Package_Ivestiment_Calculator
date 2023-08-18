from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk

# Cores -----------------------

cor0 = "#2e2d2b" #Preta
cor1 = "#feffff" #Branca
cor2 = "#4fa882" #Verde
cor3 = "#38576b" #valor
cor4 = "403d3d"
cor5 = "F3E99F" #Amarelo
cor6 = "03091f" #Azul
# Windows ----------------------

windows = Tk()
windows.title("")
windows.geometry("400x350")
windows.configure(background=cor1)
windows.resizable(width=FALSE, height=FALSE)

style = Style(windows)
style.theme_use("clam")

windows.mainloop()