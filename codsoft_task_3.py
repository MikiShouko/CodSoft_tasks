import tkinter as tk
import string
import secrets

# Function to generate a random password
def generate_password():
    password_length = int(password_length_entry.get())
    complexity = complexity_var.get()

    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(secrets.choice(characters) for _ in range(password_length))
    password_var.set(generated_password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create input fields and labels
password_length_label = tk.Label(window, text="Password Length:")
password_length_label.pack()
password_length_entry = tk.Entry(window)
password_length_entry.pack()

complexity_label = tk.Label(window, text="Complexity:")
complexity_label.pack()
complexity_var = tk.StringVar(window)
complexity_var.set("Low")
complexity_menu = tk.OptionMenu(window, complexity_var, "Low", "Medium", "High")
complexity_menu.pack()

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Display the generated password
password_var = tk.StringVar()
password_label = tk.Label(window, textvariable=password_var)
password_label.pack()

# Start the Tkinter main loop
window.mainloop()
