import tkinter as tk
import string
import random

def generate_password():
    length = int(length_var.get())
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    result_window = tk.Toplevel(root)
    result_window.title("Generated Password")
    result_label = tk.Label(result_window, text=f"Generated Password: {password}")
    result_label.pack()

# Create the main application window
root = tk.Tk()
root.title("Password Generator")

# Length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_var = tk.StringVar()  # Password length
length_entry = tk.Entry(root, textvariable=length_var)
length_entry.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Start the GUI event loop
root.mainloop()
