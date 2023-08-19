from tkinter.ttk import *
from tkinter import *
from tkinter import ttk
from tkinter import Entry
from PIL import Image, ImageTk
import locale

# Set locale to country -----------------------------------------------
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Investment calculation function -----------------------------------------------
def calculate_profit(event):    
    try:
        initial_investment = float(e_value_investiment.get())
        days_invested = int(e_value_days.get())
        return_percentage = float(e_value_percentage.get())
        
        daily_return = return_percentage / 100 / days_invested
        
        daily_profit = (initial_investment * daily_return)
        weekly_profit = (daily_profit * 7)
        monthly_profit = (daily_profit * 30)
        total_profit = initial_investment * (1 + return_percentage / 100)
        
        e_value_day['text'] = locale.currency(daily_profit, symbol=True, grouping=True)
        e_value_weekly['text'] = locale.currency(weekly_profit, symbol=True, grouping=True)
        e_value_monthly['text'] = locale.currency(monthly_profit, symbol=True, grouping=True)
        e_value_totally['text'] = locale.currency(total_profit, symbol=True, grouping=True)

    except ValueError as e:
        pass

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
app_logo = Label(frame_up, image=app_img, text="Investment Calculator", font=('Verdana 14'), width=350, compound=LEFT, padx=5, anchor=CENTER, background=cor1, foreground=cor0)
app_logo.place(x=5, y=0)
line = Label(frame_up, width=450, height=1, font=('Verdana 1'), background='#4E6E81',foreground=cor1)
line.place(x=0, y=48)

# Frame Question -------------------------------------------------------------------
frame_question = Frame(windows, width=450, height=100, background=cor1, relief="solid")
frame_question.grid(row=1, column=0, padx=5, sticky=NSEW)
# Question Investiment
app_investiment = Label(frame_question, text="Investment", width=20, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_investiment.place(x=52, y=15)
e_value_investiment = Entry(frame_question, width=10, font=('Ivy 18'), justify='center', relief='solid', background='#F3E99F', foreground='#4E6E81')
e_value_investiment.place(x=17, y=50)
# Days
app_days = Label(frame_question, text="Days", width=10, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_days.place(x=198, y=15)
e_value_days = Entry(frame_question, width=6, font=('Ivy 18'), justify='center', relief='solid', background='#F3E99F', foreground='#4E6E81')
e_value_days.place(x=175, y=50)
# Percentage
app_percentage = Label(frame_question, text="Percentage %", width=13, font=('Verdana 10'), anchor=NW, background=cor1,foreground=cor0)
app_percentage.place(x=272, y=15)
e_value_percentage = Entry(frame_question, width=6, font=('Ivy 18'), justify='center', relief='solid', background='#F3E99F', foreground='#4E6E81')
e_value_percentage.place(x=275, y=50)

# Frame Result ------------------------------------------------------------------------
frame_result = Frame(windows, width=300, height=310, background='#4E6E81', relief="raised")
frame_result.grid(row=3, column=0, sticky=NSEW)

# Frame Day ---------------------------------------------------------------------------
frame_day = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_day.grid(row=0, column=0, padx=1, pady=1, sticky=NSEW)
# Daily Result
app_day = Label(frame_day, text="Daily Profit", width=15, anchor=CENTER, font=('Verdana 11'), background=cor1,foreground='#4E6E81')
app_day.place(x=20, y=7)
e_value_day = Label(frame_day, text="", width=10, anchor=CENTER, font=('Verdana 15'), background=cor1,foreground=cor0)
e_value_day.place(x=20, y=35)

# Frame weekly ---------------------------------------------------------------------------
frame_weekly = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_weekly.grid(row=0, column=1, padx=1, pady=1, sticky=NSEW)
# Weekly Profit
app_weekly = Label(frame_weekly, text='Weekly Profit', width=15, anchor=CENTER, font=('Verdana 11'), background=cor1, foreground='#4E6E81')
app_weekly.place(x=20, y=7)
e_value_weekly = Label(frame_weekly, text="", width=10, anchor=CENTER, font=('Verdana 15'), background=cor1,foreground=cor0)
e_value_weekly.place(x=20, y=35)

# Frame Month ---------------------------------------------------------------------------
frame_month = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_month.grid(row=1, column=0, padx=1, pady=1, sticky=NSEW)
# Monthly Profit
app_monthly = Label(frame_month, text='Monthly Profit', width=13, anchor=CENTER, font=('Verdana 11'), background=cor1, foreground='#4E6E81')
app_monthly.place(x=20, y=7)
e_value_monthly = Label(frame_month, text="", width=10, anchor=CENTER, font=('Verdana 15'), background=cor1,foreground=cor0)
e_value_monthly.place(x=20, y=35)

# Frame Totally ---------------------------------------------------------------------------
frame_totally = Frame(frame_result, width=200, height=100, background=cor1, relief="solid")
frame_totally.grid(row=1, column=1, padx=1, pady=1, sticky=NSEW)
# Totally Profit
app_totally = Label(frame_totally, text='Totally Profit', width=15, anchor=CENTER, font=('Verdana 11'), background=cor1, foreground='#4E6E81')
app_totally.place(x=20, y=7)
e_value_totally = Label(frame_totally, text="", width=10, anchor=CENTER, font=('Verdana 15'), background=cor1,foreground=cor0)
e_value_totally.place(x=20, y=35)

# Key Release ---------------------------------------------------------------------------
e_value_investiment.bind("<KeyRelease>", calculate_profit)
e_value_days.bind("<KeyRelease>", calculate_profit)
e_value_percentage.bind("<KeyRelease>", calculate_profit)

windows.mainloop()

