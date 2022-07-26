from cgitb import text
import tkinter as tk
from tkinter import messagebox, Label
from tkinter import *
from tracemalloc import start


root = tk.Tk()
root.title("GRAFICADORA")
root.geometry("600x660")
#root.resizable(0 , 0)


BASE = 580

ALTURA = 500

frame_1 = tk.Frame(root)
frame_1.config(bg = "blue" , width=580 , height = 300)
frame_1.place(x=10,y=10)

frame_2 = tk.Frame(root)
frame_2.config(bg = "red" , width=580 , height = 300)
frame_2.place(x=10,y=320)


x1_label = Label(text="X1: ")
x1_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)
x1_label.place(x=20,y=380)

x1_label.grid(row=0, column=0, sticky= "W", padx=20, pady=380)
x1_entry.grid(row=0, column=1, sticky= "E", padx=10)

boton_grafica = Button(text="GRAFICAR", command='')
boton_grafica.grid(row=2, column=0, padx=10, pady=10, sticky= "W")


tex_label = Label(text="X1: ")
tex_entry = Entry(bd=5, highlightcolor="red", highlightthickness=2)
tex_label.place(x=20,y=380)

tex_label.grid(row=0, column=0, sticky= "W", padx=20, pady=380)
tex_entry.grid(row=0, column=1, sticky= "E", padx=10)




#creacion de lineas

c = tk.Canvas(frame_1, width=BASE, height=ALTURA)
c.place(x=10, y=10)

c.create_line(5,250,580,600, width=3 )






root.mainloop()
