import tkinter as tk
from tkinter import messagebox

def on_click(button_text):
    """Handles button clicks and updates the display."""
    current_text = entry.get()
    
    if button_text == "=":
        try:
            # eval() evaluates the string as a mathematical expression
            result = eval(current_text)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            entry.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
            
    elif button_text == "C":
        entry.delete(0, tk.END)
        
    else:
        # Append the button text to the current entry
        entry.insert(tk.END, button_text)

# Initialize the main window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Create the display area (Entry widget)
entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="flat", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

# Define button labels in a grid layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Create and place buttons using a loop
row_val = 1
col_val = 0

for btn in buttons:
    action = lambda x=btn: on_click(x)
    tk.Button(root, text=btn, width=5, height=2, font=("Arial", 14),
              command=action).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Configure grid weights so buttons expand evenly
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, 5):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()