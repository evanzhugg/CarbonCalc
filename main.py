import tkinter as tk
from Data.Dump import dump
from Data.Collect import personal, transport, waste, energy, consumption

def collect_data():
    data = {
        "personal": personal(),
        "transport": transport(),
        "waste": waste(),
        "energy": energy(),
        "consumption": consumption()
    }
    dump(data)

main_window = tk.Tk()
main_window.geometry("1920x1080")
main_window.title("Carbon Footprint Calculator")
main_window.configure(background='ForestGreen')

greeting = tk.Label(text="Welcome to the calculator! Please enter some info below by clicking on the buttons", bg="PaleGreen", fg="Gray")
greeting.pack()

personal_button = tk.Button(
    text="Personal Data",
    width=25,
    height=5,
    fg="green",
    command=personal
)
personal_button.pack()

travel_button = tk.Button(
    text="Travel info",
    width=25,
    height=5,
    fg="blue",
    command=transport
)
travel_button.pack()

waste_button = tk.Button(
    text="Waste info",
    width=25,
    height=5,
    fg="purple",
    command=waste
)
waste_button.pack()

energy_button = tk.Button(
    text="Energy info",
    width=25,
    height=5,
    fg="black",
    command=energy
)
energy_button.pack()

consumption_button = tk.Button(
    text="Consumption",
    width=25,
    height=5,
    fg="gold",
    command=consumption
)
consumption_button.pack()
save_button = tk.Button(
    text="Save Data",
    width=25,
    height=5,
    fg="red",
    command=collect_data
)
save_button.pack()

main_window.mainloop()