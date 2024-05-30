#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *


# In[1]:


import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Sample data storage using pandas
data = pd.DataFrame(columns=['Date', 'Calories_Consumed', 'Calorie_Goal'])

def add_entry():
    global data
    try:
        date = entry_date.get()
        calories_consumed = int(entry_calories.get())
        calorie_goal = int(entry_goal.get())

        # Validate date
        datetime.strptime(date, '%Y-%m-%d')
        
        # Add data to DataFrame
        new_entry = {'Date': date, 'Calories_Consumed': calories_consumed, 'Calorie_Goal': calorie_goal}
        data = data.append(new_entry, ignore_index=True)
        
        # Clear input fields
        entry_date.delete(0, tk.END)
        entry_calories.delete(0, tk.END)
        entry_goal.delete(0, tk.END)
        
        messagebox.showinfo("Success", "Entry added successfully!")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please check the date format and numeric values.")

def calculate_stats():
    global data
    if data.empty:
        messagebox.showinfo("Stats", "No data available.")
        return
    
    total_calories = data['Calories_Consumed'].sum()
    average_calories = data['Calories_Consumed'].mean()
    total_days = len(data)
    
    stats_message = f"Total Days: {total_days}\nTotal Calories Consumed: {total_calories}\nAverage Calories Per Day: {average_calories:.2f}"
    messagebox.showinfo("Statistics", stats_message)

def plot_data():
    global data
    if data.empty:
        messagebox.showinfo("Plot", "No data available to plot.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Calories_Consumed'], marker='o', label='Calories Consumed')
    plt.plot(data['Date'], data['Calorie_Goal'], marker='x', label='Calorie Goal', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Calories')
    plt.title('Calorie Tracker')
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Create the main window
root = tk.Tk()
root.title("Calorie Tracker")

# Create and place the widgets
tk.Label(root, text="Enter date (YYYY-MM-DD):").grid(row=0, column=0, padx=10, pady=5)
entry_date = tk.Entry(root)
entry_date.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter calories consumed:").grid(row=1, column=0, padx=10, pady=5)
entry_calories = tk.Entry(root)
entry_calories.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Enter calorie goal:").grid(row=2, column=0, padx=10, pady=5)
entry_goal = tk.Entry(root)
entry_goal.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Add Entry", command=add_entry).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="Calculate Stats", command=calculate_stats).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(root, text="Plot Data", command=plot_data).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(root, text="Exit", command=root.quit).grid(row=6, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()


# In[ ]:




