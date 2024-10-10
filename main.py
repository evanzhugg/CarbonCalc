import tkinter as tk
from Data.Dump import *
from Data.Collect import *

main_window = tk.Tk()
main_window.geometry("1920x1080")
main_window.title("Carbon Footprint Calculator")
main_window.configure(
    background='ForestGreen'
)
greeting = tk.Label(text="Welcome to the calculator! Please enter some info below by clicking on the buttons", bg="PaleGreen", fg="Gray")
greeting.pack()

personal = tk.Button(
    text = "Personal Data",
    width = 25,
    height = 5,
    fg = "green",
    command=personal
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
    fg = "black"
)
energy.pack()

consumption = tk.Button(
    text = "Consumption",
    width = 25,
    height = 5,
    fg = "gold"
)
consumption.pack()

main_window.mainloop()
