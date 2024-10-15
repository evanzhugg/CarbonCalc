# process_data.py
import tkinter as tk
from Data.Collect import personal, transport, waste, energy, consumption
import matplotlib.pyplot as plt

def calculate_carbon_footprint(data):
    carbon_footprint = {
        'personal': float(data['personal'].get('weight', 0)) * 0.1,
        'transport': float(data['transport'].get('distance', 0)) * 0.05,
        'waste': float(data['waste'].get('amount', 0)) * 0.2,
        'energy': float(data['energy'].get('pc_tv_hours', 0)) * 0.3,
        'consumption': float(data['consumption'].get('grocery_spending', 0)) * 0.4
    }
    total_footprint = sum(carbon_footprint.values())
    return carbon_footprint, total_footprint

def plot_pie_chart(carbon_footprint):
    labels = carbon_footprint.keys()
    sizes = carbon_footprint.values()
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Carbon Footprint Distribution')
    plt.show()

def process_data():
    data = {
        "personal": personal(),
        "transport": transport(),
        "waste": waste(),
        "energy": energy(),
        "consumption": consumption()
    }
    carbon_footprint, total_footprint = calculate_carbon_footprint(data)

    result_window = tk.Tk()
    result_window.geometry("400x200")
    result_window.title("Carbon Footprint Result")

    result_label = tk.Label(result_window, text=f"Your Total Carbon Footprint: {total_footprint:.2f} units")
    result_label.pack(pady=20)

    plot_button = tk.Button(result_window, text="Show Pie Chart", command=lambda: plot_pie_chart(carbon_footprint))
    plot_button.pack(pady=20)

    result_window.mainloop()

if __name__ == "__main__":
    process_data()