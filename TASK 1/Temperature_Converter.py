import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conversion functions
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to perform conversion
def convert_temperature():
    try:
        temp = float(temp_entry.get())
        unit = unit_combobox.get()

        if unit == 'Celsius':
            fahrenheit = celsius_to_fahrenheit(temp)
            kelvin = celsius_to_kelvin(temp)
            result_label.config(text=f"{temp} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K")
        elif unit == 'Fahrenheit':
            celsius = fahrenheit_to_celsius(temp)
            kelvin = fahrenheit_to_kelvin(temp)
            result_label.config(text=f"{temp} °F = {celsius:.2f} °C = {kelvin:.2f} K")
        elif unit == 'Kelvin':
            celsius = kelvin_to_celsius(temp)
            fahrenheit = kelvin_to_fahrenheit(temp)
            result_label.config(text=f"{temp} K = {celsius:.2f} °C = {fahrenheit:.2f} °F")
        else:
            messagebox.showerror("Invalid unit", "Please select a valid unit of measurement.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid temperature.")

# Create the main application window
root = tk.Tk()
root.geometry("800x500")
root.title("Temperature Converter")
root.configure(bg="black")

# Create and place the widgets
temp_label = tk.Label(root, text="Enter Temperature:", bg="white", font=(20))
temp_label.pack(pady=10)

temp_entry = tk.Entry(root, width=30, font=(20))
temp_entry.pack(pady=10)

unit_label = tk.Label(root, text="Select Unit:", bg="white", font=(20))
unit_label.pack(pady=10)

unit_combobox = ttk.Combobox(root, values=['Celsius', 'Fahrenheit', 'Kelvin'], font=(20))
unit_combobox.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Times New Roman",40), bg="black", fg="white")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()