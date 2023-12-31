import tkinter as tk

# Function to perform arithmetic operations
def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operation_var.get()

    if operation == "Add":
        result.set(num1 + num2)
    elif operation == "Subtract":
        result.set(num1 - num2)
    elif operation == "Multiply":
        result.set(num1 * num2)
    elif operation == "Divide":
        if num2 == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(num1 / num2)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Create input fields and labels
label_num1 = tk.Label(window, text="Enter first number:")
label_num1.pack()
entry_num1 = tk.Entry(window)
entry_num1.pack()

label_num2 = tk.Label(window, text="Enter second number:")
label_num2.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a dropdown menu for the operation choice
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_var = tk.StringVar(window)
operation_var.set(operations[0])  # Default operation
operation_menu = tk.OptionMenu(window, operation_var, *operations)
operation_menu.pack()

# Create a button to perform the calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Display the result
result = tk.StringVar()
result_label = tk.Label(window, textvariable=result)
result_label.pack()

# Start the Tkinter main loop
window.mainloop()
