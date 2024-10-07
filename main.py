import tkinter as tk
from Data.Dump import *

main_window = tk.Tk()
main_window.title("Carbon Footprint Calculator")
main_window.configure(
    background='ForestGreen'
)
greeting = tk.Label(text="Welcome to the calculator, please enter some info below by clicking on the buttons", bg="PaleGreen")
greeting.pack()

personal = tk.Button(
    text = "Personal Data",
    width = 25,
    height = 5,
    fg = "green"
)
personal.pack()

travel = tk.Button(
    text = "Travel info",
    width = 25,
    height = 5,
    fg = "blue",
)
travel.pack()

waste = tk.Button(
    text = "Waste info",
    width = 25,
    height = 5,
    fg = "purple"
)
waste.pack()

energy = tk.Button(
    text = "Energy info",
    width = 25,
    height = 5,
    fg = "yellow"
)
energy.pack()
main_window.mainloop()
