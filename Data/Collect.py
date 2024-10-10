import tkinter as tk
from tkinter import ttk
import sv_ttk
import os



def personal():
    main_window0 = tk.Tk()
    main_window0.geometry("900x600")
    main_window0.title("Personal Data")
    greeting = tk.Label(main_window0,
        text="\u2B63\u2B63Please enter your personal data below \u2B63\u2B63"
    )
    greeting.pack()

    height_label = tk.Label(main_window0, text="Your height:")
    height_label.pack()
    height = tk.Entry(main_window0, width=20)
    height.pack()

    weight_label = tk.Label(main_window0, text="Your weight:")
    weight_label.pack()
    weight = tk.Entry(main_window0, width=20,)
    weight.pack()

    gender_label = tk.Label(main_window0, text="Your gender:")
    gender_label.pack()
    gender_var = tk.StringVar(main_window0)
    gender_var.set("Select")
    gender_options = ["Male", "Female"]
    gender_menu = tk.OptionMenu(main_window0, gender_var, *gender_options)
    gender_menu.pack()

    diet_label = tk.Label(main_window0, text="Your diet:")
    diet_label.pack()
    diet_var = tk.StringVar(main_window0)
    diet_var.set("Select")
    diet_options = ["Vegan", "Vegetarian", "Pesca", "Omnivore"]
    diet_menu = tk.OptionMenu(main_window0, diet_var, *diet_options)
    diet_menu.pack()

    social_label = tk.Label(main_window0, text="Social activity:")
    social_label.pack()
    social_var = tk.StringVar(main_window0)
    social_var.set("Select")
    social_options = ["Never", "Often", "Sometimes"]
    social_menu = tk.OptionMenu(main_window0, social_var, *diet_options)
    social_menu.pack()


    main_window0.mainloop()

def transport():
    main_window1 = tk.Tk()
    main_window1.geometry("900x600")
    main_window1.title("Transport Data")
    greeting1 = tk.Label(main_window1, text="Here you will enter your transport information")
    greeting1.pack()

    method_label = tk.Label(main_window1, text="Transport method:")
    method_label.pack()
    method_var = tk.StringVar(main_window1)
    method_var.set("Select")
    method_options = ["Public", "Private", "Walk/Bike"]
    method_menu = tk.OptionMenu(main_window1, method_var, *method_options)
    method_menu.pack()

    distance_label = tk.Label(main_window1, text="How long do your travel on vehicle per month in km:")
    distance_label.pack()
    distance = tk.DoubleVar()
    distance_now = tk.Label(main_window1, text="0km")
    distance_now.pack()
    def get_current_value():
        return '{:.2f}'.format(distance.get())
    def slider_changed(event):
        distance_now.configure(text=get_current_value()+"km")
    distance_slider = ttk.Scale(
        main_window1,
        from_=0,
        to=5000,
        orient="horizontal",
        variable=distance,
        command=slider_changed
    )
    distance_slider.pack()

    flight_label = tk.Label(main_window1, text="How often did you fly last month?")
    flight_label.pack()
    flight_var = tk.StringVar(main_window1)
    flight_var.set("Select")
    flight_options = ["Never", "Rarely", "Frequently", "Very Frequently"]
    flight_menu = tk.OptionMenu(main_window1, flight_var, *flight_options)
    flight_menu.pack()


    main_window1.mainloop()


def waste():
    main_window = tk.Tk()
    main_window.geometry("900x600")
    main_window.title("Waste Data")
    greeting = tk.Label(main_window, text="Here you will enter information about your waste")
    greeting.pack()

    bag_label = tk.Label(main_window, text="How big is your waste bag?")
    bag_label.pack()
    bag_var = tk.StringVar(main_window)
    bag_var.set("Select")
    bag_options = ["Small", "Medium", "Large", "Extra Large"]
    bag_menu = tk.OptionMenu(main_window, bag_var, *bag_options)
    bag_menu.configure(fg="Green")
    bag_menu.pack()

    amount_label = tk.Label(main_window, text="How many trash bags do you take out per day?")
    amount_label.pack()
    amount = tk.DoubleVar()
    amount_now = tk.Label(main_window, text="0 bags")
    amount_now.pack()
    def get_current_value():
        return '{:.0f}'.format(amount.get())
    def slider_changed(event):
        amount_now.configure(text=get_current_value()+" bags")
    amount_slider = ttk.Scale(
        main_window,
        from_=1,
        to=10,
        orient="horizontal",
        variable=amount,
        command=slider_changed
    )
    amount_slider.pack()

    recycle_label = tk.Label(main_window, text="Do you recycle any materials below?")
    recycle_label.pack()
    recycle_var = tk.StringVar(main_window)
    recycle_var.set("Select")
    recycle_options = ["Plastic", "Paper", "Metal", "Glass"]
    recycle_menu = tk.OptionMenu(main_window, recycle_var, *recycle_options)
    recycle_menu.configure(fg="Green")
    recycle_menu.pack()


    sv_ttk.set_theme("dark")


    script_dir = os.path.dirname(__file__)
    img_path = os.path.join(script_dir, "../Img/trash.png")
    img = tk.PhotoImage(file=img_path)
    img_label = tk.Label(main_window, image=img)
    img_label.image = img
    img_label.pack()
    main_window.mainloop()

def energy():
    main_window = tk.Tk()
    main_window.title("Energy Data")
    main_window.geometry("900x600")
    greeting = tk.Label(main_window, text="Please enter your energy information below")
    greeting.pack()

    source_label = tk.Label(main_window, text="What power source do you use for heating?")
    source_label.pack()
    source_var = tk.StringVar()
    source_var.set("Select")
    source_options = ["Natural Gas", "Electricity", "Wood", "Coal"]
    source_menu = tk.OptionMenu(main_window, source_var, *source_options)
    source_menu.pack()

    cook_label = tk.Label(main_window, text="What cooking system do you use?")
    cook_label.pack()
    cook_var = tk.StringVar()
    cook_var.set("Select")
    cook_options = ["microwave", "oven", "grill", "air fryer", "stove"]
    cook_menu = tk.OptionMenu(main_window, cook_var, *cook_options)
    cook_menu.pack()

    efficiency_label = tk.Label(main_window, text="Do you consider the efficiency of your devices")
    efficiency_label.pack()
    efficiency_var = tk.StringVar()
    efficiency_var.set("No")
    efficiency_options = ["No", "Yes"]
    efficiency_menu = tk.OptionMenu(main_window, efficiency_var, *efficiency_options)
    efficiency_menu.pack()

    hours_label = tk.Label(main_window, text="How many hours a day do you use your PC/TV")
    hours_label.pack()
    hours = tk.IntVar()
    hours_now = tk.Label(main_window, text="0 Hours")
    hours_now.pack()
    def get_current_value():
        return "{:.0f}".format(hours.get())
    def slider_changed(event):
        hours_now.configure(text=get_current_value()+" hours")
    hours_slider = ttk.Scale(
        main_window,
        from_=0,
        to=24,
        orient="horizontal",
        variable=hours,
        command=slider_changed
    )
    hours_slider.pack()

    internet_label = tk.Label(main_window, text="Whats your daily internet usage?")
    internet_label.pack()
    internet = tk.IntVar()
    internet_now = tk.Label(main_window, text="0 Hours")
    internet_now.pack()
    def get_current_value1():
        return '{:.0f}'.format(internet.get())
    def slider_changed1(event):
        internet_now.configure(text=get_current_value1()+" hours")
    internet_slider = ttk.Scale(
        main_window,
        from_=0,
        to=24,
        orient="horizontal",
        variable=internet,
        command=slider_changed1
    )
    internet_slider.pack()

    main_window.mainloop()

def consumption():
    main_window = tk.Tk()
    main_window.title("Consumption information")
    main_window.geometry("900x600")
    greeting = tk.Label(main_window, text="Please input your consumption info below")
    greeting.pack()

    shower_label = tk.Label(main_window, text="How often do you shower?")
    shower_label.pack()
    shower_var = tk.StringVar()
    shower_var.set("Daily")
    shower_options = ["Daily", "Twice a day", "More frequently", "Less frequently"]
    shower_menu = tk.OptionMenu(main_window, shower_var, *shower_options)
    shower_menu.pack()

    grocery_label = tk.Label(main_window, text="Monthly grocery spending in \u20ac")
    grocery_label.pack()
    grocery = tk.IntVar()
    grocery_now = tk.Label(main_window, text="0 \u20ac")
    grocery_now.pack()
    def get_current_value():
        return '{:.0f}'.format(grocery.get())
    def slider_changed(event):
        grocery_now.configure(text=get_current_value()+" \u20ac")
    grocery_slider = ttk.Scale(
        main_window,
        from_=0,
        to=500,
        orient="horizontal",
        variable=grocery,
        command=slider_changed
    )
    grocery_slider.pack()

    cloth_label = tk.Label(main_window, text="How many clothes do you buy monthly?")
    cloth_label.pack()
    cloth = tk.IntVar()
    cloth_now = tk.Label(main_window, text="0 cloths")
    cloth_now.pack()
    def get_current1_value():
        return '{:.0f}'.format(cloth.get())
    def slider_changed1(event):
        cloth_now.configure(text=get_current1_value()+" clothes")
    cloth_slider = ttk.Scale(
        main_window,
        from_=1,
        to=30,
        orient="horizontal",
        variable=cloth,
        command=slider_changed1
    )
    cloth_slider.pack()

    main_window.mainloop()

consumption()