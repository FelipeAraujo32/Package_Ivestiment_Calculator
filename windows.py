from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import Entry
from PIL import Image, ImageTk

# Cores -------------------------------------------------------------------

cor0 = "#2e2d2b" #Preta
cor1 = "#feffff" #Branca
cor2 = "#4fa882" #Verde
cor3 = "#38576b" #valor
cor4 = "403d3d"
cor5 = "F3E99F" #Amarelo
cor6 = "03091f" #Azul
# Windows -------------------------------------------------------------------

windows = Tk()
windows.title("")
windows.geometry("400x350")
windows.configure(background=cor1)
windows.resizable(width=FALSE, height=FALSE)

style = Style(windows)
style.theme_use("clam")

# Frame Up -------------------------------------------------------------------
frame_up = Frame(windows, width=450, height=50, background=cor1, relief="flat")
frame_up.grid(row=0, column=0)
# Soon 
app_img =Image.open('soon.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)
app_logo = Label(frame_up, image=app_img, text="Investment Calculator", font=('Verdana 14'), width=350, compound=LEFT, padx=5, anchor=CENTER, background=cor1,foreground=cor0)
app_logo.place(x=5, y=0)
line = Label(frame_up, width=450, height=1, font=('Verdana 1'), background='#4E6E81',foreground=cor1)
line.place(x=0, y=48)

# Frame Question -------------------------------------------------------------------
frame_question = Frame(windows, width=450, height=100, background=cor1, relief="solid")
frame_question.grid(row=1, column=0, padx=5, sticky=NSEW)
# Investiment
app_question = Label(frame_question, text="Investment", width=20, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_question.place(x=50, y=15)
e_value = Entry(frame_question, width=10, font=('Ivy 18'), justify='center', relief='solid', background='#F3E99F', foreground='#4E6E81')
e_value.place(x=15, y=50)
# Days
app_question = Label(frame_question, text="Days", width=10, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_question.place(x=198, y=15)
e_value_days = Entry(frame_question, width=6, font=('Ivy 18'), justify='center', relief='solid', background='#F3E99F', foreground='#4E6E81')
e_value_days.place(x=175, y=50)
# Percentage
app_question = Label(frame_question, text="Percentage %", width=13, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_question.place(x=272, y=15)
e_value_percentage = Entry(frame_question, width=6, font=('Ivy 18'), justify='center', relief='solid', background='#F3E99F', foreground='#4E6E81')
e_value_percentage.place(x=275, y=50)

# Frame Result ------------------------------------------------------------------------
frame_result = Frame(windows, width=300, height=310, background='#4E6E81', relief="raised")
frame_result.grid(row=3, column=0, sticky=NSEW)

# Frame Day ---------------------------------------------------------------------------
frame_day = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_day.grid(row=0, column=0, padx=1, pady=1, sticky=NSEW)
# Daily Result
app_day = Label(frame_day, text="Daily Profit", width=13, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_day.place(x=272, y=15)

# Frame weekly ----------------------
frame_weekly = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_weekly.grid(row=0, column=1, padx=1, pady=1, sticky=NSEW)

# Frame Month ----------------------
frame_month = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_month.grid(row=1, column=0, padx=1, pady=1, sticky=NSEW)

# Frame Totally ----------------------
frame_totally = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_totally.grid(row=1, column=1, padx=1, pady=1, sticky=NSEW)


windows.mainloop()

